# multithreading = Used to perform multiple tasks concurrently (multitasking)
#               Good for I/O bound tasks like reading files or fetching data from APIs

import threading
import time

def walk_dog(first):
    time.sleep(8)
    print(f"You finish walking {first}")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the mail")

chore1=threading.Thread(target=walk_dog,args=("Scooby",)) #args是tuple，只有一個值時要加逗號
chore1.start() #start後在背景執行，不用等它結束

chore2=threading.Thread(target=take_out_trash)
chore2.start()

chore3=threading.Thread(target=get_mail)
chore3.start()

chore1.join() #join等待執行緒結束才往下走
chore2.join()
chore3.join()

print("All chores are complete!")
