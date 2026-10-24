# Python Shell and IDLE: A Complete Guide for Windows, macOS, and Linux

## 1. Introduction

Python is a high-level, general-purpose programming language used in web development, automation, data analysis, artificial intelligence, scientific computing, and many other fields.

To write and execute Python code, we need a Python interpreter. The interpreter processes Python instructions and executes them.

Two beginner-friendly ways to interact with Python are the **Python Shell** and **IDLE**.

- **Python Shell** allows us to enter Python statements interactively and see their results immediately.
- **IDLE** is a development environment included with many standard Python installations. It provides an interactive Python Shell along with an editor for writing, saving, and executing Python programs.

Although these tools are closely related, they are not exactly the same. The Python Shell is an interactive environment, whereas IDLE is an application that provides a shell and additional programming tools.

Their availability and installation procedures differ slightly across Windows, macOS, and Linux.

## 2. What Is the Python Shell?

The Python Shell is an interactive environment in which users can enter Python statements and execute them one at a time.

It is commonly associated with the term **REPL**, which stands for:

- **R — Read:** Read the instruction entered by the user.
- **E — Evaluate:** Evaluate the instruction.
- **P — Print:** Display the result when appropriate.
- **L — Loop:** Wait for the next instruction and repeat the process.

The Python Shell allows us to experiment with Python without creating a separate source-code file.

### 2.1 How the Python Shell works

When we start Python in interactive mode, we generally see a prompt similar to this:

```
Python 3.x.x (...)
Type "help", "copyright", "credits" or "license" for more information.
>>>

```

The `>>>` symbol is the primary Python prompt. It indicates that the interpreter is ready to accept a statement.

For example:

```
>>> 10 + 20
30

```

The interpreter evaluates the expression `10 + 20` and displays its result, `30`.

Another example:

```
>>> print("Hello, Python!")
Hello, Python!

```

Here, the `print()` function explicitly displays a message.

We can also create variables:

```
>>> name = "Alice"
>>> age = 20
>>> print(name)
Alice
>>> print(age)
20

```

The variables remain available during the current interactive session unless they are changed, deleted, or the session is restarted.

### 2.2 The difference between an expression and a statement

An expression produces a value.

```
>>> 5 * 4
20

```

In the interactive shell, the value of an expression is displayed automatically.

An assignment statement stores a value in a variable.

```
>>> number = 25

```

This assignment normally produces no displayed result. To see the value, enter:

```
>>> number
25

```

This distinction is useful when experimenting with Python interactively.

### 2.3 The primary and continuation prompts

Python uses different prompts to indicate whether it is ready for a new statement or expects more input.

The primary prompt is:

```
>>>

```

The continuation prompt is:

```
...

```

For example:

```
>>> for number in range(3):
...     print(number)
...
0
1
2

```

The continuation prompt appears because the `for` loop requires an indented body and must be completed before execution.

A multiline function works similarly:

```
>>> def greet(name):
...     print("Hello,", name)
...
>>> greet("Sam")
Hello, Sam

```

**Important:** The exact prompts and startup messages can vary slightly between Python versions and interactive environments.

### 2.4 Where can the Python Shell be found?

The Python Shell can be accessed through different interfaces:

1. A terminal or command-line application.
2. The interactive Shell window inside IDLE.
3. Other Python development environments that provide an interactive console.

The underlying Python language remains the same, although the interface and available features may differ.

---

## 3. What Is IDLE?

**IDLE stands for Integrated Development and Learning Environment.**

It is a lightweight development environment designed for writing and experimenting with Python programs. It is developed alongside Python and is commonly distributed with the standard Python installer for Windows and macOS. On many Linux systems, it is provided through a separate package.

IDLE is particularly suitable for beginners because it provides a relatively simple interface without requiring a complex project setup.

### 3.1 Main features of IDLE

IDLE provides several useful features:

**1. Interactive Python Shell**

IDLE includes a Shell window where Python statements can be entered and executed immediately.

**2. Source-code editor**

It provides an editor for writing complete Python programs and saving them as `.py` files.

**3. Syntax highlighting**

Different elements of Python code are displayed in different colors. For example, keywords, strings, comments, and built-in names may receive different colors.

