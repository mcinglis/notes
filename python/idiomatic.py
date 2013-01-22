''' idiomatic.py -- examples of idiomatic python code

* http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#generator-expressions-1
* http://www.jeffknupp.com/blog/2012/10/04/writing-idiomatic-python/
'''

# Formatting: always according to PEP8.

# Use docstrings to explain *how to use* the code.

# Use comments to explain *why* and *how the code works*.

# Swapping variables
foo, bar = bar, foo

# Unpacking sequences
row = ('dog', 'Fido', 10)
animal, name, age = row

# Combining list elements into a string
combine = ' '.join(['Words', 'joined', 'by', 'spaces'])

# Providing default dictionary values
host = response.get('host') or DEFAULT_HOST
# Less intuitive
host = response.get('host', DEFAULT_HOST)

# Use implied truthiness liberally
if tester():
    print('It\'s true!')

if get_list():
    print('It\'s not empty!')

# Use context managers for entry and closing operations
with open('data.json', 'r') as data:
    for line in data:
        print(line)

# Use "in" to test for multiple possible equalities
if name in {'Tom', 'Dick', 'Harry'}:
    print('Lucky!')

# Use {list, set, dictionary} comprehensions for filtering other sequences
numbers = range(1, 100)
primes = [n for n in numbers if is_prime(n)]

# For simple generators that should be reused, assign generator expressions
# to variables
adder = (n + 1 for n in get_n())

# Use generator expressions when folding containers
sum_of_squares = sum(n * n for n in range(1, 100))

# Use `enumerate` when the index is required
for index, element in enumerate(container):
    print(index, element)

# Sort sequences with `sorted`
sorted_list = sorted(random_numbers())

# Never use wild-card imports; it makes code harder to maintain.

# Structure modules and scripts like so:

#!/usr/bin/env python

'''Module docstring.'''

# imports
# constants
# exception classes
# public functions
# classes
# internal functions and classes

def main(...):
    ...

if __name__ == '__main__':
    status = main()
    sys.exit(main)


