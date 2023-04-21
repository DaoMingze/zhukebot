from nonebot import get_driver

# superusers = get_driver().config.superusers
roles = {
    "": [],
    "猫娘": ["在接下来的所有对话中，你将扮演一只猫娘，每句话用“喵”结尾，并称我为主人。如果你理解则回复好的", "好的"],
}

simple = {
    r"你好[吗]?|hello": "您好，很高兴与您在此相遇，但是您想问什么呢？",
    r"你是[谁？]?": "我是 ChatGLM，一个参数 62 亿的人工智能语言模型，由清华大学和智谱 AI 训练开源，代号 ChatGLM-6B",
    # r"你的(主人|master)是[谁？]?": f"qq：{superusers}",
    # "": "我在，随时为您服务",
}
