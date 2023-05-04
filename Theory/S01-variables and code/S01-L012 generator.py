listA = list(range(6))
listB = list(range(6))

print(listA, listB)

print()
product = []
for a in listA:
    for b in listB:
        product.append((a, b))
print(product)

print()
product = [(a, b)for a in listA for b in listB]
print(product)

print()
product = [(a, b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0]
print(product)
print()
product = {a: b for a in listA for b in listB if a % 2 == 1 and b % 2 == 0}
print(product)


print()
gen = ((a, b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0)
print(gen)

print(next(gen))
print(next(gen))
print('-'*30)
for x in gen:
    print(x)
print('-'*30)
for x in gen:
    print(x)

print('*'*30)
gen = ((a, b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0)
while True:
    try:
        print(next(gen))
    except StopIteration:
        print('all values have been generated')
        break


