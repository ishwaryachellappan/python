a = int(input('Enter an integer 1: '))
b = int(input('Enter an integer 2: '))
sum=(lambda x,y: a+b)
sub=(lambda x,y: a-b)
print ('Addition : {}, Subtraction = {}'.format(sum(a,b),sub(a,b)))



