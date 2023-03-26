import json
import os
import re
import time, shutil
from argparse import Namespace

from nonebot.adapters.onebot.v11 import (
    Bot,
    Event,
    GroupMessageEvent,
    Message,
    PrivateMessageEvent,
)
from nonebot.exception import ParserExit
from nonebot.log import logger
from nonebot.params import CommandArg, ShellCommandArgs
from nonebot.permission import SUPERUSER
from nonebot.plugin import on_command, on_keyword, require
from nonebot.rule import ArgumentParser, to_me
from torch import cuda

from .config import *

if config.chatglm_pic:
    require("nonebot_plugin_htmlrender")
    from nonebot_plugin_htmlrender import md_to_pic

# 模块化/函数化功能


def readfile(name: str, suff: str = "json"):
    """读取chatglm_record路径下的文件，输入文件名和后缀"""
    filename = config.chatglm_record + name + "." + suff
    if os.path.exists(filename):
        with open(filename, "r+", encoding="utf-8") as f:
            if suff == "txt":
                new = f.read()
            else:
                new = json.load(f)
    else:
        new = []
    return new


def savehistory(name, context):
    path = config.chatglm_record + "history/"
    if os.path.exists(path) == False:
        os.mkdir(path)
    with open(path + name + ".json", "w", encoding="utf-8") as f:
        f.write(json.dumps(context))


def check_cd(qq_id):
    nowtime = time.time()
    deltatime = nowtime - cd.get(qq_id, 0)
    if deltatime < config.chatglm_cd:
        return True, deltatime
    else:
        cd[qq_id] = nowtime
        return False, deltatime


def choicerole(role=str):
    roles = readfile("roles", "json")
    if role == "":
        role = "catgirl"
    roleprompt = roles[f"{role}"]
    return roleprompt


"""
def chat(id, query, history):
    try:
        response, new = model.chat(tokenizer, query, history=history)
        if response == None:
            raise RuntimeError("Error")
    except Exception as e:
        logger.exception("生成失败", stack_info=True)
        # 抓取错误
        message = f"抱歉，{nickname}遭遇了以下错误：\n"
        for i in e.args:
            message += str(i)
        return message
    savehistory(id, new)
    torch_gc()
    return response
"""


chatGLM_chat = on_command(config.chatglm_cmd[0], priority=8)


emoji = re.compile(
    "["
    "\U0001F300-\U0001F64F"
    "\U0001F680-\U0001F6FF"
    "\u2600-\u2B55"
    "\U00010000-\U0010ffff]+"
)


def ctx_pure(ctx: str):
    ctx = ctx.extract_plain_text().strip()
    ctx = re.sub(emoji, "", ctx)
    ctx = re.sub("\[CQ[^\s]*?]", "", ctx)
    print(ctx)
    return ctx


cmd_help = {
    f"{config.chatglm_cmd}": "唤醒机器人",
    "-l": "控制输入长度",
    "-r": "控制随机性",
    "-p": "控制相关性",
}

"""
@chatGLM_chat.handle()
async def chat_get(event: Event, args: ParserExit = CommandArg()):
    qq_id = event.get_user_id()
    chatGLM_chat.finish(
        f"[CQ:at,qq={qq_id}]{nickname}认为您错误输入了命令，现告知您正确的输入格式：{{cmd_help}}"
    )
"""


@chatGLM_chat.handle()
async def chat(bot: Bot, event: Event, message: Message = CommandArg()):
    # group_id
    qq_id = event.get_user_id()
    # 判断冷却时间
    flag_cd, deltatime = check_cd(qq_id)
    if flag_cd:
        await chatGLM_chat.finish(
            Message(
                f"[CQ:at,qq={qq_id}]{nickname}认为您问得太快了，您需要{config.chatglm_cd - int(deltatime)}秒来思考这个问题的价值。"
            )
        )
    ctx = ctx_pure(message)
    # 判断简单问题
    simple = eval(readfile("simple", "txt"))  # 可以以此加载一些专业词典或免责声明，实际上是fakeAI（假冒AI），最好不要用
    for i in simple.keys():
        a = re.match(i, ctx)
        if a != None:
            ctx = simple.get(i)
        await chatGLM_chat.finish(Message(f"[CQ:at,qq={qq_id}]{ctx}"))
    # 判断记忆
    if config.chatglm_memo:
        history = readfile(qq_id, "json")
    else:
        history = []
    # await chatGLM_chat.send(Message(f"[CQ:at,qq={qq_id}]{nickname}正在运算"))
    query = ctx
    # response = chat(qq_id, query, history)
    try:
        response, new = model.chat(tokenizer, query, history=history)
        savehistory(qq_id, new)
        if response == None:
            raise RuntimeError("Error")
    except Exception as e:
        logger.exception("生成失败", stack_info=True)
        # 抓取错误
        message = f"抱歉，{nickname}遭遇了以下错误：\n"
        for i in e.args:
            message += str(i)
        await chatGLM_chat.finish(Message(message))

    torch_gc()
    msg = Message(f"[CQ:at,qq={qq_id}]{response}")
    await chatGLM_chat.finish(msg)


chatGLM_print = on_keyword([config.chatglm_cmd[0] + "导出记录"], priority=50, block=True)


@chatGLM_print.handle()
async def user_export_handle(bot: Bot, event: Event):
    qq_id = event.get_user_id()
    if isinstance(event, PrivateMessageEvent):  # gocq不支持私聊传文件
        await chatGLM_print.finish(
            Message(f"[CQ:at,qq={qq_id}]暂不支持私聊传文件，可以创建单人群聊后使用命令")
        )
    try:
        response = config.chatglm_record + qq_id + ".json"
    except Exception as e:
        logger.error(e)
        await chatGLM_print.finish(Message(f"[CQ:at,qq={qq_id}]{str(e)}"))
    await bot.upload_group_file(
        group_id=event.group_id,
        file=response,
        name=response.split(os.sep)[-1],
    )


chatGLM_clear = on_keyword([config.chatglm_cmd[0] + "clear"] + ["清空记录"], priority=50)


@chatGLM_clear.handle()
async def clear(bot: Bot, event: Event):
    qq_id = event.get_user_id()
    context = []
    savehistory(qq_id, context)
    msg = Message("已清空")
    await chatGLM_clear.finish(msg)


chatGLM_allclear = on_command("清理全部", permission=SUPERUSER, priority=50)


@chatGLM_allclear.handle()
async def allclear(bot: Bot, event: Event):
    shutil.rmtree(config.chatglm_record)
