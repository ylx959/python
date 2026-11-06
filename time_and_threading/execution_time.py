# HOW TO MEASURE EXECUTION TIME IN PYTHON

import time

start_time=time.perf_counter()


for i in range(100000):
    pass

end_time=time.perf_counter()

elapsed_time=end_time-start_time

print(elapsed_time)



