import time
import functools



def fib(n):
    
    if n < 2:
        result = n
    else:
        result = fib(n-1) + fib(n-2)
        
    return result


start = time.time()
for n in range(1, 33):
    print('F{} = {}'.format(n, fib(n)))


stop = time.time()

non_cached = stop - start
print('-'*20)
print("Execution time", non_cached)
print('-'*20)

@functools.lru_cache(maxsize=100)
def fib(n):
    
    if n < 2:
        result = n
    else:
        result = fib(n-1) + fib(n-2)
        
    return result


start = time.time()
for n in range(1, 33):
    print('F{} = {}'.format(n, fib(n)))


stop = time.time()
cached = stop - start
print('-'*20)
print("Execution time", cached)
print('-'*20)
print("Kod wykonuje się szybciej",non_cached / cached, 'razy')
print('-'*20)
print(fib.cache_info())



# wykonanie instruktora 
print('-'*20)
print('-'*20)

import time
import functools
 
@functools.lru_cache(maxsize=100)
def fib(n):
    
    if n < 2:
        result = n
    else:
        result = fib(n-1) + fib(n-2)
        
    return result
 
start = time.time()
 
for i in range(34):
    result = fib(i)
    print('{0:2d}  {1}, time = {2:3.2f}'.format(i, result, time.time() - start))
    
print(fib.cache_info())