**4. Automatic indentation**

IDLE assists with indentation when writing code blocks, such as functions, loops, and conditional statements.

**5. Program execution**

Python files can be executed from the editor, usually through the Run Module command.

**6. Error reporting**

Syntax errors and runtime exceptions are displayed with information that helps identify where a problem occurred.

**7. Interactive experimentation**

Variables, expressions, functions, and other Python objects can be tested in the Shell without creating a new file for every experiment.

**8. Debugging support**

IDLE provides basic debugging features, including stepping through code and examining execution state.

### 3.2 Why is IDLE useful for beginners?

IDLE reduces the number of tools a beginner needs to learn initially.

A student can:

- Write a Python program in the editor.
- Save it to a file.
- Run it using the Python interpreter.
- Read the output in the Shell.
- Correct errors and execute the program again.

This workflow introduces important programming concepts without requiring an advanced IDE.

### 3.3 Is IDLE a programming language?

No. IDLE is not a programming language.

Python is the programming language, the Python interpreter executes Python code, and IDLE is a development environment that helps users write and execute that code.

A simple way to understand the relationship is:

- **Python:** The language used to express instructions.
- **Python interpreter:** The software that executes Python instructions.
- **Python Shell:** An interactive interface for entering Python instructions.
- **IDLE:** An application that combines an interactive Shell with an editor and other development features.

---

## 4. Python Shell vs. IDLE

The Python Shell and IDLE are related, but their purposes are different.

| Feature                      | Python Shell                                 | IDLE                                       |
| ---------------------------- | -------------------------------------------- | ------------------------------------------ |
| Primary purpose              | Execute Python statements interactively      | Write, edit, and execute Python programs   |
| Interactive execution        | Yes                                          | Yes, through its Shell                     |
| Source-code editor           | Not normally part of a basic terminal shell  | Yes                                        |
| Save programs as `.py` files | Requires a separate editor or another method | Yes                                        |
| Syntax highlighting          | Usually limited in a basic terminal          | Yes, in the editor                         |
| Automatic indentation        | Depends on the interface                     | Available in the editor                    |
| Debugging tools              | Depends on the interface                     | Basic debugging support                    |
| Graphical interface          | Not required                                 | Yes                                        |
| Typical use                  | Testing expressions and short statements     | Learning Python and writing small programs |

### Example: Using the Shell

Suppose we want to calculate the area of a rectangle.

```
>>> length = 10
>>> width = 5
>>> area = length * width
>>> area
50

```

This is convenient for a quick calculation.

### Example: Using IDLE's editor

For a program that should be saved and executed again, write the following code in the editor:

```
length = 10
width = 5

area = length * width

print("Area of rectangle:", area)

```

Save the file as `rectangle.py` and execute it.

The output is:

```
Area of rectangle: 50

```

The first example is useful for experimentation, while the second is more appropriate for a reusable program.

---

## 5. Understanding the Python Shell

### 5.1 Starting a Python Shell

The precise command depends on the operating system and how Python was installed.

Common commands include:

```
```

or:

```
python3

```

On Windows, another common command is:

```
py

```

These commands start Python interactively when they successfully locate an appropriate Python installation.

The commands are entered into the operating system's terminal or command-line application, not at the Python `>>>` prompt.

### 5.2 Performing calculations

Python can be used as a calculator.

```
>>> 10 + 5
15
>>> 10 - 5
5
>>> 10 * 5
50
>>> 10 / 5
2.0
>>> 10 // 3
3
>>> 10 % 3
1
>>> 2 ** 3
8

```

These operators represent:

- `+`: Addition
- `-`: Subtraction
- `*`: Multiplication
- `/`: Division
- `//`: Floor division
- `%`: Modulo or remainder
- `**`: Exponentiation

Notice that ordinary division returns a floating-point result, so `10 / 5` produces `2.0`.

### 5.3 Working with variables

A variable is a name that refers to a value.

```
>>> student = "Riya"
>>> marks = 92
>>> passed = True
>>> student
'Riya'
>>> marks
92
>>> passed
True

```

Python supports several built-in data types, including:

