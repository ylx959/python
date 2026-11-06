import time
#defult arguement
def count(end,start=0):
    for x in range(start,end+1):
        print(x)
        time.sleep(0.5)
    print("done")

count(30,15)
