from . import config, manage
from .aidraw import Draw
from .help import help
from nonebot.plugin import PluginMetadata
from nonebot.log import logger

logger.info("已加载SD WebUi 支持插件")

__plugin_meta__ = PluginMetadata(
    name="SD绘画",
    description="基于Stable Diffusion Webui，是对nonebot-plugin-novelai的精简",
    usage="[绘画|咏唱|召唤|aidraw][命令参数+prompt]\n-m模型，-w采样方法，-r分辨率，-c服从度，-l层数，-s种子，-t步数，-u负面标签，-e修改强度（0-1），-n修改噪声，-o无视预设",
    extra={
        "author": "daomingze",
        "version": "0.1",
        "priority": 8,
    },
)