- `int`: Integers
- `float`: Floating-point numbers
- `str`: Strings
- `bool`: Boolean values
- `list`: Lists
- `tuple`: Tuples
- `dict`: Dictionaries
- `set`: Sets

We can inspect a value's type using `type()`:

```
>>> type(92)
<class 'int'>
>>> type(3.14)
<class 'float'>
>>> type("Python")
<class 'str'>

```

### 5.4 Defining functions

The Shell can be used to define and test functions.

```
>>> def square(number):
...     return number * number
...
>>> square(6)
36

```

The function remains available in the current session until it is replaced, deleted, or the session ends.

### 5.5 Limitations of interactive execution

The Shell is excellent for small experiments, but it is less convenient for large programs.

For example:

- Re-entering a long program is tedious.
- Code is not automatically saved as a source file.
- Organizing a project with multiple files is difficult.
- Starting a fresh session generally removes variables and functions defined only in the previous session.

For these reasons, interactive execution is often combined with a source-code editor.

---

## 6. Understanding the IDLE Interface

When IDLE starts, it usually opens a window named Python Shell.

The main components are as follows.

### 6.1 Shell window

The Shell window displays the Python prompt, accepts interactive statements, and shows output and error messages.

Example:

```
>>> message = "Welcome to IDLE"
>>> print(message)
Welcome to IDLE

```

### 6.2 Editor window

The editor is where complete Python programs are written.

A program may contain multiple variables, functions, classes, loops, conditional statements, and imports.

For example:

```
def greet(name):
    return f"Hello, {name}!"

user = "Alex"
print(greet(user))

```

The editor makes it easier to modify, save, and reuse the program.

### 6.3 Syntax highlighting

Syntax highlighting visually distinguishes parts of Python code.

For example:

```
# This is a comment

def add(a, b):
    return a + b

print(add(10, 20))

```

The editor may display comments, keywords, strings, and other elements in different colors. The exact colors depend on the selected theme and configuration.

Syntax highlighting helps readability, but it does not guarantee that code is correct.

### 6.4 Running a program

In IDLE, a typical workflow is:

1. Open the editor by selecting **File → New File**.
2. Write Python code.
3. Save the file with a `.py` extension.
4. Select **Run → Run Module**, or press `F5` when the editor is active.
5. Read the output in the Shell window.

For example, save this program as `hello.py`:

```
print("Hello, World!")

```

After running the module, the Shell displays:

```
Hello, World!

```

IDLE may prompt you to save the file before running it if it contains unsaved changes.

### 6.5 The Shell and editor work together

The editor and Shell serve different purposes but work as a connected environment.

The editor stores the program as a source file. When the program is run, Python executes the module and displays its output in the Shell.

The Shell can also be used to inspect objects or call functions that are available in the active interactive environment. However, running a module should not be confused with permanently defining all of its names in the Shell's global namespace.

---

## 7. Python Shell and IDLE on Windows

Windows commonly provides Python through the official Python installer, the Microsoft Store, or other distribution methods.

The exact installation and launch process depends on which method was used.

### 7.1 Installing Python on Windows

A common approach is to download the official installer from:

https\://www\.python.org/downloads/windows/

General procedure:

1. Open the official Python downloads page.
2. Download a suitable stable Python release.
3. Run the installer.
4. Follow the installation instructions.
5. If offered and appropriate for your setup, enable the option to add Python to `PATH`.
6. Complete the installation.

The standard Windows installer generally includes IDLE, although optional installation choices and distribution methods can affect what is available.

### 7.2 Opening the Python Shell on Windows

**Method 1: Using Command Prompt**

1. Open the Start menu.
2. Search for `Command Prompt`.
3. Open it.
4. Enter:

```
py

```

If the Python launcher is installed and configured, the interactive interpreter should start.

Alternatively, try:

```
```

If the command is unavailable, Python may not be installed, may not be on `PATH`, or may be exposed through a different installation method.

**Method 2: Using Windows Terminal or PowerShell**

Open Windows Terminal or PowerShell and run:

```
py

```

You can also request a specific Python version when supported by the launcher:

```
py -3

```

To exit the interactive interpreter, enter:

```
exit()

```

