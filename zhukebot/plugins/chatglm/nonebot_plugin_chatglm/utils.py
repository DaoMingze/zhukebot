import json
import os
import re
import time

from .config import *


def readfile(name: str, suff: str = "json"):
    """读取chatglm_record路径下的文件，输入文件名和后缀"""
    filename = config.chatglm_record + name + "." + suff
    if os.path.exists(filename):
        with open(filename, "r+", encoding="utf-8") as f:
            if suff == "txt":
                new = f.read()
            else:
                new = json.load(f)
    else:
        new = []
    return new


def savehistory(id: str, context: str):
    """存储与机器人的聊天记录"""
    path = config.chatglm_record + "history/"
    if os.path.exists(path) is False:
        os.mkdir(path)
    with open(path + id + ".json", "w", encoding="utf-8") as f:
        f.write(json.dumps(context))


def check_cd(id):
    """基于发言人，检查冷却时间"""
    nowtime = time.time()
    deltatime = nowtime - cd.get(id, 0)
    if deltatime < config.chatglm_cd:
        return True, deltatime
    else:
        cd[id] = nowtime
        return False, deltatime


def choicerole(role: str = ""):
    """选择预设角色"""
    roles = readfile("roles", "json")
    roleprompt = roles[f"{role}"]
    return roleprompt


emoji = re.compile(
    "["
    "\U0001F300-\U0001F64F"
    "\U0001F680-\U0001F6FF"
    "\u2600-\u2B55"
    "\U00010000-\U0010ffff]+"
)


def ctx_pure(ctx: str):
    """净化输入文本"""
    ctx = ctx.extract_plain_text().strip()
    ctx = re.sub(emoji, "", ctx)
    ctx = re.sub(r"\[CQ[^\s]*?]", "", ctx)
    return ctx
