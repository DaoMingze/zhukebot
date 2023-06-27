# -*- coding: utf-8 -*-
import os

import nonebot

right_path = __file__.rstrip(os.path.basename(__file__))  # 获取当前文件的所在路径
os.chdir(right_path)  # 将工作路径改至目标路径

# Custom your logger
"""
from nonebot.log import logger, default_format

logger.add(
    "error.log",
    rotation="00:00",
    retention="1 week",
    diagnose=False,
    level="ERROR",
    format=default_format,
    encoding="utf-8",
)
"""
# You can pass some keyword args config to init function
nonebot.init()
# Please DO NOT modify this file unless you know what you are doing!
driver = nonebot.get_driver()
config = driver.config
if config.test_mode is False:
    print(config.test_mode)
    from nonebot.adapters.onebot.v11 import Adapter

    driver.register_adapter(Adapter)
    nonebot.load_plugin("nonebot_plugin_gocqhttp")
else:
    from nonebot.adapters.console import CONAdapter

    driver.register_adapter(CONAdapter)

# As an alternative, you should use command `nb`
# or modify `pyproject.toml` to load plugins
nonebot.load_from_toml("pyproject.toml")
# Modify some config / config depends on loaded configs
APSCHEDULER_CONFIG = {
    "apscheduler.timezone": "Asia/Shanghai",
    "apscheduler.executors.processpool": {
        "type": "processpool",
        "max_workers": "5",
    },
    "apscheduler.job_defaults.coalesce": "false",
    "apscheduler.job_defaults.misfire_grace_time": "60",
    "apscheduler.job_defaults.max_instances": "5",
}


# do something...
app = nonebot.get_asgi()
if __name__ == "__main__":
    nonebot.logger.warning(
        "Always use `nb run` to start the bot instead of manually running!"
    )
    nonebot.run()
