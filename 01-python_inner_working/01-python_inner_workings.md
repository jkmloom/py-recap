# Python's Inner Workings: From Source Code to Execution

## Overview

When you run a Python program, Python does more than simply read each line and send it directly to the computer's processor. In the standard **CPython** implementation, source code typically passes through a compilation stage and then a runtime execution stage.

A simplified view is:

```text
loom.py (Python source code)
        |
        v
Python compiler
        |
        v
Bytecode (Python-specific instructions)
        |
        v
Python Virtual Machine (PVM)
        |
        v
Program behavior and output
```

This diagram is a useful mental model. Some implementation details vary depending on the Python implementation, Python version, and how the code is run.

> **Key idea:** Python bytecode is not the same as native machine code. In CPython, the Python Virtual Machine executes Python bytecode.

---

## 1. Step One: Compile Python Source Code to Bytecode

Suppose you write a Python program in a file named `loom.py`:

```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Ada"))
```

The file contains **source code**: the human-readable instructions you wrote in Python.

Before CPython can execute the program, it compiles the source code into an internal representation called **bytecode**.

### What is bytecode?

Bytecode is a lower-level set of instructions designed for a particular runtime or virtual machine. CPython bytecode represents operations such as loading values, calling functions, performing calculations, and returning results.

It is lower-level than Python source code, but it is still **Python-specific**. It is not a set of instructions that a physical CPU can normally execute directly.

You can inspect bytecode using Python's built-in `dis` module:

```python
import dis

def add(a, b):
    return a + b

dis.dis(add)
```

The exact output depends on the Python version. The important point is that `dis` displays the low-level instructions CPython uses for the function.

### Is bytecode platform-independent?

CPython bytecode is often described as platform-independent because it is not native machine code for a particular processor. However, this description needs a qualification:

- Bytecode is specific to the Python implementation and its bytecode format.
- The format and instructions can change between Python versions.
- A `.pyc` file created by one CPython version may not be usable by another version.
- Other Python implementations may use different internal representations or execution strategies.

Therefore, do not assume that a bytecode file is universally portable across Python versions or implementations.

---

## 2. Step Two: Bytecode and `.pyc` Files

### What is a `.pyc` file?

A `.pyc` file stores compiled Python bytecode along with metadata used by Python to determine whether the cached compilation is suitable for reuse.

For example:

```text
loom.py
__pycache__/
    loom.cpython-314.pyc
```

The `.pyc` file is a **bytecode cache**. When Python imports a module, it may save the compiled bytecode so it can avoid recompiling the source on a later import, provided the cache is valid.

This can reduce the work required to load imported modules. It does not mean that every Python program will run faster simply because a `.pyc` file exists.

### What is `__pycache__`?

`__pycache__` is a directory Python commonly uses to store cached bytecode files for imported modules.

It helps organize cache files that may differ by interpreter implementation or Python version. For example, a directory could contain:

```text
project/
├── loom.py
├── main.py
└── __pycache__/
    ├── loom.cpython-314.pyc
    └── loom.cpython-313.pyc
```

This is an illustrative example: the exact files present depend on which Python versions have imported the module and how Python was configured.

Python can keep separate cache files when different compatible interpreter versions need different bytecode formats. The cache is managed by Python; in normal development, you generally do not need to edit these files yourself.

### Breaking down `loom.cpython-314.pyc`

Consider this filename:

```text
loom.cpython-314.pyc
```

Its parts are:

| Part | Meaning |
|---|---|
| `loom` | The source module's name |
| `cpython` | The Python implementation |
| `314` | The Python version tag, corresponding to Python 3.14 |
| `.pyc` | A compiled-bytecode cache file |

The general pattern is often similar to:

```text
module_name.implementation-version.pyc
```

The exact cache tag and filename depend on the implementation and version. The filename is not a universal format for every Python implementation.

### Are `.pyc` files created for every Python file?

Not necessarily. A common distinction is between **imported modules** and a **top-level script**.

- **Imported module:** When a module such as `loom.py` is imported, Python will commonly cache its compiled bytecode in `__pycache__`, if bytecode caching is enabled and the cache is usable.
- **Top-level script:** When you run a file directly, such as `python loom.py`, Python compiles and executes it, but does not ordinarily create a `__pycache__/loom...pyc` file for that top-level script just because it was run.

There are exceptions and additional details depending on how code is loaded or compiled, but this distinction is a good starting point.

### When does Python reuse a `.pyc` file?

When importing a module, Python checks whether an existing bytecode cache is suitable. The cache includes information that helps Python determine whether the source has changed or whether the cache is otherwise appropriate.

Depending on the cache mode, validation can use source metadata such as modification time and file size, or a hash of the source. If the cache is missing, invalid, or incompatible, Python can compile the source again and may update the cache.

**Important:** `.pyc` files are implementation-managed cache files, not frozen standalone executables. They usually rely on a compatible Python runtime and do not generally contain everything needed to run a program independently.

---

## 3. Step Three: The Python Virtual Machine (PVM)

### What is the Python Virtual Machine?

The **Python Virtual Machine (PVM)** is a conceptual name for the runtime machinery that executes Python bytecode in CPython.

A simplified way to think about it is that the runtime repeatedly fetches and carries out bytecode instructions while the program runs. In practice, the implementation is more complex than a single simple loop, and details vary across Python versions.

The PVM is part of the execution environment. It is not a separate physical computer or a virtual machine that you normally need to install independently.

### Is the PVM the same as the Python interpreter?

In beginner explanations, the PVM is often described as the part of the Python interpreter that executes bytecode. The phrase **Python interpreter** can also refer more broadly to the whole implementation that parses, compiles, and executes Python code.

