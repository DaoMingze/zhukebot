import json
import os
import time
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import (Bot, Event, GroupMessageEvent,
                                         Message, PrivateMessageEvent)
from nonebot.log import logger
from nonebot.params import CommandArg
from nonebot.plugin import on_command, on_keyword

from .config import *
import torch

def readjson(name):
    filename = chatglm_record + name + "rec.json"
    if os.path.exists(filename):
        with open(filename, "r+", encoding="utf-8") as f:
            new = json.load(f)
    else:
        new = []
    return new


def savehistory(name, context):
    with open(chatglm_record + name + "rec.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(context))


def choicerole(role):
    roles = readjson(chatglm_record + "roles.json")  # 待测试完成后统一存放路径到data
    roleprompt = roles[f"{role}"]
    return roleprompt


# on_regex("角色")
chatGLM_chat = on_command(chatglm_cmd, priority=8)
# query = choicerole("0")  # 载入默认
# response, history = model.chat(tokenizer, query, history=history)
# record = [history]


@chatGLM_chat.handle()
async def chat(bot: Bot, event: Event, message: Message = CommandArg()):
    qq_id = event.get_user_id()
    nowtime = time.time()
    deltatime = nowtime - cd.get(qq_id, 0)
    if deltatime < chatglm_cd:
        await chatGLM_chat.finish(Message(f"[CQ:at,qq={qq_id}]，ChatGLM认为您问得太快了，您需要{chatglm_cd - int(deltatime)}秒来思考这个问题的价值。"))
    else:
        cd[qq_id] = nowtime
    prompt = message.extract_plain_text().strip()
    history = readjson(qq_id)
    query = prompt
    response, new = model.chat(tokenizer, query, history=history)
    savehistory(qq_id, new)
    torch.cuda.empty_cache()
    msg = Message(f"[CQ:at,qq={qq_id}]{response}")
    await chatGLM_chat.finish(msg)


chatGLM_print = on_keyword([chatglm_cmd + "print", "导出记录"], priority=50, block=True)


@chatGLM_print.handle()
async def user_export_handle(bot: Bot, event: Event):
    qq_id = event.get_user_id()
    if isinstance(event, PrivateMessageEvent):  # gocq不支持私聊传文件
        await chatGLM_print.finish(
            Message(f"[CQ:at,qq={qq_id}]暂不支持私聊传文件，可以创建单人群聊后使用命令")
        )
    try:
        response = chatglm_record + qq_id + "rec.json"
    except Exception as e:
        logger.error(e)
        await chatGLM_print.finish(Message(f"[CQ:at,qq={qq_id}]{str(e)}"))
    await bot.upload_group_file(
        group_id=event.group_id,
        file=response,
        name=response.split(os.sep)[-1],
    )


chatGLM_clear = on_keyword([chatglm_cmd + "clear", "清空记录"], priority=50)


@chatGLM_clear.handle()
async def clear(bot: Bot, event: Event):
    qq_id = event.get_user_id()
    context = []
    savehistory(qq_id, context)
    msg = Message("已清空")
    await chatGLM_clear.finish(msg)
