import json
import os
from nonebot import get_driver
from nonebot.adapters.onebot.v11 import Bot, Event, Message
from nonebot.params import CommandArg
from nonebot.plugin import on_command, on_regex
from transformers import AutoModel, AutoTokenizer
from torch import compile

basic_config = get_driver().config
if "chatglm_path" in dir(basic_config):
    model_path = basic_config.chatglm_path
else:
    raise RuntimeError("请在.env文件中配置模型存放路径")

if "chatglm_cmd" in dir(basic_config):
    chatglm_cmd = basic_config.chatglm_cmd
else:
    chatglm_cmd = "hi"
hispath = basic_config.chatglm_hispath + "history/"

tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = (
    AutoModel.from_pretrained(model_path, trust_remote_code=True)
    .half()
    .quantize(4)
    .cuda()
)

model = compile(model).eval()


def readjson(path):
    with open(path, "r", encoding="utf-8") as f:
        new = json.load(f)
    return new


def choicerole(role):
    roles = readjson(basic_config.chatglm_hispath + "roles.json")  # 待测试完成后统一存放路径到data
    roleprompt = roles[f"{role}"]
    return roleprompt


# on_regex("角色")
chatGLM_chat = on_command(chatglm_cmd, aliases={"你好"}, priority=5)
history = []
query = choicerole("0")  # 载入默认
response, history = model.chat(tokenizer, query, history=history)
record = []

@chatGLM_chat.handle()
async def chatGLM_help_chat(bot: Bot, event: Event, message: Message = CommandArg()):
    qq_id = event.get_user_id()
    prompt = message.extract_plain_text().strip()

    def history2json(user, history):
        """
        导出对话历史到本地，为后续载入准备
        """
        rec = hispath + user + "rec.json"
        if os.path.exists(rec) == False:
            with open(rec, "w", encoding="utf-8") as f:
                f.write('[["",""]]')
        with open(rec, "r", encoding="utf-8") as file:
            record = json.load(file)
            record.append(history)
        with open(rec, "a", encoding="utf-8") as file_new:
            json.dump(record,file_new)

    def genetext(user, prompt):
        query = prompt
        response, history = model.chat(tokenizer, query, history=history)
        history2json(user, history)
        return response

    response = genetext(qq_id, prompt)
    msg = Message(response)
    await chatGLM_chat.finish(msg)
