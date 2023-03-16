from nonebot.plugin import on_command
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import Bot, Event, Message
from nonebot import get_driver
from os import system
from transformers import AutoModel, AutoTokenizer

basic_config = get_driver().config
if "chatglm_path" in dir(basic_config):
    chatglm_path = basic_config.chatglm_path
else:
    raise RuntimeError("请在.env文件中配置模型存放路径")

#chatglm_path = "/home/wdz/aigc/ChatGLM/models"
model = chatglm_path
tokenizer = AutoTokenizer.from_pretrained(model, trust_remote_code=True)
model = (
    AutoModel.from_pretrained(model, trust_remote_code=True).half().quantize(4).cuda()
)
model = model.eval()

chatGLM_chat = on_command("hi", aliases={"你好"}, priority=5)


@chatGLM_chat.handle()
async def chatGLM_help_chat(bot: Bot, event: Event, message: Message = CommandArg()):
    history = []
    query = message.extract_plain_text().strip()
    response, history = model.chat(tokenizer, query, history=history)
    msg = Message(response)
    await chatGLM_chat.finish(msg)
