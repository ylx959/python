
import math
principle=0
rate=0
time=0
while True:
    principle=float(input("enter the interest principle: "))
    if principle<0:
        print("principle cna't be less than ro equal to zero")
    else:
        break

while True:
    rate=float(input("enter the interest rate: "))
    if rate<0:
        print("rate cna't be less than ro equal to zero")
    else:
        break

while True:
    time=float(input("enter the time in years "))
    if time<0:
        print("time cna't be less than ro equal to zero")    
    else:
        break

total=principle*math.pow(1+rate/100,time)

print(f"total: {total:,.2f}")
