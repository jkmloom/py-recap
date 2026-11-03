score = 10
a_score = 10
# since both the variables ('score' and 'a_score') have same value therefore, they're refering to the same id
print(id(score))
print(id(a_score))

id_var = 5 # if we delete this variable then the value 5 will not refer to any variable

# every memory allocation has a 'ref_count'
# finding the ref_count
# there is no absolute way get the ref_count in python, but we use the following method
import sys
username = 'jkmloom'
print("ref_count for 'username': ", sys.getrefcount(username))

# data type in python is in memory, it doesn't refers to the variable name
# the memory assigns the data type not python (user-side) itself
a = 3 # assigned a vale to 'a'
print(a, id(a))
a = "jkmloom" # updated the assigned value to 'a'
print(a, id(a))
# since, the value 3 has got no reference now you might think that garbage_collector will clean this memory block
# this is ture for majority of the cases but numbers and strings are a few exceptions
# python waits for the possibility that this value can be assigned to a new variable in near future (if not the garbage_collector cleans the block)
# this is 'cause assigning and reassigning uses compute power, so the system here is optimised
a = 3.14 # updated the value again
print(a, id(a))

print('---'*9)

# creating 2 lists
our_list_one = [1, 2, 3]
our_list_two = our_list_one

our_list_one = "jkmloom" # updated the value
print(f"{our_list_one}\n{our_list_two}")

print("---"*9)
our_list_one = [1, 2, 3] # reverting changes
print(f"{our_list_one}\n{our_list_two}")
our_list_one[0] = 99 # updated the index_value[0]
print(f"{our_list_one}\n{our_list_two}")

h1 = [1, 2, 3] # created a simple list
h2 = h1[:] # created a list which is a subset of 'h1'
# h2 is a copy of h1 and they're refering to different memory blocks (or IDs)
print(f"h1: {h1}, id: {id(h1)}")
print(f"h2: {h2}, id: {id(h2)}")
h1[0] = 55 # this is another way to prove it
print(f"h1: {h1}")
print(f"h2: {h2}")

import copy # for clearing out the concept
h2 = copy.copy(h1) # we're doing the same here (making a copy of h1 at a different memory block)
print(f"h1: {h1}, id: {id(h1)}")
print(f"h2: {h2}, id: {id(h2)}")

# working on the concepts
n = [1, 2, 3]
m = n
print(f"n: {n},m: {m}")
print(m == n) # checking (via code) if the values are same
print(m is n) # checking memory reference
m = [1, 2, 3] # now some things while change on the memory allocation part
print(m == n) # still the same (same values)
print(m is n) # different (memory addresses is different for 'n' and 'm')