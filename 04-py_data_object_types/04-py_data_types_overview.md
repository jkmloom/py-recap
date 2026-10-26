# Python Data Types: The Big Picture

> Revision notes on Python's built-in data types, what they represent, and when to use them.

---

## 1. What Is a Data Type?

A **data type** describes the kind of value an object represents and the operations that make sense for it.

```python
age = 21
price = 19.99
name = "Jatin"
is_learning = True
```

Here, `21` is an `int`, `19.99` is a `float`, `"Jatin"` is a `str`, and `True` is a `bool`.

Types matter because operations behave differently depending on the values involved:

```python
print(10 + 5)
print("hello " + "Python")
```

Output:

```text
15
hello Python
```

The `+` operator performs arithmetic for numbers and concatenation for strings.

## 2. Python Is Dynamically Typed

Python determines an object's type at runtime. We do not normally declare a variable's type in advance.

```python
value = 10
print(type(value))

value = "ten"
print(type(value))
```

Output:

```text
<class 'int'>
<class 'str'>
```

More precisely, **objects have types; variable names refer to objects**. A name does not permanently belong to one type.

Use `type()` to inspect an object's type:

```python
print(type(42))
print(type(3.14))
print(type("Python"))
print(type(False))
```

You can also use `isinstance()` to check whether an object is an instance of a type:

```python
print(isinstance(21, int))  # True
```

---

## 3. The Big Picture: Built-in Type Categories

| Category | Types | Purpose |
|---|---|---|
| Numeric | `int`, `float`, `complex` | Represent numbers |
| Sequence | `str`, `list`, `tuple`, `range` | Represent ordered sequences |
| Mapping | `dict` | Store key-value associations |
| Set | `set`, `frozenset` | Store distinct elements |
| Boolean | `bool` | Represent truth values |
| Binary | `bytes`, `bytearray`, `memoryview` | Work with binary data |
| None | `NoneType` | Represent the absence of a value |

These categories are a useful way to organize Python's built-in types. They are not all the same kind of classification; for example, `bool` is a subclass of `int` in Python, but it is usually taught separately because it represents truth values.

## 4. Numeric Types

### 4.1 Integers — `int`

An integer is a whole number without a fractional part.

```python
count = 12
temperature_change = -4
zero = 0

print(type(count))  # <class 'int'>
```

Python integers can represent very large values, limited in practice by available memory rather than a fixed 32-bit or 64-bit range.

### 4.2 Floating-point numbers — `float`

A `float` represents a number using floating-point arithmetic. It is commonly used for values with fractional parts.

```python
price = 19.99
scientific_value = 2.5e3

print(price)
print(scientific_value)
```

Output:

```text
19.99
2500.0
```

Most decimal fractions cannot be represented exactly in binary floating-point. That is why:

```python
print(0.1 + 0.2)
```

may produce `0.30000000000000004`. For financial calculations that require exact decimal arithmetic, Python's `decimal` module may be more appropriate.

### 4.3 Complex numbers — `complex`

A complex number has a real part and an imaginary part. Python uses `j` for the imaginary unit.

```python
number = 3 + 4j

print(number.real)
print(number.imag)
print(type(number))
```

Output:

```text
3.0
4.0
<class 'complex'>
```

Complex numbers are useful in mathematics, engineering, and signal processing.

---

## 5. Sequence Types

Sequences preserve an order and commonly support indexing and slicing.

### 5.1 Strings — `str`

A string represents text.

```python
language = "Python"

print(language[0])
print(language[-1])
print(language[0:3])
```

Output:

```text
P
n
Pyt
```

- Indexing accesses an individual character.
- Positive indexing starts at `0`.
- Negative indexing counts from the end; `-1` means the last character.
- Slicing extracts part of a sequence, excluding the ending index.

Strings are **immutable**: characters cannot be changed in place.

```python
language[0] = "J"  # Raises TypeError
```

### 5.2 Lists — `list`

A list is an ordered, mutable collection. It can hold values of different types.

```python
student = ["Jatin", 21, True]
student.append("Python")

print(student)
```

Output:

```text
['Jatin', 21, True, 'Python']
```

Lists are useful when a collection needs to grow, shrink, or change.

### 5.3 Tuples — `tuple`

A tuple is an ordered, immutable sequence.

```python
coordinates = (28.6, 77.2)
print(coordinates[0])
```

Output:

```text
28.6
```

A one-element tuple requires a trailing comma:

