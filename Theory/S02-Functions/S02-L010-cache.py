import time
import functools


@functools.lru_cache(maxsize=256)  # python będzie zapamiętywać już raz wykonane funkcje
def Factorial(n):

    time.sleep(0.1)
    if n == 1:
        return 1
    else:
        return n * Factorial(n-1)


start = time.time()
for i in range(1, 11):
    print('{}! = {}'.format(i, Factorial(i)))
stop = time.time()

print("Execution time", stop - start)

print(Factorial.cache_info())


# start = time.time()
# for i in range(1, 11):
#     print('{}! = {}'.format(i, Factorial(i)))
# stop = time.time()

# print("Execution time", stop - start)

