import asyncio
import os
import re
import shutil
from collections import deque

from nonebot.adapters.onebot.v11 import (
    Bot,
    Event,
    Message,
    MessageSegment,
    PrivateMessageEvent,
)
from nonebot.exception import ParserExit
from nonebot.log import logger
from nonebot.params import CommandArg
from nonebot.permission import SUPERUSER
from nonebot.plugin import on_command, on_keyword, require
from nonebot.rule import to_me

from .config import *
from .utils import *

if config.chatglm_pic:
    require("nonebot_plugin_htmlrender")
    from nonebot_plugin_htmlrender import md_to_pic

# 模块化/函数化功能


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
chat_queue: deque = deque([])

if config.chatglm_tome:
    chatGLM_chat = on_command(
        tuple(config.chatglm_cmd), rule=to_me(), priority=1
    )
else:
    chatGLM_chat = on_command(tuple(config.chatglm_cmd), priority=1)


@chatGLM_chat.handle()
async def args(bot: Bot, event: Event, message: Message = CommandArg()):
    # group_id
    qq_id = event.get_user_id()
    query = message.extract_plain_text().strip()
    flag_cd, deltatime = check_cd(qq_id)
    if flag_cd:
        await chatGLM_chat.finish(
            Message(
                f"[CQ:at,qq={qq_id}]{nickname}认为您问得太快了，您需要{config.chatglm_cd - int(deltatime)}秒来思考这个问题的价值。"
            )
        )
    # 判断简单问题
    flag_stats, query = check_simple(query)
    if flag_stats:
        await chatGLM_chat.finish(Message(f"[CQ:at,qq={qq_id}]{query}"))
    # await chatGLM_chat.send(Message(f"[CQ:at,qq={qq_id}]{nickname}正在运算，请稍候。"))
    # 判断是否角色扮演
    if botrole.get(qq_id, []) != []:
        history = botrole.get(qq_id, [])
        print(f"角色记忆内容为{history}")
    elif check_memo(qq_id):
        history = readfile(qq_id, "json")
    else:
        history = []
    await _chatgen(qq_id, query, history)


async def _chatgen(qq_id, query, history):
    start = time.time()
    try:
        response, new = model.chat(tokenizer, query, history)
        savehistory(qq_id, new)
        if response is None:
            raise RuntimeError("Error")
        message = f"{response}"
    except Exception as e:
        logger.exception("生成失败", stack_info=True)
        # 抓取错误
        message = f"抱歉，{nickname}遭遇了以下错误：\n"
        for i in e.args:
            message += str(i)
        await chatGLM_chat.finish(Message(message))
    torch_gc()
    await chat_answer(qq_id, response)
    end = time.time()
    print(end - start)


async def chat_answer(qq_id, response):
    if config.chatglm_pic:  # 转图片
        if response.count("```") % 2 != 0:
            response += "\n```"
        img = await md_to_pic(response, width=config.chatglm_width)
        response = MessageSegment.image(img)
    if config.chatglm_rply:  # 回复方式
        ans = MessageSegment.at(qq_id) + response
        await chatGLM_chat.finish(ans)
    else:
        await chatGLM_chat.finish(response, at_sender=True)


chatGLM_chooserole = on_command("设置chatglm角色", priority=30)


@chatGLM_chooserole.handle()
async def role(bot: Bot, event: Event, message: Message = CommandArg()):
    qq_id = event.get_user_id()
    ctx = message.extract_plain_text().strip()
    saverole(qq_id, ctx)
    await chatGLM_chooserole.finish(Message(f"[CQ:at,qq={qq_id}]您选取的角色是{ctx}"))


chatGLM_print = on_keyword(
    [config.chatglm_cmd[0] + "export", "导出记录"], priority=40, block=True
)


@chatGLM_print.handle()
async def user_export_handle(bot: Bot, event: Event):
    qq_id = event.get_user_id()
    if isinstance(event, PrivateMessageEvent):  # gocq不支持私聊传文件
        await chatGLM_print.finish(
            Message(f"[CQ:at,qq={qq_id}]暂不支持私聊传文件，可以创建单人群聊后使用命令")
        )
    try:
        response = record + qq_id + ".json"
    except Exception as e:
        logger.error(e)
        await chatGLM_print.finish(Message(f"[CQ:at,qq={qq_id}]{str(e)}"))
    await bot.upload_group_file(
        group_id=event.group_id,
        file=response,
        name=response.split(os.sep)[-1],
    )


chatGLM_clear = on_keyword(
    [config.chatglm_cmd[0] + "clear", "清空记录"], priority=40
)


@chatGLM_clear.handle()
async def clear(bot: Bot, event: Event):
    qq_id = event.get_user_id()
    context = []
    memo[qq_id] = 0
    savehistory(qq_id, context)
    msg = Message("已清空")
    await chatGLM_clear.finish(msg)


chatGLM_allclear = on_command("清理全部", permission=SUPERUSER, priority=50)


@chatGLM_allclear.handle()
async def allclear(bot: Bot, event: Event):
    shutil.rmtree(record)


chatGLM_help = on_keyword(["对话帮助"], priority=50)


@chatGLM_help.handle()
async def chatGLM_help_handle(bot: Bot, event: Event):
    message_CQ = Message(
        f"[CQ:at,qq={event.get_user_id()}]\n欢迎使用ChatGLM插件！\
                \n帮助信息如下：\
                \n对话格式：“hi[对话内容]”\
                \n导出对话历史记录：导出记录\
                \n清空对话历史记录：清空记录"
    )
    await chatGLM_help.finish(message_CQ)
