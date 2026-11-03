# Python Internals: Copy, Reference Counts, and Slicing

> Revision notes on how Python names refer to objects, how copying works, how CPython tracks references, and what slicing actually creates.

---

## 1. Start With the Right Mental Model: Names and Objects

A common beginner mistake is to imagine that a variable is a box that physically contains a value. A more useful mental model for Python is:

- An **object** exists and holds data.
- A **name** refers to an object.
- Multiple names can refer to the same object.

Consider:

```python
a = [10, 20, 30]
b = a
```

This does not create two separate lists. It creates one list object and makes both `a` and `b` refer to it.

```text
a ─────┐
       ├────> [10, 20, 30]
b ─────┘
```

We can demonstrate this by modifying the list:

```python
a = [10, 20, 30]
b = a

a.append(40)

print(a)
print(b)
```

Output:

```text
[10, 20, 30, 40]
[10, 20, 30, 40]
```

Both names show the change because they refer to the same mutable list.

**Important:** `b = a` is assignment, not copying. It creates another reference to the same object.

## 2. Object Identity: `is` vs. Equality: `==`

Python provides two different ways to compare objects.

### `==` checks equality

`==` asks whether two objects have equal values according to their equality implementation.

```python
first = [1, 2, 3]
second = [1, 2, 3]

print(first == second)
```

Output: `True`

The lists contain equal values in the same order.

### `is` checks identity

`is` asks whether two references point to the very same object.

```python
first = [1, 2, 3]
second = [1, 2, 3]

print(first is second)
```

Output: `False`

Although the lists have equal contents, they are two distinct list objects.

Now compare this with assignment:

```python
first = [1, 2, 3]
second = first

print(first == second)
print(first is second)
```

Output:

```text
True
True
```

| Operator | What it checks |
|---|---|
| `==` | Whether values are equal |
| `is` | Whether both references identify the same object |

Use `is` for identity checks, especially for singleton values such as `None`:

```python
result = None
if result is None:
    print("No result")
```

Do not use `is` as a replacement for `==` when comparing ordinary values.

## 3. What Does Copying Mean?

Copying means creating another object based on an existing object. The exact behavior depends on the kind of copy.

Python commonly distinguishes between:

1. Assignment (which does not copy an object).
2. Shallow copying.
3. Deep copying.

These distinctions matter most when working with mutable objects such as lists and dictionaries.

## 4. Assignment Is Not a Copy

```python
original = [1, 2, 3]
alias = original

alias.append(4)
print(original)
```

Output: `[1, 2, 3, 4]`

The two names refer to the same list. This behavior is called **aliasing**: multiple names refer to one object. If you need an independent list, explicitly make a copy.

## 5. Shallow Copy

A **shallow copy** creates a new outer object, but does not recursively copy the objects stored inside it. The new collection contains references to the same inner objects.

For a flat list:

```python
original = [10, 20, 30]
copied = original.copy()

print(original == copied)  # True
print(original is copied)  # False
```

The two lists have equal contents but are distinct list objects.

Changing the outer list does not change the other outer list:

```python
original = [10, 20, 30]
copied = original.copy()
copied.append(40)

print(original)  # [10, 20, 30]
print(copied)    # [10, 20, 30, 40]
```

The `.copy()` method makes a shallow copy of a list. You can also use the `copy` module:

```python
import copy

original = [10, 20, 30]
copied = copy.copy(original)
```

### The important catch: nested mutable objects

A shallow copy only copies the outer container. Inner objects are still shared.

```python
original = [[1, 2], [3, 4]]
copied = original.copy()

print(original is copied)       # False
print(original[0] is copied[0]) # True
```

The outer lists are different, but their first inner list is the same object.

```python
original = [[1, 2], [3, 4]]
copied = original.copy()
copied[0].append(99)

print(original)
print(copied)
```

Both print:

```text
[[1, 2, 99], [3, 4]]
```

Both outer lists appear to change because they refer to the same inner list. However, adding a new item to the copied outer list affects only that outer list.

**Remember:** A shallow copy creates a new outer container, but keeps references to the original inner objects.

## 6. Deep Copy

A **deep copy** recursively copies objects contained within the original object, subject to Python's copy protocol and special handling for certain objects.

Use `copy.deepcopy()`:

```python
import copy

original = [[1, 2], [3, 4]]
copied = copy.deepcopy(original)

print(original is copied)       # False
print(original[0] is copied[0]) # False
```

Both the outer list and its nested lists are separate objects.

```python
original = [[1, 2], [3, 4]]
copied = copy.deepcopy(original)
copied[0].append(99)

print(original)  # [[1, 2], [3, 4]]
print(copied)    # [[1, 2, 99], [3, 4]]
```

