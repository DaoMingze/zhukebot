import time

from ..config import config


class DayLimit:
    day: int = time.localtime(time.time()).tm_yday
    data: dict = {}

    @classmethod
    def count(cls, user: str, num):
        day_ = time.localtime(time.time()).tm_yday
        if day_ != cls.day:
            cls.day = day_
            cls.data = {}
        count: int = cls.data.get(user, 0) + num
        if count > config.sd_daylimit:
            return -1
        else:
            cls.data[user] = count
            return config.sd_daylimit - count