For clarity:

- **Python language:** The rules and syntax used to write Python programs.
- **Python implementation/interpreter:** Software that implements the language and runs Python programs.
- **Compiler:** The part that translates source code into an internal form, such as CPython bytecode.
- **PVM/runtime execution machinery:** The part that executes bytecode.
- **CPU:** The physical processor that executes native machine instructions, including those used to run the Python implementation itself.

### Why can't the CPU execute Python bytecode directly?

A CPU executes machine instructions defined by its processor architecture, such as x86-64 or ARM64.

CPython bytecode is a different instruction format. Its instructions are designed for CPython's runtime, not directly for the processor. CPython's native implementation executes the runtime machinery that interprets those bytecode instructions and performs the requested operations.

For example, the bytecode for an addition operation does not mean the CPU directly understands a special “Python add” instruction. Instead, CPython's runtime handles that operation, including Python-specific behavior such as object types and operator methods.

> **Remember:** Python bytecode is not native machine code. The CPU runs the native instructions of the Python implementation; CPython's runtime uses those instructions to execute Python bytecode.

### Does the PVM run in a continuous loop?

A common teaching model describes the PVM as a loop that repeatedly processes bytecode instructions. This is helpful as a conceptual introduction, but it is simplified. Actual execution involves runtime data structures, function calls, object operations, exception handling, and other mechanisms. The exact implementation changes over time.

---

## 4. CPython and Other Python Implementations

Python is a language specification and ecosystem, not just one particular executable. Different implementations can run Python code using different internal techniques.

Common implementations include:

| Implementation | General description |
|---|---|
| **CPython** | The standard and most widely used implementation; written primarily in C. |
| **PyPy** | An alternative implementation known for its just-in-time (JIT) compilation capabilities. |
| **Jython** | An implementation designed to run Python on the Java platform and interoperate with Java. |
| **IronPython** | An implementation designed for the .NET ecosystem. |
| **Stackless Python** | A Python implementation or variant focused on lightweight task scheduling and related execution features. |

These implementations are not simply interchangeable versions of the same internal engine. They may differ in performance, supported versions, compatibility, and execution details.

### Which implementation do most people use?

Most people who install Python from the official Python website use **CPython**. It is also the implementation most commonly assumed when discussing `.pyc` files, `__pycache__`, and CPython bytecode.

The details in this guide about bytecode caching and filenames such as `loom.cpython-314.pyc` specifically describe common CPython behavior, not a universal rule for every Python implementation.

---

## 5. Putting It All Together

Imagine running a program named `main.py` that imports a module named `loom.py`.

```python
# loom.py
def greet(name):
    return f"Hello, {name}!"
```

```python
# main.py
import loom

print(loom.greet("Ada"))
```

A simplified sequence is:

1. You ask Python to run `main.py`.
2. CPython reads and compiles the top-level script so it can execute it.
3. The script imports `loom`.
4. Python locates `loom.py` and checks whether a suitable cached bytecode file is available.
5. If the cache is valid, Python can load the cached bytecode; otherwise, it compiles the module and may write a new `.pyc` cache file.
6. CPython executes the relevant bytecode using its runtime machinery.
7. The program prints:

```text
Hello, Ada!
```

This example illustrates why a top-level script and an imported module can behave differently with respect to bytecode caching.

---

## 6. Common Misunderstandings

### “Python directly executes the source code line by line.”

That is an oversimplification for CPython. CPython generally compiles source code into bytecode before executing it. The exact steps depend on how the code is run and the implementation being used.

### “Bytecode is machine code.”

No. CPython bytecode is designed for the CPython runtime. Native machine code is the instruction set executed directly by the CPU.

### “Every `.py` file gets a `.pyc` file.”

No. Python commonly caches bytecode for imported modules, but running a file directly as the top-level script does not ordinarily create a cache file for that script.

### “A `.pyc` file is a frozen executable.”

Not in the usual standalone-program sense. It stores cached compiled bytecode and metadata, and generally requires a compatible Python implementation to execute it.

### “Bytecode works on every Python version.”

No. Bytecode formats can change between versions and implementations. A cache file should be treated as an internal artifact for a compatible runtime, not as a universal distribution format.

### “The PVM is a physical machine.”

No. It is a conceptual term for runtime machinery that executes bytecode.

---

## 7. Quick Summary

| Term | Simple explanation |
|---|---|
| `.py` file | Human-readable Python source code |
| Compiler | Translates source code into an internal representation |
| Bytecode | Python-runtime instructions produced by compilation |
| `.pyc` file | A cache file containing compiled bytecode and related metadata |
| `__pycache__` | A directory commonly used to store bytecode caches for imported modules |
| PVM | The runtime machinery that executes Python bytecode |
| CPU | The physical processor that executes native machine instructions |
| CPython | The standard, widely used Python implementation |

The central flow is:

```text
Python source (.py)
        |
        v
Compilation
        |
        v
Python bytecode
        |
        v
CPython runtime / PVM
        |
        v
Program executes
```

Keep in mind that this is a simplified model of CPython. Other Python implementations may use different internal strategies.

---

## Further Reading

- [Python documentation](https://docs.python.org/3/)
- [The `dis` module — disassembler for Python bytecode](https://docs.python.org/3/library/dis.html)
- [The `py_compile` module](https://docs.python.org/3/library/py_compile.html)
- [The `compileall` module](https://docs.python.org/3/library/compileall.html)
- [Python glossary](https://docs.python.org/3/glossary.html)

By. Jatin Kumar Mehta | **End of Document** | https://github.com/jkmloom/py-recap