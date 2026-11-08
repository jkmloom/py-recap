# practise code by @jkmloom (aka jatin kumar mehta) 08/11/2026

chip = "hetmind intelligence" # assumed company name
print(chip)
sliced_chip = chip[0]
print("1st character (company name): ", sliced_chip)
sliced_chip = chip[0:7]
print(f"brand name: {sliced_chip}")

# practising slicing of string in python
nums = "0123456789"
print(nums[:])
print(nums[0:])
print(nums[:5])
print(nums[::2])
print(nums[0::3])

# getting back to "chip = hetmind intelligence"
print("chip variable =", chip)
print(chip.lower())
print(chip.upper())

chip = "  hetmind  "
print(chip)
print(chip.strip()) # this removes unwanted spaces before and after the characters

chip = "labsloom intelligence" # another assumed company name
print("chip company name (assumed):", chip)
print("after replacing -->", chip.replace("labsloom", "hetmind")) # searches for the part of string defined in the function and replaces it
print("original value -->", chip) # the original value of the variable is unaffected

chai = "lemon, ginger, masala, mint" # defined a list but in string data type
# convert string into list
print(chai.split()) # default split value " " --> white space
print(chai.split(", ")) # we define custom spliting value. here --> ", "

isp_india = "jio, airtel, vi, bsnl"
print(isp_india.find("bsnl")) # the o/p index value is from where the name starts
print(isp_india.find("mtnl")) # if the value is not available .find() will return --> -1

customers = "jio, jio, jio, airtel, jio, airtel, vi, jio, airtel, jio" # assume the data of 10 random customers
print(customers.count("airtel")) # counting the frequency of a sliced_string

customers_type = "gen-z"
quantity = 10
details = "user size: {}\npopulation type: {}\ncustomers (airtel): {}" # {} in strings are called place-holders
print(details.format(quantity, customers_type, customers.count('airtel'))) # we can fill these place holders with values

# converting list to string
chip_companies = ['intel', 'amd', 'apple', 'samsung', 'microsoft', 'qualcomm', 'etc..']
print(" ".join(chip_companies))
print(", ".join(chip_companies))

chai = "masala chai"
print(len(chai)) # find length of a string

# printing every letter of the value in variable chai
for letter in chai:
    print(letter, end=" ")
print()
# \"\" --> allows to use "" as printable character in the print() function
thought = "she thinks @jkmloom is not a cool username. \"I THINK SHE'S WRONG!\""
print(thought)
# this is usually proven very helpful while defining path in python code

# another example
text = "hello\nworld" # normal string
print(text)
text = r"hello\nworld" # this will be treated as a raw string
print(text)

import_file = r"c:\user\pwd" # example (path assumed for a windows system althouth this code was originally written on Arch)
print(import_file)

assumed_company = "hetmind intelligence"
print("hetmind" in assumed_company) # asking the function if a string is present --> True
print("labsloom" in assumed_company) # False
