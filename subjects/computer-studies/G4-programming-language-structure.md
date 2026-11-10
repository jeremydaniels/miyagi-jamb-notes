# JAMB Computer Studies Notes: Programming Language Structure

## What JAMB expects

This topic is Section G, Topic 4 of the JAMB Computer Studies syllabus: Programming Language Structure. It covers the basic building blocks used to write computer programs. 

This file covers the following content items:
- **a. Basic Statements**
- **b. Arithmetic/string operators**
- **c. Subunits**
- **d. Primitive and non-primitive data**

By the end of these notes, you should be able to:
1. Identify features/syntax of a programming language (Keywords, Variable types, Constants/literals, Numeric, String/alphanumeric, Basic characteristics of the language). *(Objective i)*
2. Identify basic statements of a high-level programming language (Input, Output, Processing, Comments, Subunits, Statements like Iteration/Loop, Conditional, Assignment, Dimension, etc.). *(Objective ii)*
3. Use arithmetic operators and expressions. *(Objective iii)*
4. Use string operators and expressions. *(Objective iv)*
5. Identify built-in functions. *(Objective v)*
6. Identify primitive data (Integer, float, Boolean, character, etc.). *(Objective vi)*
7. Identify non-primitive Data Types (Arrays, classes, string, etc). *(Objective vii)*
8. Understand complex data structures (Trees, graphs, linked lists, objects etc.). *(Objective viii)*

**Note on the syllabus wording:** The syllabus asks you to identify "Dimension" as a basic statement. This refers to the `DIM` statement, which is used in the older BASIC programming language to declare arrays. Because JAMB frequently asks about older programming concepts alongside modern ones, we will explain `DIM` and give some examples in BASIC as well as modern examples in Python. Furthermore, the syllabus classifies a "string" as a non-primitive data type; while in some modern languages strings are built-in primitives, in languages like C and Java they are non-primitive arrays of characters. We will follow the syllabus classification.

---

## Features and Syntax of a Programming Language

**Objective i: Identify features/syntax of a programming language**

Just like human languages (English, Hausa, Yoruba, Igbo) have grammar rules and vocabularies, programming languages have sets of rules called **syntax**. If you break the syntax rules, the computer will give a "syntax error" and the program will not run.

### 1. Keywords (Reserved Words)
Keywords are special words built into the programming language that have a specific meaning. You cannot use them as names for your own variables. 
- Examples in Python: `if`, `else`, `while`, `for`, `def`, `import`, `print`.
- Examples in BASIC: `LET`, `PRINT`, `INPUT`, `DIM`, `REM`.

### 2. Variables and Variable Types
A **variable** is a named storage location in the computer's memory that holds data. The data inside a variable can change while the program is running.
Depending on the language, variables have different **types**. Some languages (like C or Java) are *statically typed*, meaning you must state the type of data (e.g., integer, text) the variable will hold before using it. Other languages (like Python) are *dynamically typed*, meaning the computer figures out the type automatically.

### 3. Constants and Literals
A **constant** is a named memory location whose value **cannot change** while the program is running (for example, a constant named `PI` set to `3.14159`).
A **literal** is the actual raw data value you type directly into the code. 
- **Numeric literals:** Numbers used for calculations. They can be whole numbers (integers, e.g., `500`) or decimal numbers (e.g., `99.9`).
- **String/alphanumeric literals:** Text enclosed in quotation marks. It can contain letters, numbers, and symbols. Example: `"JAMB 2024"`, `"Ngozi"`.

### 4. Basic Characteristics of High-Level Languages
High-level programming languages (like Python, Java, C++, BASIC) share several characteristics:
- **Readability:** They use English-like words and mathematical symbols, making them easy for humans to read and write.
- **Portability:** A program written in a high-level language on one computer can usually run on a different type of computer with little or no modification.
- **Abstraction:** They hide the complex details of the computer's hardware (like memory addresses and CPU registers) from the programmer.
- **Need for Translation:** They must be translated into machine code (binary 0s and 1s) by a compiler or an interpreter before the computer can execute them.

---

## Basic Statements of a High-Level Language

**Content a & Objective ii: Basic statements of a high-level programming language**

A **statement** is a single instruction that the computer executes. Programs are made up of a sequence of statements.

