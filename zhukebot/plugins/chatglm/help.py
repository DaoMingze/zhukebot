from nonebot.plugin import on_keyword
from nonebot.adapters.onebot.v11 import Bot, Event, Message

chatGLM_help = on_keyword(["对话插件帮助"], priority=50)


@chatGLM_help.handle()
async def chatGLM_help_handle(bot: Bot, event: Event):
    message_CQ = Message(
        f"[CQ:at,qq={event.get_user_id()}]\n欢迎使用ChatGLM插件！\
                \n帮助信息如下：\
                \n对话格式“hi[对话内容]”"
    )
    await chatGLM_help.finish(message_CQ)
