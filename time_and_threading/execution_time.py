# HOW TO MEASURE EXECUTION TIME IN PYTHON

import time

start_time=time.perf_counter() #perf_counter適合用來量測時間差


for i in range(100000):
    pass

end_time=time.perf_counter()

elapsed_time=end_time-start_time

print(f"Elapsed time:{elapsed_time:.6f} seconds")



