import time 

source = 'reportLine += 1'

reportLine = 0


start = time.time()
for i in range(100000):
    exec(source)
stop = time.time()
time_not_compiled = stop - start


start = time.time()
sourceCompiled = compile(source, 'internal variable source', 'exec')
for i in range(100000):
    exec(sourceCompiled)
stop = time.time()
time_compiled = stop - start

print('Czas programu nie skompilowanego: ', time_not_compiled)
print('Czas programu skompilowanego: ', time_compiled)
print('Ile razy szybciej: ', time_not_compiled/time_compiled)