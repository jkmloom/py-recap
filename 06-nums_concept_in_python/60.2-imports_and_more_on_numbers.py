import random

print(random.random()) # returns a random value between 0-1

random_integer = random.randint(1, 100) # random integer between 1-100 (100 is excluded)
print(f"random integer (1-100): {random_integer}")

chip = ['Intel', 'AMD', 'Qualcomm', 'Samsung', 'Microsoft', 'Apple', 'Nvidia']
select_chip = random.choice(chip)
print(f"chip company selected at random: {select_chip}")

# deck = ['king', 'queen', 'jack', 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# shuffle_deck = random.shuffle(deck)
# print(f"shuffled cards: {shuffle_deck}")

print(0.1 + 0.1 + 0.1 - 0.3) # unexpeced result
print((0.1 + 0.1 + 0.1) - 0.3) # still unexpected result

from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3')) # expected result
# refer to for context recontext --> DECIMAL CONTEXT MANAGER

from fractions import Fraction
our_fraction = Fraction(2, 7)
print(our_fraction)

# SETS
set_one = {1, 2, 3, 4}
print(type(set_one))
# & --> used for working with intersection of sets
print(set_one & {1, 3})
# | --> used for union
print(set_one | {3, 4, 5})
print("original set: ", set_one)
print(set_one - {1, 2, 3})
print(set_one - {1, 2, 3, 4}) # returns empty set --> set()
print(type({}))

# BOOLEAN
# 1 = True, 0 = False
print(True == 1)
print(False == 0)
print(True is 1)
print(True + 4)
print(10 * False)