from .config import *
import json,os,time,re

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


def savehistory(name, context):
    path = config.chatglm_record + "history/"
    if os.path.exists(path) == False:
        os.mkdir(path)
    with open(path + name + ".json", "w", encoding="utf-8") as f:
        f.write(json.dumps(context))


def check_cd(qq_id):
    nowtime = time.time()
    deltatime = nowtime - cd.get(qq_id, 0)
    if deltatime < config.chatglm_cd:
        return True, deltatime
    else:
        cd[qq_id] = nowtime
        return False, deltatime


def choicerole(role=str):
    roles = readfile("roles", "json")
    if role == "":
        role = "catgirl"
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
    ctx = ctx.extract_plain_text().strip()
    ctx = re.sub(emoji, "", ctx)
    ctx = re.sub("\[CQ[^\s]*?]", "", ctx)
    print(ctx)
    return ctx