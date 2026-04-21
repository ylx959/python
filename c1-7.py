#indexing [start:end:start]


credit_number="1234-1234-1234-1234"
#print(credit_number[0:4])
#print(credit_number[5:9])
#print(credit_number[-1])
#print(credit_number[-1])
#print(credit_number[::3])
last_digit=credit_number[-4:]
print(f"xxxx-xxxx-xxxx-{last_digit}")
print(credit_number[::-1])