### Shallow copy vs. deep copy

| Behavior | Shallow copy | Deep copy |
|---|---|---|
| Creates a new outer object | Yes | Yes |
| Copies nested objects recursively | No | Generally, yes |
| Shares references to nested objects | Yes | Generally, no |
| Typical tool | `copy.copy()` or `.copy()` | `copy.deepcopy()` |

Deep copying is not always necessary or appropriate. It can be more expensive, and some objects have custom copying behavior or cannot be copied in the ordinary way. Choose based on whether nested objects should be shared.

## 7. Reference Counts

Python objects need to remain alive while they are still being used. In **CPython**, one important memory-management mechanism is reference counting.

A reference is a way for a name, container, or another part of a program to refer to an object.

At a conceptual level:

- When a new reference to an object is created, its reference count increases.
- When a reference is removed, its reference count decreases.
- When an object's reference count reaches zero, CPython can release that object's memory.

Inspect a reference count with `sys.getrefcount()`:

```python
import sys

items = [1, 2, 3]
print(sys.getrefcount(items))
```

`sys.getrefcount()` reports the reference count in CPython. The number can be higher than expected because passing the object to `getrefcount()` temporarily creates another reference. Exact counts can vary with Python version and execution environment.

### Adding another reference

```python
import sys

items = [1, 2, 3]
print(sys.getrefcount(items))

another_name = items
print(sys.getrefcount(items))
```

The second name refers to the same list, so it adds another reference.

### Removing a reference

```python
items = [1, 2, 3]
another_name = items

del another_name
print(items)
```

`del another_name` removes that name. It does not necessarily delete the list object. The name `items` still refers to the list.

**Deleting a name is not the same as forcibly deleting an object.** An object can be reclaimed when it is no longer reachable and the implementation's memory-management rules allow it.

### Reference counting is not the whole garbage collector

Reference counting alone cannot reclaim every unreachable object. Two objects can refer to each other even when nothing outside the pair can reach them. This creates a reference cycle.

CPython also has a cyclic garbage collector that can detect and collect many unreachable reference cycles. Reference counting is a key part of CPython's memory management, not a guarantee that every Python implementation works identically.

## 8. The `del` Statement

The `del` statement removes a reference, such as a variable name or an item from a container. Its effect depends on what is being deleted.

### Deleting a variable name

```python
numbers = [1, 2, 3]
del numbers
```

The name `numbers` is removed from the current namespace. If no other references keep the list alive, it may become eligible for reclamation.

### Deleting a list element

```python
numbers = [10, 20, 30, 40]
del numbers[1]
print(numbers)
```

Output: `[10, 30, 40]`

Here, `del` removes an element from the existing list. The list is mutated.

### Deleting a slice

```python
numbers = [10, 20, 30, 40, 50]
del numbers[1:4]
print(numbers)
```

Output: `[10, 50]`

The selected portion is removed from the original list.

## 9. Slicing

Slicing extracts a portion of a sequence. It is commonly used with strings, lists, and tuples.

General syntax:

```python
sequence[start:stop:step]
```

- `start`: Index where the slice begins (included).
- `stop`: Index where the slice ends (excluded).
- `step`: Interval between selected elements.

### Basic slicing

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])
```

Output: `[20, 30, 40]`

The slice starts at index `1` and stops before index `4`.

### Omitting start or stop

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[:3])
print(numbers[2:])
```

Output:

```text
[10, 20, 30]
[30, 40, 50]
```

### Using a step

```python
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[::2])
```

Output: `[10, 30, 50]`

### Negative indexes and reverse slicing

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[-1])
print(numbers[::-1])
```

Output:

```text
50
[50, 40, 30, 20, 10]
```

A step of `-1` traverses the sequence in reverse.

## 10. Does Slicing Create a Copy?

A list slice creates a **new list object**, but it is a **shallow copy**. The new list contains references to the same elements as the original.

```python
original = [10, 20, 30]
sliced = original[:]

print(original == sliced)  # True
print(original is sliced)  # False
```

The two lists have equal contents but are different outer list objects.

For a flat list, changes to the sliced list's structure do not affect the original:

```python
original = [10, 20, 30]
sliced = original[:]
sliced.append(40)

print(original)  # [10, 20, 30]
print(sliced)    # [10, 20, 30, 40]
```

But nested objects are shared:

```python
original = [[1, 2], [3, 4]]
sliced = original[:]
sliced[0].append(99)

