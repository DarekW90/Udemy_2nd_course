for i in range(10):
    print(i)

print("-"*30)
for i in range(1, 11):
    print(i)

print("-"*30)
for i in range(1, 11, 2):
    print(i)

print("-"*30)
for i in range(10, 0, -1):
    print(i)

print("-"*30)

list1 = range(10)
print('List:', list1, type(list1))

print("-"*30)

list2 = list(range(10))
print('List:', list, type(list2))
print(list[5:7])
print(list[5:])
print(list[:-1])
print(list[5:-1])
print(list[5:-3])
print(list[:8:2])
print(list[-1:0:-1])
print(list[-1::-1])

print("-"*30)

list3 = list(range(10))
print('List3:', list3, type(list3), id(list3))
list4 = list3
print('List4:', list4, type(list4), id(list4))
list3 = list(range(10))
print("-"*30)
print('List3:', list3, type(list3), id(list3))
list4 = list3.copy()
print('List4.copy():', list4, type(list4), id(list4))
list4 = list3[:]
print('List4[:]:', list4, type(list4), id(list4))


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

my_days = days[:]
my_days = my_days + ['Saturday', 'Sunday']

print(days[-2:-1])
