from torch import compile
from transformers import AutoModel, AutoTokenizer
from nonebot import get_driver

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

if "chatglm_mode" in dir(basic_config):
    chatglm_mode = basic_config.chatglm_mode
    print(f"启用{chatglm_mode}模式")
    if chatglm_mode.lower() == "cuda":
        model = AutoModel.from_pretrained(model_path, trust_remote_code=True).half().cuda()
        model = compile(model).eval()
    elif chatglm_mode.lower() == "rwkv":
        from .mini_rwkv import *
    else:
        model = AutoModel.from_pretrained(model_path, trust_remote_code=True).float()
        model = compile(model).eval()
else:
    model = AutoModel.from_pretrained(model_path, trust_remote_code=True).float()
    model = compile(model).eval()

if "chatglm_cd" in dir(basic_config):
    chatglm_cd = basic_config.chatglm_cd
else:
    chatglm_cd = 30

cd = {}