### 1. Assignment Statements
An assignment statement gives a value to a variable. In most languages, this is done using the equals sign (`=`). The computer evaluates whatever is on the right side of the `=` and stores it in the variable on the left side.

```python
# Python assignment examples
score = 85
student_name = "Adebayo"
total_cost = 500 * 3
```

### 2. Input and Output Statements
- **Input statements:** These allow the program to receive data from the user (usually via the keyboard) while the program is running.
- **Output statements:** These display the results of processing to the user (usually on the screen).

```python
# Python Input and Output
name = input("Enter your name: ")  # Input statement
print("Welcome to JAMB, " + name)  # Output statement
```

### 3. Processing Statements
Processing statements are instructions that perform arithmetic calculations or logical operations. They take input data, process it (often using mathematical formulas), and produce a result.

```python
# Processing statement calculating simple interest
interest = (principal * rate * time) / 100
```

### 4. Comments
Comments are notes written by the programmer to explain what the code does. The computer completely **ignores** comments when running the program. They are purely for human readers.
- In Python, a single-line comment starts with `#`.
- In C, Java, or JavaScript, a comment starts with `//`.
- In BASIC, comments start with the keyword `REM` (Remark).

### 5. Conditional Statements
Conditional statements (also called selection statements) allow the program to make decisions. The program checks a condition (which is either True or False) and decides which block of code to run.

```python
# Python conditional statement
mark = 65

if mark >= 50:
    print("You passed!")
else:
    print("You failed. Try again.")
```

### 6. Iteration / Loop Statements
Iteration means repeating a set of instructions. Loop statements allow the computer to do something over and over again until a specific condition is met. The two most common loops are **FOR** loops (used when you know how many times to repeat) and **WHILE** loops (used when you repeat until a condition becomes false).

**Tracing a Loop:** Let's look at a Python `while` loop and trace its execution by hand in a trace table.

```python
count = 1
total = 0
while count <= 3:
    total = total + count
    count = count + 1
print(total)
```

*Trace Table for the loop above:*

| Step | `count` at start | `total` at start | Condition: `count <= 3` | New `total` | New `count` |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | 0 | True | 0 + 1 = 1 | 1 + 1 = 2 |
| 2 | 2 | 1 | True | 1 + 2 = 3 | 2 + 1 = 3 |
| 3 | 3 | 3 | True | 3 + 3 = 6 | 3 + 1 = 4 |
| 4 | 4 | 6 | False (Loop ends) | - | - |

*Output:* The final value of `total` printed is `6`.

### 7. Dimension Statements (DIM)
In early programming languages like BASIC, before you can use a list (an array) to store multiple items, you must declare how much memory to set aside. This is done using the **Dimension** statement, written as `DIM`.

```basic
REM BASIC Dimension statement
REM This sets aside memory for an array of 10 student scores
DIM SCORES(10)
```
JAMB often tests the `DIM` statement: remember that it stands for "Dimension" and is used to declare the size of an array.

---

## Arithmetic and String Operators

**Content b, Objective iii & iv: Arithmetic/string operators and expressions**

An **operator** is a special symbol that tells the compiler to perform a specific mathematical or logical task. An **expression** is a combination of variables, constants, and operators that evaluates to a single value (e.g., `5 + 3`).

### 1. Arithmetic Operators

Arithmetic operators perform standard mathematics. 

| Operator | Meaning | Example Expression | Result |
| --- | --- | --- | --- |
| `+` | Addition | `10 + 3` | 13 |
| `-` | Subtraction | `10 - 3` | 7 |
| `*` | Multiplication | `10 * 3` | 30 |
| `/` | Division | `10 / 2` | 5 |
| `%` (or MOD) | Modulo (Remainder) | `10 % 3` | 1 |
| `**` (or `^`) | Exponentiation (Power) | `10 ** 3` | 1000 |

**Modulo (`%`) Note:** The modulo operator gives the *remainder* of a division. For example, 10 divided by 3 is 3 with a remainder of 1. Therefore, `10 % 3` equals 1. This is heavily tested in programming exams!

**Order of Precedence:** Just like BODMAS in mathematics, programming languages evaluate expressions in a specific order: Parentheses first, then Exponents, then Multiplication/Division/Modulo, and finally Addition/Subtraction.

### 2. String Operators

Strings are text. You cannot do normal mathematics on text, but you can use specific string operators.

