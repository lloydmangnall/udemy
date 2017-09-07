# python provide 3 modules for Date & Time calculations
import time
# import datetime
# import locale
# import calendar

# print(time.gmtime(0))
# print(time.localtime())
# print(time.time())

# time_here = time.localtime()
# print(time_here)
# print("Year:", time_here[0], time_here.tm_year)
# print('Month:', time_here[1], time_here.tm_mon)
# print('Day:', time_here[2], time_here.tm_mday)

# a simple reaction time game to demonstrate the time module
# from time import time as my_timer  # use for dealing with real times
# from time import perf_counter as my_timer  # best for actual elapsed time
# from time import monotonic as my_timer
from time import process_time as my_timer  # measures actual CPU time - useful for profiling code
import random

input("Press enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to stop")

end_time = my_timer()

print("Started at " + time.strftime('%X', time.localtime(start_time)))
print("Ended at " + time.strftime('%X', time.localtime(end_time)))

print("Your reaction time was {} seconds".format(end_time - start_time))
