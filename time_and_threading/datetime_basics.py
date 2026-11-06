import datetime

date=datetime.date(2025,1,2)
today=datetime.date.today()

time=datetime.time(12,30,0)
now=datetime.datetime.now()

now=now.strftime("%H:%M:%S %m-%d-%Y") #strftime把時間轉成指定格式的字串

print(date)
print(today)
print(time)
print(now)

target_datetime=datetime.datetime(2030,1,2,12,30,1)
current_datetime=datetime.datetime.now()

if target_datetime<=current_datetime: #時間可以直接比較大小
    print("pass")
else:
    print("yet to come")
