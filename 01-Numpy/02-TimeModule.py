import time

a = 5
start = time.time()
for i in range(0,100000000):
    a = a+i

end = time.time()

print("Total time taken",end-start)
