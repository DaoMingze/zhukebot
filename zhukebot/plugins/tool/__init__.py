from nonebot import get_driver, on_command
from nonebot.log import logger
from nonebot.permission import SUPERUSER
from nonebot.plugin import PluginMetadata, inherit_supported_adapters

driver = get_driver()
nickname = driver.config.nickname.pop()

__plugin_meta__ = PluginMetadata(
    name="tool",
    description="零散小工具",
    usage="".strip(),
    type="application",
    homepage="https://github.com/DaoMingze/zhukebot",
    supported_adapters=inherit_supported_adapters(),
)


async def sendtosuperuser(message):
    # 将消息发送给superuser
    import asyncio

    from nonebot import get_bot, get_driver

    superusers = get_driver().config.superusers
    bot = get_bot()
    for superuser in superusers:
        await bot.call_api(
            "send_msg",
            **{
                "message": message,
                "user_id": superuser,
            },
        )
        await asyncio.sleep(5)


"""
@driver.on_bot_connect
async def on_start():
    await sendtosuperuser(f"{nickname}启动完成")
"""
