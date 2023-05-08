from nonebot import get_driver
from nonebot.log import logger

driver = get_driver()
if sd_switch := driver.config.sd_switch is True:
    from .nonebot_plugin_sdwebui import *

    logger.info("已加载 SD WebUi 支持插件")
elif sd_switch == "origin":
    from .nonebot_plugin_novelai import *

    logger.info("已加载 原版 插件")
else:
    logger.info("停止加载 SD WebUi 支持插件")
