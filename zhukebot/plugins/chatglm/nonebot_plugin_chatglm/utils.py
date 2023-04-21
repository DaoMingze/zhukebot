import json
import os
import re
import time

from .config import *
from .prompt import *


def readfile(name: str, path: str = record, suff: str = "json"):
    """读取chatglm_record路径下的文件，输入文件名和后缀"""
    filename = path + name + "." + suff
    print(os.path.exists(filename))
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
    if os.path.exists(record) is False:
        os.mkdir(record)
    with open(record + id + ".json", "w", encoding="utf-8") as f:
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


def check_memo(id):
    """基于发言人，检查记忆轮数"""
    deltamemo = memo.get(id, 0)
    if deltamemo < config.chatglm_memo:
        memo[id] = deltamemo + 1
        return True
    else:
        memo[id] = 0
        return False


def saverole(id: str, role: str = ""):
    """记录用户所选角色"""
    if role == "" or "取消":
        botrole[id] = []
    botrole[id] = [roles[role]]
    savehistory(id, botrole[id])
    with open(record + "botroles.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(botrole))


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


def check_simple(ctx):
    """
    可以以此加载一些专业词典或免责声明，实际上是fakeAI（假冒AI），最好不要用
    """
    # ctx = ctx_pure(ctx)
    for i in simple:
        a = re.match(i, ctx)
        if a:
            ctx = simple.get(i)
            return True, ctx
    return False, ctx
