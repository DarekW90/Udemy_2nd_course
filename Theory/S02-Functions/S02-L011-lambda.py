def double(x):
    return x*2


x = 10
x = double(x)
print(x)
print ('-'*20)

x = 10 
f = lambda x: x*2
print(f(x))
print ('-'*20)


def power(x,t):
    return x**y 

x = 5
y = 3
print(power(x,y))
print ('-'*20)

f = lambda x,y: x ** y
print (f(x,y))
print ('-'*20)

list_numbers = [1,2,3,4,11,14,15,20,21]

def is_odd(x):
    return x % 2 != 0

print(is_odd(7), is_odd(4))

filtered_list = list(filter(is_odd, list_numbers))
print(filtered_list)
print ('-'*20)

list_numbers = [1,2,3,4,11,14,15,20,21]

def is_odd(x):
    return x % 2 != 0

print(is_odd(7), is_odd(4))

filtered_list = list(filter(lambda x: x%2!=0, list_numbers))
print(filtered_list)
print ('-'*20)

print(list(filter(lambda x: x%2 != 0, list_numbers)))
print ('-'*20)

def generate_multiply_function(n):
    return lambda x: n*x

mul_2 = generate_multiply_function(2)
mul_3 = generate_multiply_function(3)

print(mul_2(13), mul_3(8))

