#indexing [start:end:step]


credit_number="1234-1234-1234-1234"
#print(credit_number[0:4])
#print(credit_number[5:9])
#print(credit_number[-1])
#print(credit_number[-1])
#print(credit_number[::3])
last_digit=credit_number[-4:] #負數索引從尾端算起，這裡取最後4碼
print(f"xxxx-xxxx-xxxx-{last_digit}")
print(credit_number[::-1]) #step為-1會把字串反轉