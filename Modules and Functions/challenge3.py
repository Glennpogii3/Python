import time
from time import process_time as my_timer
import random

print("time():\t\t\t", time.get_clock_info('time'))
print("perf_counter():\t\t\t", time.get_clock_info('perf_counter'))
print("monotonic():\t\t\t", time.get_clock_info('monotonic'))
print("process_time():\t\t\t", time.get_clock_info('process_time'))
