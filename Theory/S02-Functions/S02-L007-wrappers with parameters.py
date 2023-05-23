import datetime
import functools

#logFilePath = r'G:\Cwiczenia\BackEnd\Python\Kurs Udemy\Kurs2\Theory\S02-Functions\Data\function_log.txt'


def CreateFunctionWithWrapper_logToFile(logFilePath):
    def CreateFunctionWithWrapper(func):
        def func_with_wrapper(*args, **kwargs):
            file = open(logFilePath,'a')
            file.write("-"*20 +"\n")
            file.write('Function "{}" started at {}\n'.format(func.__name__,datetime.datetime.now().isoformat()))
            file.write('Following arguments were used:\n')
            file.write(" ".join("{}".format(x) for x in args))
            file.write("\n")
            file.write(" ".join("{}={}".format(k,v) for (k,v) in kwargs.items()))
            file.write("\n")
            result = func(*args, **kwargs)
            file.write('Function returned {}\n'.format(result))
            file.close()
            return result
        return func_with_wrapper
    return CreateFunctionWithWrapper


@CreateFunctionWithWrapper_logToFile(r'G:\Cwiczenia\BackEnd\Python\Kurs Udemy\Kurs2\Theory\S02-Functions\Data\S02-L007\change_salary_log.txt')
def ChangeSalary(emp_name, new_salary, is_bonus=False):
    print('CHANGING SALARY FOR {} TO {} AS BONUS={}'.format(
        emp_name, new_salary, is_bonus))
    return new_salary

@CreateFunctionWithWrapper_logToFile(r'G:\Cwiczenia\BackEnd\Python\Kurs Udemy\Kurs2\Theory\S02-Functions\Data\S02-L007\change_position_log.txt')
def ChangePosition(emp_name, new_position, is_bonus=False):
    print('CHANGING POSITION FOR {} TO {}'.format(
        emp_name, new_position, is_bonus))
    return new_position


print(ChangeSalary('Johnson', 20000, True))
print(ChangeSalary('Johnson', 20000, is_bonus = True))

print(ChangePosition('Michael','Salesman'))
print(ChangePosition('Anke','Manager'))

