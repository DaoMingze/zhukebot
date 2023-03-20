import json
import os
from nonebot import get_driver
from nonebot.adapters.onebot.v11 import Bot, Event, Message
from nonebot.params import CommandArg
from nonebot.plugin import on_command, on_keyword
from transformers import AutoModel, AutoTokenizer
from torch import compile

basic_config = get_driver().config
if "chatglm_model" in dir(basic_config):
    model_path = basic_config.chatglm_model
else:
    raise RuntimeError("请在.env文件中配置模型存放路径")

if "chatglm_cmd" in dir(basic_config):
    chatglm_cmd = basic_config.chatglm_cmd
else:
    chatglm_cmd = "hi"

if "chatglm_record" in dir(basic_config):
    chatglm_record = basic_config.chatglm_record
else:
    chatglm_record = "./data/history/"

tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = (
    AutoModel.from_pretrained(model_path, trust_remote_code=True)
    .half()
    .quantize(4)
    .cuda()
)

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
chatGLM_chat = on_command(chatglm_cmd, priority=5)
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
    msg = Message(response)
    await chatGLM_chat.finish(msg)


chatGLM_print = on_keyword(["zhuke print", "打印记录"], priority=50)


@chatGLM_print.handle()
async def printrecord(bot: Bot, event: Event):
    qq_id = event.get_user_id()
    msg = readjson(qq_id)
    await chatGLM_print.finish(msg)


"""
chatGLM_clear = on_command("zhuke clear", aliases=["清空记录"], priority=5)


@chatGLM_clear.handle()
async def clear(bot: Bot, event: Event):
    qq_id = event.get_user_id()
    context = []
    savehistory(qq_id,context)
    msg = Message("已清空")
    await chatGLM_clear.finish(msg)
"""