```python
single_item = (5,)
```

Without the comma, `(5)` is just the integer `5` in parentheses.

### 5.4 Ranges — `range`

A `range` represents a sequence of integers, often used in loops. It represents the sequence compactly rather than storing each number as a separate item.

```python
for number in range(1, 5):
    print(number)
```

Output:

```text
1
2
3
4
```

The stop value is excluded. `range(1, 5)` produces `1`, `2`, `3`, and `4`.

```python
print(list(range(5)))
```

Output:

```text
[0, 1, 2, 3, 4]
```

---

## 6. Mapping Type: Dictionaries

### Dictionaries — `dict`

A dictionary stores associations between **keys and values**. Use a key to look up its corresponding value.

```python
student = {
    "name": "Jatin",
    "age": 21,
    "is_learning": True,
}

print(student["name"])
print(student["age"])
```

Output:

```text
Jatin
21
```

Dictionaries are mutable:

```python
student["age"] = 22
student["language"] = "Python"
```

They are useful for structured records such as user profiles, settings, or product information. Dictionaries preserve insertion order in modern Python. Keys must be hashable: strings and integers are common choices, while lists cannot be dictionary keys.

---

## 7. Set Types

Sets hold distinct elements and are useful when uniqueness matters.

### 7.1 Sets — `set`

A regular set is mutable and does not keep duplicate elements.

```python
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)
```

The set contains only `1`, `2`, and `3`. Do not rely on the display order of set elements.

```python
numbers.add(4)
numbers.discard(2)
```

Use `set()` to create an empty set. The expression `{}` creates an empty dictionary.

### 7.2 Frozen sets — `frozenset`

A `frozenset` is an immutable version of a set.

```python
fixed_numbers = frozenset({1, 2, 3})
print(2 in fixed_numbers)  # True
```

Its elements cannot be added or removed after creation. A `frozenset` can be used as a dictionary key if its elements satisfy the hashability requirements.

---

## 8. Boolean Type: `bool`

A Boolean represents one of two truth values: `True` or `False`. The first letter must be capitalized.

```python
is_logged_in = True
has_permission = False
```

Booleans are commonly used in conditions:

```python
age = 21

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Python also has **truthiness**: values such as `False`, `None`, numeric zero, and empty built-in collections behave as false in a condition. Many other values behave as true.

```python
print(bool(0))        # False
print(bool(1))        # True
print(bool(""))       # False
print(bool("Python")) # True
```

A Boolean is not the same as a string containing the same word:

```python
print(type(True))    # <class 'bool'>
print(type("True"))  # <class 'str'>
```

---

## 9. Binary Types

Binary types are useful for working with raw byte data, such as file contents or data received over a network.

### 9.1 Bytes — `bytes`

A `bytes` object is an immutable sequence of byte values.

```python
data = b"ABC"

print(data)
print(data[0])
```

Output:

```text
b'ABC'
65
```

Each byte is an integer from `0` to `255`. Here, `65` is the byte value for `A` in ASCII and UTF-8. Bytes represent byte values, not text characters in the same way a string does.

### 9.2 Byte arrays — `bytearray`

A `bytearray` is a mutable sequence of bytes.

```python
data = bytearray(b"ABC")
data[0] = 90

print(data)
```

Output:

```text
bytearray(b'ZBC')
```

### 9.3 Memory views — `memoryview`

A `memoryview` provides a view into the binary data of an object that supports Python's buffer protocol. It can provide access to data without copying the entire buffer.

```python
data = bytearray(b"ABC")
view = memoryview(data)

print(view[0])  # 65
```

This is a more specialized tool, useful for binary processing and performance-sensitive operations.

---

## 10. The None Type: `NoneType`

`None` is a special value commonly used to represent the absence of a value or a meaningful result.

```python
result = None

print(result)
print(type(result))
```

Output:

```text
None
<class 'NoneType'>
```

A function that does not explicitly return a value returns `None`:

```python
def greet():
    print("Hello")

result = greet()
print(result)
```

Output:

```text
Hello
None
```

Use `is None` to check for it:

```python
if result is None:
    print("There is no result.")