### 7.3 Opening IDLE on Windows

**Method 1: Start menu**

1. Open the Start menu.
2. Search for `IDLE`.
3. Select the entry associated with your Python installation.

The Python Shell window should open.

**Method 2: Using the Python launcher**

Open Command Prompt or PowerShell and enter:

```
py -m idlelib

```

If the installation includes IDLE, this command launches it.

You may also use:

```
python -m idlelib

```

provided that `python` resolves to the intended installation.

### 7.4 Running a Python program in Windows IDLE

1. Open IDLE.
2. Select **File → New File**.
3. Enter the following code:

```
name = input("Enter your name: ")
print("Welcome,", name)

```

4. Save the file as `welcome.py`.
5. Select **Run → Run Module**, or press `F5`.

The Shell will display:

```
Enter your name: Priya
Welcome, Priya

```

The displayed name is an example; enter your own input when running the program.

### 7.5 Windows-specific considerations

- Windows commonly uses the `py` launcher, but it is not guaranteed to be available in every installation.
- File paths often use backslashes, such as `C:\Users\Student\Documents`.
- Windows may hide known file extensions in File Explorer. Check that a source file is actually saved as `.py`, rather than accidentally as `.py.txt`.
- Multiple Python installations can coexist. A command such as `py -0p`, when supported by the installed launcher, can list available Python installations.
- Python installed through the Microsoft Store or another distribution may behave differently from a traditional installer regarding command aliases and paths.

---

## 8. Python Shell and IDLE on macOS

macOS provides Terminal as its standard command-line application. Python installations vary depending on the macOS version and the software installed by the user.

A Python installation should not be assumed to exist merely because macOS provides a Unix-based command-line environment.

### 8.1 Installing Python on macOS

A common approach is to use the official macOS installer:

https\://www\.python.org/downloads/macos/

General procedure:

1. Open the official Python downloads page.
2. Download a suitable macOS installer.
3. Open the downloaded installer package.
4. Follow the installation instructions.
5. Complete the installation.
6. Verify that the intended Python version is accessible from Terminal.

Another option is a package manager such as Homebrew, if it is already installed and appropriate for your setup:

```
brew install python

```

Package-manager installations may have different layouts and may not include IDLE by default. Verify which components are provided by the chosen distribution.

### 8.2 Opening the Python Shell on macOS

1. Open Finder.
2. Navigate to **Applications → Utilities → Terminal**, or search for Terminal using Spotlight.
3. Enter:

```
python3

```

The interactive Python prompt should appear if a suitable installation is available.

For example:

```
>>> print("Hello from macOS")
Hello from macOS

```

Exit with:

```
exit()

```

On macOS, `python3` is generally the safer command to try first because `python` may be unavailable or may refer to a different installation.

### 8.3 Opening IDLE on macOS

There are two common approaches.

**Method 1: Open the installed application**

Depending on the installer, IDLE may be available in the Python installation folder under `/Applications`, or through a corresponding application shortcut.

Open the IDLE application associated with your Python installation.

**Method 2: Launch IDLE from Terminal**

Try:

```
python3 -m idlelib

```

This works when the selected Python installation includes IDLE and its dependencies.

If it does not work, check which Python installation is selected and whether that distribution provides IDLE.

### 8.4 Running a Python program in macOS IDLE

1. Open IDLE.
2. Select **File → New File**.
3. Write the following code:

```
numbers = [10, 20, 30, 40, 50]

total = sum(numbers)
average = total / len(numbers)

print("Total:", total)
print("Average:", average)

```

4. Save the file as `average.py`.
5. Run the module using **Run → Run Module** or `F5`.

Expected output:

```
Total: 150
Average: 30.0

```

### 8.5 macOS-specific considerations

- Use `python3` when starting Python from Terminal unless you have verified that another command points to the intended interpreter.
- Official installer, Homebrew, and other Python installations may coexist.
- Different installations may have different paths and available packages.
- If `python3 -m idlelib` fails, it does not necessarily mean Python itself is missing. The installation may simply lack IDLE.
- macOS file paths generally use forward slashes, such as `/Users/student/Documents`.
- The `F5` shortcut may require the `Fn` key on some keyboards or system configurations.

