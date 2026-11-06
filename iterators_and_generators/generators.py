# Generator = Function that behaves like an iterator (it can be used in a for loop)
#                      Pauses a function, returns a value, then resumes
#                      Uses 'yield' instead or 'return'
#                      Iterate without loading everything into memory (ex. reading large files)
#                      return = Pouring bucket
#                      yield = Drip faucet
import time

def count_to(n):
    count=1
    while count<=n:
        yield count
        count+=1


number=int(input("enter a number to count to : "))

for n in count_to(number):
    print(n)
    time.sleep(1)

print("time's up⌛️")
