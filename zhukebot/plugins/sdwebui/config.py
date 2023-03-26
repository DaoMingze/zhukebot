import json
from pathlib import Path

# from .fifo import FIFO
import aiofiles
from nonebot import get_driver
from nonebot.log import logger
from pydantic import BaseSettings, validator
from pydantic.fields import ModelField

driver = get_driver()
jsonpath = Path("data/sdwebui/config.json").resolve()
nickname = (
    list(driver.config.nickname)[0]
    if len(driver.config.nickname)
    else "sdwebui"
)


class Config(BaseSettings):
    sd_site: str = "127.0.0.1:7860"
    """你的服务器配置信息"""
    sd_save: int = 2
    """是否保存图片至本地,0为不保存，1保存jpg(丢失图片chunk信息)，2保存图片原本png"""
    sd_debug: bool = False
    """是否保存追踪信息，这会在图片旁保存同名txt文件"""
    sd_paid: int = 0
    """0为禁用付费模式，1为点数制，2为严格点数制，3为不限制"""
    sd_pure: bool = False
    """是否启用简洁返回模式（只返回图片，不返回tag等数据）"""
    sd_limit: bool = True
    """是否开启限速模式，开启后，每次调用都会检查上次调用时间，如果小于cd则会被拒绝"""
    sd_daylimit: int = 0
    """每日点数限制，0为禁用限制"""
    sd_nsfw: bool = False
    """是否允许H"""
    sd_antireport: bool = True
    """玄学选项。开启后，合并消息内发送者将会显示为调用指令的人而不是bot"""
    sd_max: int = 3
    """每次能够生成的最大数量"""
    sd_size: int = 1024
    """允许生成的图片最大分辨率，对应(值)^2.默认为1024（即1024*1024）。如果服务器比较寄，建议改成640（640*640）或者根据能够承受的情况修改。"""
    sd_tags: str = ""
    """内置的tag"""
    sd_ntags: str = ""
    """内置的反tag"""
    sd_cd: int = 30
    """默认的cd"""
    sd_on: bool = True
    """是否全局开启"""
    sd_revoke: int = 0
    """是否自动撤回，该值不为0时，则为撤回时间"""
    bing_key: str = None
    """bing的翻译key"""
    deepl_key: str = None
    """deepL的翻译key"""

    def keys(cls):
        return (
            "sd_cd",
            "sd_tags",
            "sd_on",
            "sd_ntags",
            "sd_revoke",
        )

    def __getitem__(cls, item):
        return getattr(cls, item)

    @validator("sd_cd", "sd_max")
    def non_negative(cls, v: int, field: ModelField):
        if v < 1:
            return field.default
        return v

    @validator("sd_paid")
    def paid(cls, v: int, field: ModelField):
        if v < 0:
            return field.default
        elif v > 3:
            return field.default
        return v

    class Config:
        extra = "ignore"

    async def set_enable(cls, group_id, enable):
        # 设置分群启用
        await cls.__init_json()
        now = await cls.get_value(group_id, "on")
        logger.debug(now)
        if now:
            if enable:
                return f"sdwebui已经处于启动状态"
            else:
                if await cls.set_value(group_id, "on", "false"):
                    return f"sdwebui已关闭"
        else:
            if enable:
                if await cls.set_value(group_id, "on", "true"):
                    return f"aidraw开始运行"
            else:
                return f"aidraw已经处于关闭状态"

    async def __init_json(cls):
        # 初始化设置文件
        if not jsonpath.exists():
            jsonpath.parent.mkdir(parents=True, exist_ok=True)
            async with aiofiles.open(jsonpath, "w+") as f:
                await f.write("{}")

    async def get_value(cls, group_id, arg: str):
        # 获取设置值
        group_id = str(group_id)
        arg_ = arg if arg.startswith("sd_") else "sd_" + arg
        if arg_ in cls.keys():
            await cls.__init_json()
            async with aiofiles.open(jsonpath, "r") as f:
                jsonraw = await f.read()
                configdict: dict = json.loads(jsonraw)
                return configdict.get(group_id, {}).get(arg_, dict(cls)[arg_])
        else:
            return None

    async def get_groupconfig(cls, group_id):
        # 获取当群所有设置值
        group_id = str(group_id)
        await cls.__init_json()
        async with aiofiles.open(jsonpath, "r") as f:
            jsonraw = await f.read()
            configdict: dict = json.loads(jsonraw)
            baseconfig = {}
            for i in cls.keys():
                value = configdict.get(group_id, {}).get(i, dict(cls)[i])
                baseconfig[i] = value
            logger.debug(baseconfig)
            return baseconfig

    async def set_value(cls, group_id, arg: str, value: str):
        """设置当群设置值"""
        # 将值转化为bool和int
        if value.isdigit():
            value: int = int(value)
        elif value.lower() == "false":
            value = False
        elif value.lower() == "true":
            value = True
        group_id = str(group_id)
        arg_ = arg if arg.startswith("sd_") else "sd_" + arg
        # 判断是否合法
        if arg_ in cls.keys() and isinstance(value, type(dict(cls)[arg_])):
            await cls.__init_json()
            # 读取文件
            async with aiofiles.open(jsonpath, "r") as f:
                jsonraw = await f.read()
                configdict: dict = json.loads(jsonraw)
            # 设置值
            groupdict = configdict.get(group_id, {})
            if value == "default":
                groupdict[arg_] = False
            else:
                groupdict[arg_] = value
            configdict[group_id] = groupdict
            # 写入文件
            async with aiofiles.open(jsonpath, "w") as f:
                jsonnew = json.dumps(configdict)
                await f.write(jsonnew)
            return True
        else:
            logger.debug(f"不正确的赋值,{arg_},{value},{type(value)}")
            return False


config = Config(**get_driver().config.dict())
logger.info(f"加载config完成" + str(config))