---

## 9. Python Shell and IDLE on Linux

Linux distributions commonly provide Python through their package managers. However, the availability of IDLE depends on the distribution, installed packages, and desktop environment.

Python may already be installed because other system tools depend on it, but IDLE may need to be installed separately.

### 9.1 Checking whether Python is installed

Open a terminal and enter:

```
python3 --version

```

A successful installation may produce output such as:

```
Python 3.x.x

```

The exact version depends on the installed distribution and Python release.

To locate the interpreter, use:

```
command -v python3

```

### 9.2 Installing Python and IDLE

On Debian- and Ubuntu-based systems, you can generally install the relevant packages using:

```
sudo apt update
sudo apt install python3 python3-idle

```

On Fedora, a typical command is:

```
sudo dnf install python3 python3-idle

```

Package names and availability can vary across Linux distributions and releases. Consult the documentation for your distribution if a package cannot be found.

These commands install software system-wide and may require administrator privileges.

### 9.3 Opening the Python Shell on Linux

Open a terminal and enter:

```
python3

```

You can then execute Python statements:

```
>>> 2 + 3
5
>>> print("Hello from Linux")
Hello from Linux

```

Exit the Shell with:

```
exit()

```

### 9.4 Opening IDLE on Linux

Depending on the distribution and installation, use one of the following:

```
idle3

```

or:

```
python3 -m idlelib

```

The first command is commonly provided by distributions that package IDLE separately. The second launches IDLE through the selected Python interpreter when IDLE is installed and available.

Some Linux installations do not include a graphical desktop environment. In that situation, a GUI application such as IDLE may not be usable without an appropriate graphical session.

### 9.5 Running a Python program in Linux IDLE

Create a new file and enter:

```
for number in range(1, 6):
    print("Number:", number)

```

Save the file as `numbers.py` and select **Run → Run Module**.

Expected output:

```
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5

```

### 9.6 Linux-specific considerations

- Linux distributions may provide multiple Python packages with different names.
- The `python3` command is generally preferred for Python 3.
- Installing IDLE separately is common.
- Linux file paths use forward slashes, such as `/home/student/Documents`.
- Python installations managed by a distribution should generally be maintained using that distribution's package manager.
- Some systems use virtual environments to isolate project dependencies. These are useful for larger projects but are not necessary for basic Shell experiments.

---

## 10. Writing and Running Python Programs

The Shell and IDLE can both be used to execute Python code, but a saved source file is more convenient when a program must be reused.

### 10.1 Creating a Python file

A Python source file usually has the `.py` extension.

For example:

```
hello.py

```

A file can be created in IDLE through **File → New File** and saved using **File → Save As**.

The same file can also be created using another text editor.

### 10.2 Example: A complete Python program

Create a file named `calculator.py`:

```
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero is not allowed."
    return a / b

print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))

```

The program defines four functions and calls each one.

Expected output:

```
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0

```

The same Python source code works on Windows, macOS, and Linux, assuming a compatible Python 3 installation.

### 10.3 Running a file from a terminal

IDLE is not required to run a Python program. A terminal can execute a saved `.py` file directly.

On Windows:

```
py calculator.py

```

On macOS and Linux:

```
python3 calculator.py

```

These commands assume that the terminal is in the directory containing `calculator.py`, or that the file is specified using its correct path.

For example, if the file is in another directory, provide the path to that file.

### 10.4 Interactive execution versus file execution

Interactive execution is useful when experimenting with one expression or testing a short piece of code.

File execution is useful when working on programs that need to be saved, shared, tested repeatedly, or maintained over time.

A common beginner workflow is to experiment in the Shell and then move the useful code into a `.py` file.

---

## 11. Common Python Shell Commands

The following commands and functions are useful when working in a Python Shell.

| Command or function | Purpose                            | Example          |
| ------------------- | ---------------------------------- | ---------------- |
| `print()`           | Display information                | `print("Hello")` |
| `type()`            | Inspect a value's type             | `type(10)`       |
| `help()`            | Access Python help                 | `help(str)`      |
| `dir()`             | List available names or attributes | `dir(str)`       |
| `len()`             | Get the length of an object        | `len("Python")`  |
| `sum()`             | Calculate a sum                    | `sum([1, 2, 3])` |
| `range()`           | Generate a sequence of integers    | `range(5)`       |
| `exit()`            | Leave the interactive interpreter  | `exit()`         |

