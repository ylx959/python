import time
h=int(input("enter the time in hours:"))

m=int(input("enter the time in minutes:"))

while m>=60:
    print("it can't be over 60 !")
    m=int(input("enter the time in minutes:"))
   
s=int(input("enter the time in seconds:"))
while s>=60:
    print("it can't be over 60 !")
    s=int(input("enter the time in seconds:"))


h*=3600
m*=60
my_time=h+m+s #全部換算成秒

for x in range(my_time,-1,-1): #step為-1代表倒數
    hour=int(x/3600)
    minute=int(x/60)%60 #%60 去掉已經算進小時的部分
    second=x%60
    print(f"{hour:02}:{minute:02}:{second:02}") #:02 不足兩位時前面補0
    time.sleep(1)

print("Time's up!")

