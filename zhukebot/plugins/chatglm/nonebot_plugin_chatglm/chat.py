import json
import os

from nonebot import get_driver
from nonebot.adapters.onebot.v11 import (
    Bot,
    Event,
    GroupMessageEvent,
    Message,
    PrivateMessageEvent,
)
from nonebot.log import logger
from nonebot.params import CommandArg
from nonebot.plugin import on_command, on_keyword
from torch import compile
from transformers import AutoModel, AutoTokenizer

basic_config = get_driver().config
if "chatglm_model" in dir(basic_config):
    model_path = basic_config.chatglm_model
else:
    model_path = "THUDM/chatglm-6b-int4"

if "chatglm_cmd" in dir(basic_config):
    chatglm_cmd = basic_config.chatglm_cmd
else:
    chatglm_cmd = "hi"

if "chatglm_record" in dir(basic_config):
    chatglm_record = basic_config.chatglm_record
else:
    chatglm_record = "./data/history/"

tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = AutoModel.from_pretrained(model_path, trust_remote_code=True).half().cuda()

model = compile(model).eval()


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
    prompt = message.extract_plain_text().strip()
    history = readjson(qq_id)
    query = prompt
    response, new = model.chat(tokenizer, query, history=history)
    savehistory(qq_id, new)
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