```

`None` is different from `0`, `False`, and an empty string.

---

## 11. Mutable vs. Immutable Types

Mutability describes whether an object can be changed in place. It is separate from the category of a data type.

| Common mutable types | Common immutable types |
|---|---|
| `list` | `int` |
| `dict` | `float` |
| `set` | `complex` |
| `bytearray` | `bool` |
| Many user-defined objects | `str` |
|  | `tuple` |
|  | `range` |
|  | `frozenset` |
|  | `bytes` |

For example, both `list` and `tuple` are sequence types, but lists are mutable and tuples are immutable. An immutable container can still contain a reference to a mutable object, such as a tuple containing a list.

For a deeper explanation, see the companion notes: [`immutable_mutable.md`](immutable_mutable.md).

---

## 12. Type Conversion

Python provides functions such as `int()`, `float()`, `str()`, `bool()`, `list()`, and `tuple()` to convert values between types.

```python
print(int("42"))
print(float("3.5"))
print(str(100))
print(list("cat"))
```

Output:

```text
42
3.5
100
['c', 'a', 't']
```

Not every conversion is valid:

```python
int("hello")  # Raises ValueError
```

Also, `int()` applied to a float truncates the fractional part toward zero; it does not round to the nearest integer.

```python
print(int(3.9))   # 3
print(int(-3.9))  # -3
```

---

## 13. A Practical Example

A dictionary can combine different data types into one record:

```python
student = {
    "name": "Jatin",              # str
    "age": 21,                    # int
    "average": 87.5,              # float
    "is_enrolled": True,          # bool
    "subjects": ["Python", "CS"], # list
    "graduation_year": None,      # NoneType
}
```

Each value type suits a different purpose: text for a name, an integer for age, a float for an average, a Boolean for a yes/no state, a list for subjects, and `None` for a value that is not currently set.

---

## 14. Quick Reference

| Type | Example | Mutable? | Typical use |
|---|---|---:|---|
| `int` | `42` | No | Whole numbers |
| `float` | `3.14` | No | Approximate decimal calculations |
| `complex` | `2 + 3j` | No | Complex-number mathematics |
| `str` | `"Python"` | No | Text |
| `list` | `[1, 2, 3]` | Yes | Changeable ordered collection |
| `tuple` | `(1, 2, 3)` | No | Ordered collection |
| `range` | `range(5)` | No | Integer sequences |
| `dict` | `{"a": 1}` | Yes | Key-value associations |
| `set` | `{1, 2, 3}` | Yes | Unique elements |
| `frozenset` | `frozenset({1, 2})` | No | Immutable set |
| `bool` | `True` | No | Truth values |
| `bytes` | `b"ABC"` | No | Immutable binary data |
| `bytearray` | `bytearray(b"ABC")` | Yes | Mutable binary data |
| `memoryview` | `memoryview(b"ABC")` | Depends on underlying buffer | View into buffer data |
| `NoneType` | `None` | No | Absent value |

---

## 15. Practice Questions

Try predicting the output before running the code.

### Question 1: Identify the types

```python
values = [10, 10.5, 2 + 3j, "hello", True, None]

for value in values:
    print(type(value))
```

### Question 2: Sequence behavior

```python
word = "Python"
numbers = [1, 2, 3]

print(word[0])
print(word[1:4])
numbers.append(4)
print(numbers)
```

### Question 3: Unique values

```python
items = {1, 1, 2, 3, 3}
print(len(items))
```

Why is the output smaller than the number of values written in the literal?

### Question 4: Conversion

```python
value = "12"
print(value + "3")
print(int(value) + 3)
```

Why are the results different?

### Question 5: Mutable or immutable?

Classify each type: `list`, `tuple`, `dict`, `str`, `set`, `bytes`.

### Answers

1. `int`, `float`, `complex`, `str`, `bool`, and `NoneType`.
2. `P`, `yth`, and `[1, 2, 3, 4]`.
3. `3`, because a set keeps only distinct elements.
4. The first expression joins strings and produces `"123"`. The second converts `"12"` to an integer and produces `15`.
5. Mutable: `list`, `dict`, `set`. Immutable: `tuple`, `str`, `bytes`.

---

## Key Takeaway

Python has different data types because different kinds of information need different behaviors. Numbers support arithmetic, strings represent text, sequences preserve order, dictionaries associate keys with values, sets represent unique elements, Booleans represent truth values, binary types work with bytes, and `None` represents an absent value.

When learning any type, ask:

1. What kind of information does it represent?
2. How do I create and inspect it?
3. What operations does it support?
4. Is it mutable or immutable?

Those questions are more useful than memorizing names alone.

By. Jatin Kumar Mehta | **End of Document** | https://github.com/jkmloom/py-recap
