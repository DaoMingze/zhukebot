from nonebot.plugin import PluginMetadata

from .chat import *
from .help import *
from .config import *

__plugin_meta__ = PluginMetadata(
    name="ChatGLM聊天",
    description="基于chatGLM-6B模型",
    usage="hi[聊天内容]，清空记录，导出记录",
    extra={
        "author": "daomingze",
        "version": "0.1.4",
        "priority": 8,
    },
)