print(original)
print(sliced)
```

Both print:

```text
[[1, 2, 99], [3, 4]]
```

The slice created a new outer list, but both outer lists still refer to the same inner list.

### Slicing other sequence types

- Slicing a `list` produces a new list.
- Slicing a `tuple` produces a tuple.
- Slicing a `str` produces a string.

Strings and tuples are immutable, so their elements cannot be changed in place. For immutable objects, an implementation may reuse an existing object in some cases; do not rely on identity behavior as a general rule.

## 11. Putting the Concepts Together

```python
import copy

original = [[1, 2], [3, 4]]

alias = original
shallow = original.copy()
deep = copy.deepcopy(original)

print(alias is original)
print(shallow is original)
print(deep is original)
print(shallow[0] is original[0])
print(deep[0] is original[0])
```

Expected output:

```text
True
False
False
True
False
```

What does this tell us?

- `alias` refers to the original outer list.
- `shallow` is a new outer list, but shares the inner lists.
- `deep` is a separate outer list with separately copied nested lists.

## 12. Common Misunderstandings

### "`b = a` makes a copy."

No. It makes `b` another name for the same object.

### "If two lists have the same values, they are the same object."

Not necessarily. `==` checks equality; `is` checks identity.

### "A shallow copy duplicates everything."

No. It creates a new outer object but keeps references to nested objects.

### "A deep copy always copies absolutely everything."

Not quite. `deepcopy()` follows Python's copy protocol, handles recursive structures, and may preserve or specially handle some objects. Some objects cannot be meaningfully deep-copied.

### "`del x` destroys the object."

Not necessarily. It removes the name `x`. Other references may still keep the object alive.

### "A slice is just another reference to the original list."

No. A list slice creates a new outer list, but its elements are references to the same objects held by the original list.

### "Reference counting is how every Python implementation works."

No. Reference counting is a key part of CPython's memory management. Other implementations can use different strategies.

## 13. Quick Revision

| Concept | Meaning |
|---|---|
| Name/reference | A name refers to an object |
| Assignment (`b = a`) | Makes `b` refer to the same object as `a` |
| Aliasing | Multiple references point to one object |
| `==` | Compares values for equality |
| `is` | Checks object identity |
| Shallow copy | New outer object; nested references are shared |
| Deep copy | Recursively copies nested objects according to copy behavior |
| Reference count | In CPython, tracks references to an object |
| `del` | Removes a name or an item/reference; does not guarantee immediate destruction |
| Slice (`a[start:stop]`) | Extracts a sequence portion; list slices create a new shallow list |

### The key ideas to remember

1. Variables are names that refer to objects.
2. Assignment does not automatically copy an object.
3. `is` checks identity; `==` checks equality.
4. A shallow copy duplicates the outer container, not its nested objects.
5. A deep copy recursively copies nested objects, subject to the copy protocol.
6. CPython uses reference counting as part of memory management.
7. A list slice creates a new list, but nested objects remain shared.

## 14. Practice Questions

Try predicting the output before running each example.

### Question 1: Assignment and aliasing

```python
a = [1, 2, 3]
b = a
b.append(4)

print(a)
print(b)
print(a is b)
```

### Question 2: Equality vs. identity

```python
a = [1, 2]
b = [1, 2]

print(a == b)
print(a is b)
```

### Question 3: Shallow copy

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.copy(a)
b[0].append(5)

print(a)
print(b)
```

### Question 4: Deep copy

```python
import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0].append(5)

print(a)
print(b)
```

### Question 5: Slicing

```python
numbers = [0, 1, 2, 3, 4, 5]

print(numbers[1:5:2])
print(numbers[::-1])
```

### Question 6: Slice and nested references

```python
a = [[1, 2], [3, 4]]
b = a[:]

b[0].append(9)
b.append([5, 6])

print(a)
print(b)
```

### Answers

1. Both lists print `[1, 2, 3, 4]`; `a is b` is `True`. Both names refer to one list.
2. `True` and `False`. The lists have equal contents but are distinct objects.
3. Both outer lists show `[[1, 2, 5], [3, 4]]`. The inner list is shared.
4. `a` remains `[[1, 2], [3, 4]]`; `b` becomes `[[1, 2, 5], [3, 4]]`. The nested list was copied.
5. `[1, 3]` and `[5, 4, 3, 2, 1, 0]`.
6. `a` is `[[1, 2, 9], [3, 4]]`; `b` is `[[1, 2, 9], [3, 4], [5, 6]]`. The inner list is shared, but appending to the outer copy affects only `b`.

---

By. Jatin Kumar Mehta | **End of Document** | https://github.com/jkmloom/py-recap
