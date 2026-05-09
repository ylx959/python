import time
h=int(input("enter the time in hours:"))

m=int(input("enter the time in minutes:"))
while m>=60:
    print("it can be over 60 !")
    m=int(input("enter the time in minutes:"))
   
s=int(input("enter the time in seconds:"))
while s>=60:
        print("it can be over 60 !")
        s=int(input("enter the time in seconds:"))
for x in range(1,4):
     print(x)

h*=3600
m*=60
my_time=h+m+s

for  x in range(my_time,0,-1):
    hour=int(x/3600)
    minute=int(x/60)%60
    second=x%60
    print(f"{hour:02}:{minute:02}:{second:02}")
    time.sleep(1)

print("Time's up?")

