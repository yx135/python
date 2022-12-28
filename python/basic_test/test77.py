import time

before = time.time()
for i in range(100):
    x = 1 + 1
after = time.time()
execution_time = after - before
print(before)
print(after)
print(execution_time)