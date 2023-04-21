import os

from nonebot import get_driver
from nonebot.log import logger
from pydantic import BaseSettings
from torch import compile, cuda
from transformers import AutoModel, AutoModelForSeq2SeqLM, AutoTokenizer


class Config(BaseSettings):
    chatglm_model: str = "./data/chatglm/model"
    """ChatGLM 模型路径，可用HuggingFace Hub格式（将远程加载），默认使用INT-QE模型，降低硬件需求及压力"""
    chatglm_mode: str = "cpu"
    """模型加载模式，默认CPU加载"""
    chatglm_cmd: list = ["hi"]
    """调用机器人命令"""
    chatglm_cd: int = 10
    """冷却时间"""
    chatglm_path: str = "./data/chatglm/"
    """chatglm相关中间文件存放路径"""
    chatglm_memo: int = 5
    """记录对话轮数"""
    chatglm_tome: bool = False
    """是否需要at机器人"""
    chatglm_group: bool = False
    """是否群聊共用记录"""
    chatglm_pic: bool = False
    """是否转图片"""
    chatglm_width: int = 640
    """图片宽度"""
    nickname: list[str] = ["ChatGLM"]
    """机器人的昵称"""

    class Config:
        extra = "ignore"


def torch_gc():
    if cuda.is_available():
        with cuda.device(CUDA_DEVICE):
            cuda.empty_cache()
            cuda.ipc_collect()


config = Config(**get_driver().config.dict())  # 格式化加载配置
model_name = "THUDM/chatglm-6b-int4-qe"
model_path = config.chatglm_model
if os.path.exists(model_path) is False:
    print(f"正在下载{model_name}，并保存到{model_path}")
    tokenizer = AutoTokenizer.from_pretrained(
        model_name, trust_remote_code=True, revision="main"
    )
    model = AutoModelForSeq2SeqLM.from_pretrained(
        model_name, trust_remote_code=True, revision="main"
    )
    tokenizer.save_pretrained(
        model_path, trust_remote_code=True, revision="main"
    )
    model.save_pretrained(model_path, trust_remote_code=True, revision="main")
elif os.path.exists(model_path):
    print(f"正从{model_path}加载模型")
else:
    model_path = model_name
    print(f"已加载{model_name}")

tokenizer = AutoTokenizer.from_pretrained(
    model_path, trust_remote_code=True, revision="main"
)

if config.chatglm_mode.lower() == "cuda":
    model = (
        AutoModel.from_pretrained(
            model_path, trust_remote_code=True, revision="main"
        )
        .half()
        .cuda()
    )
    DEVICE = "cuda"
    DEVICE_ID = "0"
    CUDA_DEVICE = f"{DEVICE}:{DEVICE_ID}" if DEVICE_ID else DEVICE
else:
    model = AutoModel.from_pretrained(
        model_path, trust_remote_code=True, revision="main"
    ).float()

model = compile(model).eval()

cd = {}
nickname = config.nickname[0]
memo = {}
record = config.chatglm_path + "record/"
botrole = {"": []}
