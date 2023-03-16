from nonebot.log import logger
from nonebot.plugin import PluginMetadata

from .chat import *
from .help import *

logger.info("已加载 ChatGLM-6B 支持插件")

__plugin_meta__ = PluginMetadata(
    name="烛客聊天",
    description="烛客，基于chatGLM-6B模型",
    usage="hi[聊天内容]",
    extra={
        "author": "daomingze",
        "version": "0.1",
        "priority": 8,
    },
)