- **Concatenation:** This means joining two strings end-to-end. In Python, Java, and C++, this is done using the `+` sign. In some other languages (like Visual Basic), the `&` symbol is used.
- **Repetition:** In Python, you can use the `*` operator to repeat a string.

```python
# String Concatenation
word1 = "Hello"
word2 = "JAMBite"
greeting = word1 + " " + word2
# greeting is now "Hello JAMBite"

# String Repetition
cheer = "Go! " * 3
# cheer is now "Go! Go! Go! "
```

---

## Built-in Functions

**Objective v: Built in functions**

A **function** is a reusable block of code designed to perform a single, specific task. Programming languages come with hundreds of **built-in functions** (sometimes called standard library functions) so you do not have to write basic tasks from scratch.

Common built-in functions include:
- **Math functions:** 
  - `abs(-15)` returns the absolute (positive) value: `15`.
  - `max(5, 10, 3)` returns the highest value: `10`.
  - `sqrt(25)` (or `SQR` in BASIC) returns the square root: `5`.
  - `round(3.14159, 2)` rounds to 2 decimal places: `3.14`.
- **String functions:** 
  - `len("Hello")` returns the length of the string: `5`.
  - `upper("jamb")` converts text to uppercase: `"JAMB"`.
- **I/O functions:** `print()`, `input()`.

---

## Subunits (Modular Programming)

**Content c & part of Objective ii: Subunits**

Real-world computer programs are massive (often millions of lines of code). Instead of writing one huge list of instructions, programmers break the program down into smaller, manageable chunks called **subunits** or **subprograms**. This is called **modular programming**.

Different terms are used depending on the programming language and how the subunit behaves:

| Subunit Term | Meaning and Characteristics |
| --- | --- |
| **Function** | A block of code that takes inputs, performs a calculation, and **returns a value** to the main program. (e.g., a function that calculates tax and gives back the tax amount). |
| **Procedure / Subroutine** | A block of code that performs a specific action but **does not return a value**. (e.g., a subroutine that clears the computer screen or prints a customized receipt). *Note: In Python, everything is called a function, but in older languages like Pascal or BASIC, the distinction is strict.* |
| **Method** | A function that is tied to a specific **Object** or **Class** in Object-Oriented Programming (OOP). |

**Advantages of using subunits:**
1. **Reusability:** You can write the code once and call it multiple times.
2. **Readability:** It makes the main program cleaner and easier to read.
3. **Debugging:** It is easier to find and fix errors in a small, isolated module than in a massive block of code.

---

## Primitive and Non-Primitive Data Types

**Content d, Objective vi & vii: Primitive and non-primitive data**

Every piece of data in a program has a **data type**. This tells the computer how much memory to allocate and what kind of operations can be performed on the data. Data types are broadly divided into Primitive and Non-Primitive.

### Primitive Data Types (Objective vi)
Primitive data types are the most basic, foundational data types built directly into the programming language. They hold a **single, simple value**.

1. **Integer (`int`):** Whole numbers without a decimal point. Can be positive, negative, or zero.
   *Example: `14`, `-300`, `0`*
2. **Float / Real (`float`):** Numbers that contain a fractional part or decimal point.
   *Example: `3.14`, `-0.001`, `10.0`*
3. **Character (`char`):** A single letter, number, or symbol.
   *Example: `'A'`, `'7'`, `'?'`*
4. **Boolean (`bool`):** A logical value that can only be one of two states: **True** or **False**.

### Non-Primitive Data Types (Objective vii)
Non-primitive data types (also called reference types) are created by combining primitive data types. They do not just store a single value; they store **collections of values** or complex data.

