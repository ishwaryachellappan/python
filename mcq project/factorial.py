def fact(x):
    if x == 0:
        return 1
    return x* fact(x-1)
number = int(input('Enter an integer: '))
print('the factorial of {} is {}'.format(number,fact(number)))
