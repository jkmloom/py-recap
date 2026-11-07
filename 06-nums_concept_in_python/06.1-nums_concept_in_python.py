# topic title:
# -----------------------------------------
# | CONCEPT OF NUMBERS IN DEPTH IN PYTHON |
# -----------------------------------------

# False = 0, True = 1

print('simple oprations in python')
x, y, z = 2, 3, 4
print(f"{x, y, z}")

# we can carry out simple mathematical operations in python
print(x+y)
# + addition, - substraction, * multiplication, ** power, / and // division, ..
print( x + (y * z))
print(40 + 55.5) # python cares about precision
# but we should not do this. we should use same data types. eg: 40.0 + 55.5
print(int(40 + 55.5)) # or we can also do this -> for integer
print(float(40 + 55.5)) # for floating point value
print('jkmloom'+'@zohomail.in') # concatination
print(x+1, y*2) # multiple operations in one statement
print(y % 2) # finding the remainder after division
print(z ** 2) # finding power
print(2 ** 100) # we can do this with large numbers

result = 1/3.0
print(result)

# try the following on python in terminal: >python
# repr('jkmloom')
# str('jkmloom')
# print('jkmloom')

# comparidion in python
print(1<2) # will return a boolen value (in this case True)
print(5.0 == 5.0) # True
print(4.0 != 5.0) # True
# chained comparision
print("values for x, y, and z: ", x, y, z)
print(x < y < z) # not a good practise while coding a program
print(x < y and y < z) # good practise for the above line
print(1==2<3) # True (but bad practise)
print(1==2 and 2<3) # good practise for the above line
print(1==2 or 2<3) # False

import math # a very commonly used module/library
print(math.floor(3.5)) # returns the closest lowest value
print(math.floor(-3.5))
print(math.floor(3.9))
# --------------------
print(math.trunc(2.8)) # takes closer to 0, returns x.0 (x is the closest value to 0)
print(math.trunc(-2.8))
# --------------------
# number precision in python is very large. for example:
number = 99999999999999999999
print(number**10)
# --------------------
# COMPLEX NUMBERS
complex_number = 2+1j # j here represents the imaginary part (iota - i)
print(type(complex_number))
print(f"complex number (original): {complex_number}")
print(f"complex number (after *2): {complex_number * 2}")
# --------------------
print("octa-decimal 0o20 = ", 0o20) # octa-decimal value (base 8)
print("hexa-decimal 0xFF = ", 0xFF) # hexa-decimal value (base 16)
print("binary 0b10 = ", 0b10) # binary value (base 2)

print("octa-decimal value for 64 = ", oct(64)) # converting decimal value to octa-decimal
print("hexa-decimal value for 64 = ", hex(64)) # convert to hexa-decimal
print("binary value for 64 = ", bin(64)) # convert to binary
print("integer value for a floating-poinr value (3.14) = ", int(3.14))
# --------------------
print(int("64", 8)) # converts an octa-decimal value (passed in string type) to decimal (integer)
# syntax --> print(int("decimal_value", base_value))
print(int("101010", 2))
# --------------------
# BIT-WISE OPERATIONS IN PYTHON
x = 1
print(x << 2) # left shifts value of x by 2 bits
# bit-shifting --> a simple concept in basic computer science