Examples:

```
>>> len("Python")
6

>>> sum([10, 20, 30])
60

>>> type([1, 2, 3])
<class 'list'>

```

The commands `help()` and `dir()` are particularly useful when exploring Python objects.

For example:

```
>>> help(print)

```

This displays documentation for the built-in `print()` function.

### Important distinction: Shell commands and Python commands

Not every command used around Python is a Python statement.

For example:

```
python3 --version

```

is an operating-system terminal command.

By contrast:

```
print("Hello")

```

is a Python statement.

Do not enter terminal commands at the Python `>>>` prompt unless they are valid Python expressions or statements.

---

## 12. Advantages and Limitations

### 12.1 Advantages of the Python Shell

- Provides immediate feedback.
- Is useful for calculations and quick experiments.
- Helps beginners understand Python expressions and data types.
- Allows functions and variables to be tested interactively.
- Does not require creating a source file for every small experiment.

### 12.2 Limitations of the Python Shell

- Long programs are difficult to manage interactively.
- Code entered in a session is not automatically saved as a reusable source file.
- Repeated experimentation can make a session difficult to follow.
- Variables and functions defined only in the session generally disappear when that session ends.

### 12.3 Advantages of IDLE

- Combines a source-code editor and interactive Shell.
- Provides syntax highlighting and automatic indentation.
- Supports saving and rerunning Python files.
- Provides basic debugging tools.
- Is relatively lightweight and beginner-friendly.
- Is available for multiple operating systems.

### 12.4 Limitations of IDLE

- It offers fewer advanced development features than many full-featured IDEs.
- Large projects may benefit from tools that provide more sophisticated project management, testing, version-control integration, or code navigation.
- Availability depends on the Python distribution and operating system.
- Its graphical interface requires an environment capable of running GUI applications.

### 12.5 Is IDLE enough to learn Python?

Yes. IDLE is sufficient for learning fundamental Python concepts, including:

- Variables and data types.
- Operators and expressions.
- Conditional statements.
- Loops.
- Functions.
- Lists, tuples, dictionaries, and sets.
- File handling.
- Modules and imports.
- Basic object-oriented programming.

More advanced tools can be introduced later as programming requirements grow.

---

## 13. Common Errors and Troubleshooting

### 13.1 `python` or `python3` is not recognized

A terminal may report that the command is not found or not recognized.

Possible causes:

- Python is not installed.
- The installation directory is not on the command search path.
- The selected command differs from the one configured by the installation method.
- An operating-system command alias interferes with the expected command.

Possible solutions:

**Windows:**

```
py --version

```

If the launcher is available, use:

```
py

```

**macOS and Linux:**

```
python3 --version

```

If neither command works, verify the installation and follow the appropriate operating-system installation instructions.

### 13.2 `No module named idlelib`

This error indicates that the selected Python interpreter cannot locate the `idlelib` module.

Possible causes include:

- IDLE is not installed.
- The Python distribution does not include IDLE.
- The command uses a different Python installation from the one containing IDLE.

On Debian- or Ubuntu-based Linux systems, installing `python3-idle` is a common solution.

On Windows and macOS, verify that the selected Python distribution includes IDLE.

### 13.3 Syntax errors

Consider the following incorrect code:

```
if 10 > 5
    print("Ten is greater")

```

It is missing a colon after the condition.

Correct version:

```
if 10 > 5:
    print("Ten is greater")

```

Python uses indentation and punctuation to define program structure. Read the error message carefully and inspect the indicated line and nearby code.

### 13.4 Indentation errors

Incorrect indentation can prevent a program from running.

Incorrect:

```
for number in range(3):
print(number)

```

Correct:

```
for number in range(3):
    print(number)

```

The statement inside the loop must be indented.

### 13.5 The Shell appears frozen or is waiting for input

The interpreter may be waiting for the completion of a multiline statement or for input requested by a function such as `input()`.

