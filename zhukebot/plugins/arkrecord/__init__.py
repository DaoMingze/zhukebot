from nonebot.log import logger
from nonebot.plugin import PluginMetadata

from .ark import *

logger.info("已加载方舟抽卡分析插件")

__plugin_meta__ = PluginMetadata(
    name="方舟抽卡分析",
    description="",
    usage="方舟卡池更新、方舟抽卡token、方舟抽卡分析",
    extra={
        "author": "zheuziihau",
        "version": "1.7.1",
        "priority": 8,
    },
)
