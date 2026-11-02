'''
- numbers -> 123, 3.45, 3+7j, 0b111, Decimal(), Fraction()
- string -> 'jkmloom', "loom's", b'a\x01c', u'sp\xc4m'
- list -> [1, 2.3, '4', 'jkmloom'], ['loom', True, [1, 2, 3]]
- tuple -> (1, 'jkmloom', 5, 'U') --> tuple()
- dictinary -> {'intel':'core 5', 'amd':'ryzen 5', 'apple':'m5', 'qualcomm':'snapdragon x'}
- set -> set('abc'), {'a', 'b', 'c'}

[] -> brackets
() -> parenthesis
{} -> braces/curly braces


- file -> open('eggs.txt'), open(r'C:\ham.bin', 'wb')
- boolean -> True, Flase
- none -> None (an empty reference)
- functions, modules, classes


- advanced --> decorators, generators, iterators
- MetaProgramming
'''

print(12 + 12) # eg. of a simple math operaiton
print(2.5 * 5) # o/p -> decimal value (python prefers precision here)
print(2 ** 10) # refers to 2 to the power of 10

import random # importing external/in-built libraries
print(f"random value:\t{random.random()}") # generate a random number
print("random number from [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: ", random.choice([0, 1, 2, 3, 4, 56, 7, 8, 9])) # choose randomly from a defined list of numbers

# strings
username = "jkmloom" # declare an username
print("username:", username, "\nusername's character length: ", len(username)) # find it's character length
print(username[0]) # indexing on a string value
# since a 'string' is immutable we can not update the value at a given index (unlike in list, list is mutable)
print(username[-1]) # starts counting the index backwards, from last index
print(username[1:3]) # slice indexing in string (3rd value/character is exculded)

print(dir(username)) # shows what all we can do with this variable

our_list = ['t', True, 0b10011, 90] # list in python is the in-built equivalent of an array
print(our_list) # the binary value 0b10011 should be translated to it's decimal value (19) in the output
print(f"length of the list: our_list -> {len(our_list)}") # length of list = no. of elements in it

ourD = {'intel':'core 5', 'amd':'ryzen 5', 'qualcomm':'snapdragon x'} # declaring a dictionary
# dictionary format -> {key:value}
print(ourD['intel']) # finding a value via keys

ourTup = (1, 2, 3, 4, 5) # declaring a tuple
print(ourTup[0])