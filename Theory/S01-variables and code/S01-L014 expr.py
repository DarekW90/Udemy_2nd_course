var_x = 10

source = 'var_x + 4'

result = eval(source)
print(result)
print('-'*30)

# source = 'var_x = 4 '
result = exec(source)
print(result)
print(var_x)
print('-'*30)

source = '''
new_var = 1
for i in range(var_x):
    print('-'*i)
    new_var += i
'''
result = exec(source)
print(result)

print(var_x)
print('new_var =', new_var)

print('-'*30)
source = input('Enter you expression: ')
print(eval(source))
print('-'*30)