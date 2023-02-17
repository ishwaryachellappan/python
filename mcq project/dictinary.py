#Dictionary
#A dictionary is just like any other collection array in python. But they have key value pairs. A dictionary is unordered and changeable. We use the keys to access the items from a dictionary. To declare a dictionary, we use the curly brackets.
mydictionary = {'python': 'data science', 'machine learning': 'tensorflow', 'artificial intelligence': 'keras'}

print(mydictionary['machine learning'])

# this will give the output as 'tensorflow'

print(mydictionary.get('python'))

# this serves the same purpose to access the value.

# adding a new value

mydictionary['analysis'] = 'matplotlib'
print(mydictionary)
# replacing a value

mydictionary['analysis'] = 'pandas'
print(mydictionary)
# deleting a value

mydictionary.pop('analysis')
print(mydictionary)

# remove() , del also serves the same purpose for deleting a value.