Check whether the prompt is `...` rather than `>>>`.

For example:

```
>>> print(
... "Hello"
... )
Hello

```

Complete the statement or cancel the current input when appropriate.

### 13.6 Changes to a file do not appear when testing code

If you modify a source file but the Shell still seems to use older behavior, check that:

- The correct file was saved.
- You are running the intended file.
- The latest changes were saved before execution.
- You are not confusing an older interactive definition with the version in the source file.

In IDLE, save the file and run the module again.

### 13.7 The output does not appear in the expected place

When a module is run from IDLE, output normally appears in its Shell window. When a program is launched from a terminal, output normally appears in that terminal.

If the program is waiting for user input, enter the requested value before expecting further output.

---

## 14. Best Practices for Beginners

1. **Use the Shell for small experiments.** Test expressions, explore data types, and try short pieces of code interactively.
2. **Use IDLE's editor for complete programs.** Save reusable code in `.py` files instead of relying on a long interactive session.
3. **Understand the difference between terminal commands and Python statements.** Commands such as `python3 --version` belong in the operating-system terminal, whereas `print("Hello")` belongs in Python.
4. **Read error messages carefully.** They often indicate the location and type of a problem.
5. **Practice indentation.** Python uses indentation to define blocks of code.
6. **Save files in an organized directory.** For example, create a folder named `PythonPractice` and store your practice programs there.
7. **Use descriptive filenames.** Names such as `calculator.py` and `student_marks.py` are more informative than `file1.py`.
8. **Use the correct interpreter command for your operating system.** On Windows, `py` is commonly available; on macOS and Linux, `python3` is generally a good starting point.
9. **Avoid unnecessary changes to system-managed Python installations.** In particular, Linux users should generally use their distribution's package manager for system Python packages.
10. **Learn one tool well before adding complexity.** IDLE is sufficient for a substantial amount of beginner practice. More advanced editors and IDEs can be introduced when needed.

---

## 15. Conclusion

The Python Shell and IDLE are important tools for learning and developing Python programs.

The **Python Shell** is an interactive environment that executes statements and displays results immediately. It is ideal for quick calculations, testing expressions, experimenting with variables, and exploring built-in functions.

**IDLE** is a lightweight development environment that includes an interactive Shell, a source-code editor, syntax highlighting, automatic indentation, program execution, and basic debugging capabilities.

The main distinction is that the Shell focuses on interactive execution, whereas IDLE provides a more complete environment for writing, saving, running, and debugging Python programs.

On Windows, Python and IDLE are commonly installed together through the standard installer. On macOS, they can be obtained through the official installer or another Python distribution. On Linux, IDLE is often installed as a separate package.

Although installation and launch commands vary, the same fundamental Python syntax and programming concepts apply across all three operating systems.

For beginners, a practical approach is to start with the Python Shell for small experiments and use IDLE's editor whenever a program needs to be saved and executed repeatedly.

---

## Quick Reference

| Task                        | Windows         | macOS                | Linux                |
| --------------------------- | --------------- | -------------------- | -------------------- |
| Check Python version        | `py --version`  | `python3 --version`  | `python3 --version`  |
| Start interactive Shell     | `py`            | `python3`            | `python3`            |
| Launch IDLE from a terminal | `py -m idlelib` | `python3 -m idlelib` | `python3 -m idlelib` |
| Run a Python file           | `py hello.py`   | `python3 hello.py`   | `python3 hello.py`   |
| Exit the interactive Shell  | `exit()`        | `exit()`             | `exit()`             |

**Note:** These are common commands, not universal guarantees. They assume that the relevant interpreter or IDLE component is installed and accessible. Linux distributions and alternative Python installations may require different commands or package names.

### Official Resources

- Python documentation: https://docs.python.org/3/
- Python IDLE documentation: https://docs.python.org/3/library/idle.html
- Python downloads for Windows: https//www\.python.org/downloads/windows/
- Python downloads for macOS: https\://www\.python.org/downloads/macos/
- Python downloads for other platforms: https\://www\.python.org/downloads/

By. Jatin Kumar Mehta | **End of Document** | https://github.com/jkmloom/py-recap