1. **Strings:** A sequence of characters. While some simple languages treat strings as primitive, strictly speaking (and in JAMB's classification), a string is a non-primitive array of characters.
   *Example: `"Nigeria"` is an array of characters `'N'`, `'i'`, `'g'`, `'e'`, `'r'`, `'i'`, `'a'`.*
2. **Arrays:** A collection of items of the **same data type** stored in a sequence. You access individual items using an index number (usually starting at 0).
   *Example: An array of integers containing student ages: `[15, 17, 16, 18]`.*
3. **Classes:** A blueprint or template for creating objects in Object-Oriented Programming. A class defines what data an object will hold and what actions (methods) it can perform.

---

## Complex Data Structures

**Objective viii: Complex data structures**

As programs get more advanced, simple arrays are not enough to organize data efficiently. Computer Scientists use **complex data structures** to manage large amounts of data. 

### 1. Trees
A tree is a **hierarchical** data structure. Unlike arrays that store data in a straight line, trees store data in a branching manner, much like a family tree.
- **Root:** The topmost data point (node) in the tree.
- **Node:** Any individual point of data in the tree.
- **Leaf:** A node at the bottom of the tree that has no "children".
Trees are highly efficient for searching and sorting data (e.g., the directory structure of folders on your computer is a tree).

[IMAGE: A hierarchical diagram of a Tree data structure. At the top is a single circle labeled 'Root Node'. Lines branch down to two child circles. From those, more lines branch down to further child circles labeled 'Leaf Nodes' at the very bottom. Clean flat textbook illustration, white background.]

### 2. Graphs
A graph is a **network** data structure. Unlike a tree, a graph does not have a strict "top-down" hierarchy. Any node can be connected to any other node.
- **Vertices (Nodes):** The data points.
- **Edges:** The lines connecting the vertices.
Graphs are used to represent networks, like maps of roads connecting cities, or friends connecting on a social media platform.

[IMAGE: A network diagram of a Graph data structure. Several circles (Vertices) scattered in a space, connected by straight lines (Edges) in a web-like, non-hierarchical pattern. Clean flat textbook illustration, white background.]

### 3. Linked Lists
A linked list is a linear sequence of data, but unlike an array, the data is not stored together in memory. Instead, each element (called a **node**) contains two parts:
1. The **Data** itself.
2. A **Pointer (or Link)** that stores the memory address of the *next* node in the sequence.
Because of this design, you can easily insert or remove items from the middle of a linked list without moving all the other items (which you would have to do in an array).

[IMAGE: A diagram of a Linked List. Three rectangular boxes arranged horizontally. Each box is divided into two parts: the left part labeled 'Data' and the right part containing an arrow pointing to the next box. The arrow from the final box points to the word 'Null'. Clean flat textbook illustration, white background.]

### 4. Objects
An object is an instance of a **Class** (discussed in non-primitive types). Objects are complex because they combine two things into a single unit:
- **State (Data/Attributes):** Variables inside the object (e.g., a "Car" object might have data like `color = "Red"`, `speed = 120`).
- **Behavior (Methods):** Functions inside the object that use the data (e.g., a `brake()` method that reduces the speed).

---

## Key terms

| Term | Meaning |
| --- | --- |
| **Syntax** | The strict grammar rules of a programming language. |
| **Keyword** | A reserved word built into the language (e.g., `IF`, `WHILE`, `DIM`) that cannot be used as a variable name. |
| **Variable** | A named location in memory whose value can change during execution. |
| **Literal** | The actual raw data written directly into the code (e.g., `5`, `"Hello"`). |
| **Statement** | A single instruction in a programming language. |
| **Modulo (`%`)** | An arithmetic operator that calculates the remainder of a division. |
| **Subroutine/Procedure** | A module of code that performs a task but does not return a value. |
| **Primitive Data** | Basic data types built into the language (Integer, Float, Boolean, Char). |
| **Array** | A non-primitive sequence of variables of the *same* data type. |
| **Tree** | A complex hierarchical data structure with roots, branches, and leaves. |
| **Graph** | A complex network data structure made of vertices and edges. |
| **Linked List** | A complex linear data structure where each node points to the next. |

---

## Exam tips and common mistakes

*   **Modulo Operator:** Do not confuse modulo (`%`) with percentage or division. `10 % 3` is the **remainder** of 10 divided by 3, which is `1`.
*   **DIM in BASIC:** JAMB frequently tests the `DIM` statement. Remember it stands for "Dimension" and it is used to declare the size of an array.
*   **Primitive vs. Non-Primitive:** A common trick question asks you to identify the non-primitive type from a list. Remember: Integer, Float, Boolean, and Char are primitive. Arrays, Strings, and Classes are non-primitive.
*   **Function vs. Subroutine:** If a JAMB question asks for the difference, remember that a **function returns a value**, while a **subroutine/procedure performs an action but does not return a value**.
*   **Tree vs. Graph:** Trees are *hierarchical* (top-down, root-to-leaf). Graphs are a *network* without a strict hierarchy.
*   **Strings in JAMB:** Though Python treats strings simply, always remember that fundamentally (and for JAMB), a string is a non-primitive array of characters.

---

## Quick summary

1. A programming language's **syntax** is its set of grammar rules. The vocabulary includes reserved **keywords**, named **variables**, and fixed **literals**.
2. Basic statements tell the computer what to do: **assignment** gives variables values, **I/O** handles data entry and display, **conditionals** make decisions (`IF`), and **loops** repeat actions (`WHILE`, `FOR`).
3. **Operators** process data. Arithmetic operators do math (including modulo `%` for remainders). String operators can concatenate (join) text together.
4. **Built-in functions** (like `max()`, `abs()`, `len()`) are pre-written modules provided by the language to perform common tasks.
5. Large programs use **subunits**. **Functions** return values, **procedures/subroutines** do not, and **methods** are tied to objects.
6. **Primitive data types** hold a single value: Integers (whole numbers), Floats (decimals), Booleans (True/False), and Characters.
7. **Non-primitive data types** hold collections: Arrays, Strings, and Classes.
8. **Complex data structures** include **Trees** (hierarchical), **Graphs** (networks), **Linked Lists** (nodes with pointers), and **Objects** (combining data and methods).

---

## Practice questions

**1. Which of the following is a primitive data type?**
- A. Array
- B. String
- C. Class
- D. Boolean

**Answer: D.** Boolean is a primitive data type (along with integer, float, and character). Arrays, strings, and classes are non-primitive.

**2. Evaluate the following arithmetic expression: 14 % 4**
- A. 3.5
- B. 3
- C. 2
- D. 0

**Answer: C.** The modulo operator (`%`) finds the remainder. 14 divided by 4 is 3 with a remainder of 2. 

**3. In programming, a word that is built into the language and cannot be used as a variable name is called a:**
- A. Literal
- B. Keyword
- C. Constant
- D. Subunit

**Answer: B.** Keywords (or reserved words) like `IF`, `WHILE`, and `DIM` have special meanings in the language and cannot be used for variable names. 

**4. The `DIM` statement in the BASIC programming language is used to:**
- A. Dim the brightness of the screen
- B. Perform mathematical division
- C. Declare the size of an array in memory
- D. Create a continuous loop

**Answer: C.** `DIM` stands for Dimension. It is used to set aside memory space for an array. 

**5. Which complex data structure is organized hierarchically, featuring a root, branches, and leaves?**
- A. Linked List
- B. Graph
- C. Array
- D. Tree

**Answer: D.** A Tree is a hierarchical data structure. A graph is a network, and a linked list is linear.

**6. What is the primary difference between a function and a subroutine/procedure?**
- A. A function cannot take inputs, but a subroutine can.
- B. A subroutine returns a value, while a function does not.
- C. A function returns a value, while a subroutine does not.
- D. A function is a primitive data type, while a subroutine is complex.

**Answer: C.** By traditional programming definitions, a function evaluates data and returns a result to the main program, whereas a subroutine executes a task without returning a value. 

**7. Joining two strings together end-to-end (e.g., "JAMB" and "2024" becoming "JAMB2024") is called:**
- A. Repetition
- B. Concatenation
- C. Modulo
- D. Dimensioning

**Answer: B.** Concatenation is the string operation used to link two or more strings together, often using the `+` operator.

**8. Which of the following statements is a loop (iteration) statement?**
- A. IF...THEN...ELSE
- B. WHILE...DO
- C. DIM
- D. PRINT

**Answer: B.** `WHILE` is used for iteration (looping). `IF` is a conditional statement, `DIM` is for arrays, and `PRINT` is an output statement.

**9. Consider a linked list data structure. What does each node in a linked list contain?**
- A. A root and a leaf
- B. Data and a pointer to the next node
- C. A string and a literal
- D. A condition and a loop statement

**Answer: B.** Every node in a linked list contains the actual data and a pointer (or link) containing the memory address of the next node in the sequence.

**10. A programmer wants to write a block of text in the code explaining how a complex formula works. This text should be ignored by the computer when the program runs. The programmer should use a:**
- A. Processing statement
- B. Variable
- C. Literal
- D. Comment

**Answer: D.** Comments are used to leave notes for humans in the code. Compilers and interpreters completely ignore comments during execution.
