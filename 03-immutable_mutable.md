# Mutable and Immutable Objects in Python

> Revision notes on how Python objects behave when we try to change them.

**Lecture:** [Immutable and Mutable in Python](https://youtu.be/MDZ4y-GgZ8k?si=Un6nt-stXt01GUKw)

---

## 1. The Core Idea

In Python, **mutability** describes whether an object can be changed after it has been created.

- A **mutable object** can have its contents changed in place.
- An **immutable object** cannot have its value changed after it has been created.

The important word here is *object*. A variable is a name that refers to an object. Changing which object a variable refers to is not the same thing as changing the object itself.

## 2. Mutable Objects

A mutable object can be changed without replacing the object itself.

Lists are a common example:

```python
letters = ["a", "b", "c"]
letters[1] = "x"
print(letters)
```

Output:

```text
['a', 'x', 'c']
```

The existing list has been modified. Other common mutable built-in types include `list`, `dict`, and `set`. Instances of many user-defined classes are mutable by default, too, although a class can be designed to restrict changes.

### Changing a list's contents

Lists provide methods such as `.append()` to modify the existing list:

```python
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)
```

Output:

```text
[1, 2, 3, 4]
```

## 3. Immutable Objects

An immutable object cannot be changed in place after it has been created. If we perform an operation that appears to change its value, Python instead produces or uses another object and makes the relevant variable refer to it.

Common immutable built-in types include:

- `int` — integers
- `float` — floating-point numbers
- `bool` — Boolean values (`True` and `False`)
- `str` — strings
- `tuple` — tuples
- `frozenset` — immutable sets
- `bytes` — immutable byte sequences
- `NoneType` — the type of `None`

### Example: Integers

```python
x = 5
x = x + 1
print(x)
```

Output:

```text
6
```

Integers are immutable. The expression `x + 1` produces the integer value `6`, and the assignment makes `x` refer to that value. The original integer object representing `5` was not modified.

### Example: Strings

Strings are immutable, so we cannot replace one character in an existing string by assigning to an index:

```python
name = "Loom"
name[0] = "B"  # Raises TypeError
```

If we want a changed string, we create a new one:

```python
name = "Loom"
name = "B" + name[1:]
print(name)
```

Output:

```text
Boom
```

The original string was not altered. A new string was constructed, and `name` was reassigned to refer to it.

### Example: Tuples

Tuples are immutable sequences:

```python
point = (10, 20)
point[0] = 99  # Raises TypeError
```

We cannot replace a tuple's element, add an element to the tuple, or remove one from it in place. If we need a tuple with different contents, we can construct another tuple and assign it to a variable.

## 4. Modification vs. Reassignment

This is one of the most useful distinctions to remember.

### Reassignment

Reassignment changes which object a variable refers to:

```python
x = 10
x = 20
print(x)
```

Output:

```text
20
```

The variable `x` now refers to the value `20`. The integer object representing `10` was not modified.

### Modification

Modification changes the contents of an existing mutable object:

```python
items = [10, 20]
items.append(30)
print(items)
```

Output:

```text
[10, 20, 30]
```

The list was modified in place.

**Remember:** Reassignment changes a variable's reference; mutation changes an existing mutable object.

## 5. Understanding `id()`

Python's built-in `id()` function returns an object's identity as an integer. An object's identity remains stable throughout that object's lifetime. In CPython, an object's identity is commonly related to its memory address, but Python code should not rely on `id()` being a literal memory address across all implementations.

```python
number = 100
print(id(number))

number = number + 1
print(id(number))
```

The two identity values may differ because the assignment makes `number` refer to the result of the addition rather than modifying the original integer object.

Compare that with a list:

```python
numbers = [1, 2, 3]
print(id(numbers))

numbers.append(4)
print(id(numbers))
print(numbers)
```

The list's identity remains the same because `.append()` changes the existing list in place.

> **Note:** Do not use `id()` as a universal test for mutability. The important distinction is whether the object's contents can be changed, not whether a printed identity happens to change between two expressions. Python implementations may also reuse identity values after an object is no longer alive.

## 6. One Object, Multiple Variables

Two variables can refer to the same mutable object. This is sometimes called *aliasing*.

```python
first = [1, 2, 3]
second = first
first.append(4)

print(first)
print(second)
```

Output:

```text
[1, 2, 3, 4]
[1, 2, 3, 4]
```

Both names refer to the same list. When the list is changed through `first`, the change is visible through `second` as well. Assigning one list variable to another does **not** automatically create a copy.

Compare that with reassignment of an integer:

```python
first = 10
second = first
first = 20

print(first)
print(second)
```

Output:

```text
20
10
```

`first` and `second` initially refer to the integer value `10`. Reassigning `first` does not change `second`; it only makes `first` refer to `20`.

## 7. Mutable and Immutable Types at a Glance

| Type | Mutable? | Example |
|---|---|---|
| `int` | No | `42` |
| `float` | No | `3.14` |
| `bool` | No | `True` |
| `str` | No | `"Python"` |
| `tuple` | No | `(1, 2, 3)` |
| `frozenset` | No | `frozenset({1, 2})` |
| `bytes` | No | `b"hello"` |
| `list` | Yes | `[1, 2, 3]` |
| `dict` | Yes | `{"name": "Ada"}` |
| `set` | Yes | `{1, 2, 3}` |

These are the usual mutability characteristics of Python's built-in types. For custom classes, mutability depends on how the class is designed.

## 8. A Subtle Case: A Tuple Containing a List

A tuple is immutable, but it can contain a reference to a mutable object, such as a list.

```python
data = ([1, 2], "hello")
data[0].append(3)
print(data)
```

Output:

```text
([1, 2, 3], 'hello')
```

Why does this work?

- The tuple's elements cannot be replaced.
- The first element refers to a list.
- The list itself is mutable, so its contents can change.

We cannot assign a different object to `data[0]`, but we can mutate the list that `data[0]` refers to.

```python
data[0] = [9, 9]  # Raises TypeError
```

This is sometimes described as **non-transitive immutability**: the tuple is immutable, but objects referenced by it are not automatically immutable.

## 9. Why This Matters

Understanding mutability helps prevent bugs and makes it easier to reason about how data changes in a program.

1. **Know your data types.** Lists, dictionaries, and sets are mutable; integers, strings, and tuples are immutable.
2. **Distinguish mutation from reassignment.** They are different operations with different consequences.
3. **Watch shared references.** Multiple variables can refer to the same mutable object.
4. **Do not assume assignment makes a copy.** `second = first` makes another name refer to the same object.
5. **Remember nested objects.** An immutable container can hold a mutable object.

## 10. Quick Revision

- **Mutable:** An object's contents can be changed after creation.
- **Immutable:** An object's value cannot be changed after creation.
- **List:** Mutable; its elements can be replaced, added, or removed.
- **String:** Immutable; operations that produce a changed string create a new string value.
- **Tuple:** Immutable as a container; it cannot have its elements reassigned.
- **Reassignment:** Makes a variable refer to another object.
- **Mutation:** Changes an existing mutable object.
- **`id()`:** Returns an object's identity; in CPython this is commonly associated with its memory address.
- **Aliasing:** Multiple variables refer to the same object.
- **Nested mutability:** An immutable container may contain a mutable object whose contents can still change.

### The one thing to remember

**A variable is a name, and an object is the value it refers to. Mutability describes whether that object can be changed in place.**

---

## Practice Questions

Try answering these without running the code first.

### 1. What will this print?

```python
x = 7
y = x
x = 12
print(x, y)
```

### 2. What will this print?

```python
a = [1, 2]
b = a
a.append(3)
print(a)
print(b)
```

### 3. Why does this raise an error?

```python
word = "cat"
word[0] = "b"
```

### 4. What will this print, and why?

```python
container = ([1, 2],)
container[0].append(3)
print(container)
```

### Answers

1. `12 7` — `x` is reassigned; `y` still refers to `7`.
2. Both print `[1, 2, 3]` — `a` and `b` refer to the same list.
3. Strings are immutable, so an individual character cannot be reassigned.
4. `([1, 2, 3],)` — the tuple is immutable, but the list it contains is mutable.

---

By. Jatin Kumar Mehta | **End of Document** | https://github.com/jkmloom/py-recap
