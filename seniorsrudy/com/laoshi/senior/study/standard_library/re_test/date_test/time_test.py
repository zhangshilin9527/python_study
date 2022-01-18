import datetime
import time

print(time.time())  # 1642486437.9088163
# time.struct_time(tm_year=2022, tm_mon=1, tm_mday=18, tm_hour=14, tm_min=13, tm_sec=57, tm_wday=1, tm_yday=18, tm_isdst=0)
print(time.localtime())
print(time.strftime('%Y%m%d'))  # 20220118
print(time.strftime('%Y-%m-%d'))  # 2022-01-18
print(time.strftime('%Y-%m-%d %H:%M%S'))  # 2022-01-18 14:1357

print(datetime.datetime.now())  # 2022-01-18 14:21:25.628625
newtime = datetime.timedelta(minutes=10)  # 偏移量 10分钟
print(datetime.datetime.now() + newtime)  # 2022-01-18 14:31:25.628625

one_day = datetime.datetime(2022, 1, 18)
new_date = datetime.timedelta(days=10)  # 偏移量 10天
print(one_day + new_date)  # 2022-01-28 00:00:00
