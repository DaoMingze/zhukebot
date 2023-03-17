import json
import os
rec = "/home/wdz/aigc/zhukebot/data/chatglm/history/135wrec.json"
history = ["ssddsafcvfds","sadsafcsdac"]
record = []

if os.path.exists(rec) == False:
    with open(rec, "w", encoding="utf-8") as f:
        json.dump(history, f)
with open(rec, "r", encoding="utf-8") as file:
    record = json.load(file)
    record.append(history)
    print(record)
with open(rec, "w", encoding="utf-8") as f:
    json.dump(record,f)