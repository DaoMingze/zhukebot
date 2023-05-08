from nonebot import get_driver
from nonebot.log import logger

driver = get_driver()
if chatglm_switch := driver.config.chatglm_switch is True:
    from .nonebot_plugin_chatglm import *

    logger.info("已加载 ChatGLM-6B 支持插件")
else:
    logger.info("停止加载 ChatGLM-6B 支持插件")
