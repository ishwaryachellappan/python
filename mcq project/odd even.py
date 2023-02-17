even_and_odd = [1,2,3,4,5,6,7,8,9]
only_even = list(filter((lambda x : (x%2 == 0)), even_and_odd))
print(only_even)
only_odd = list(filter((lambda y : (y%2 != 0)), even_and_odd))
print(only_odd)
