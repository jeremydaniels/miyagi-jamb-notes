# JAMB Computer Studies Notes: Programming Language (PL)

## What JAMB expects

This topic is Section G, Topic 1 of the JAMB Computer Studies syllabus: Developing Problem-Solving Skills – Programming Language (PL). It covers the following content items:

* (a) Definition and Classification of PL
* (b) Advantages and disadvantages of different levels of PL

By the end of these notes, you should be able to:

1. Define Programming Language (PL).
2. Identify different classifications of PL (Machine Language, Assembly languages, and High-Level languages).
3. Give advantages and disadvantages of Machine Language, Assembly Language, and High-Level programming Language.

**Note on the syllabus wording:** The syllabus describes High-Level languages as "anything that are machine independent" (the correct grammar is "anything that is machine independent"). It also lists "Pearl" as an example of a high-level language; the correct spelling of this programming language is **Perl**. The notes below use the correct spellings and grammar while covering exactly what the syllabus asks for. High-Level Languages are covered in even more depth in `G2-high-level-languages.md`.

## What is a Programming Language?

**Objective i: Define Programming Language (PL)**
**Content (a): Definition and Classification of PL**

A **Programming Language (PL)** is a formal set of instructions, vocabulary, and grammatical rules used to write computer programs. It allows a human being to communicate with a computer system and give it exact commands to perform specific tasks.

Just as humans use languages like English, Hausa, Igbo, or Yoruba to communicate with one another, programmers use programming languages to communicate with computers. Because the CPU (Central Processing Unit) only understands electronic signals (represented as 0s and 1s), programming languages provide a bridge. Depending on the language, this bridge can be very close to the computer's native binary language, or very close to human language.

## Classification of Programming Languages

**Objective ii: Identify different classifications of PL.**
**Content (a): Definition and Classification of PL**

Programming languages are broadly classified into two main levels based on how close they are to the computer's hardware: **Low-Level Languages** and **High-Level Languages**. The JAMB syllabus divides them into three specific classifications:

1. Machine Language (Low-Level)
2. Assembly Language (Low-Level)
3. High-Level Language

[IMAGE: A pyramid diagram showing the hierarchy of programming languages. At the bottom (widest part) is "Hardware". The layer above it is "Machine Language (1s and 0s)", followed by "Assembly Language (Mnemonics)". The top layer is "High-Level Languages (Python, Java, C, etc.)", showing an arrow pointing upwards labeled "Closer to human language" and an arrow pointing downwards labeled "Closer to machine hardware". Clean flat textbook illustration, white background.]

### 1. Machine Language

Machine language is the **first-generation language (1GL)**. It is the lowest level of programming language and the only language that a computer's hardware (the CPU) can understand directly. 

* **How it works:** It is written entirely in binary machine code—a series of `0`s and `1`s.
* **Interpretation:** According to the syllabus, it is "interpreted directly in hardware." This means there is no need for a translator software; the CPU reads the 0s and 1s and acts on them immediately.
* **Example:** An instruction to add two numbers might look like this to the computer: `10001011 01010101`.

### 2. Assembly Language

Assembly language is a **second-generation language (2GL)**. It was developed to make programming easier than writing endless strings of 0s and 1s.

* **How it works:** It uses short alphabetical codes called **mnemonics** (pronounced *ne-mon-iks*) instead of binary numbers. Examples of mnemonics include `ADD` (for addition), `SUB` (for subtraction), and `MOV` (to move data).
* **Wrapper over machine code:** The syllabus describes assembly language as "thin wrappers over a corresponding machine language." This means that every single assembly command translates directly to one specific machine language command. Because of this, it is also known as a **symbolic language**.
* **Translation:** The hardware cannot understand mnemonics directly. A special program called an **Assembler** is required to translate Assembly Language into Machine Language before the computer can run it.

```text
; A simple Assembly Language example
MOV AL, 5   ; Move the number 5 into register AL
ADD AL, 3   ; Add 3 to register AL
```

### 3. High-Level Languages (HLL)

High-Level languages are **third-generation languages (3GL)** and above. They were designed to be as close to human language (specifically English) and normal mathematical notation as possible.

* **How it works:** They use familiar English words like `PRINT`, `IF`, `THEN`, `WHILE`, and `FOR`. This means the programmer can focus on solving the problem rather than worrying about the internal workings of the CPU.
* **Machine independent:** The syllabus defines HLLs as "anything that are machine independent." This means a program written in a high-level language on one type of computer (like a Windows PC) can easily be modified or run directly on a completely different computer (like an Apple Mac or a smartphone). They are not tied to one specific CPU architecture.
* **Examples named in the syllabus:** 
  * **BASIC** (Beginner's All-purpose Symbolic Instruction Code)
  * **C**
  * **Java**
  * **Fortran 2008** (Formula Translation)
  * **Python**
  * **Perl** (printed as "Pearl" in the syllabus)
* **Translation:** Computers cannot run high-level languages directly. They must be translated into machine code using system software known as a **Compiler** or an **Interpreter**.

```python
# A simple High-Level Language example (Python)
x = 5
y = 3
print(x + y)
```

## Advantages and Disadvantages of Different Levels of PL

**Objective iii: Give advantages and disadvantages of Machine Language, Assembly Language and High programming Language.**
**Content (b): Advantages and disadvantages of different levels of PL**

Every classification of programming language has situations where it is the best tool for the job.

### Machine Language

**Advantages:**
1. **Extremely fast execution:** Because the code is already in binary, the CPU executes it immediately. There is no translation delay.
2. **Direct hardware control:** It allows the programmer to control the computer's memory and CPU at the most fundamental level.
3. **No translator needed:** It does not require an assembler, compiler, or interpreter.

**Disadvantages:**
1. **Very difficult to learn and write:** Humans do not naturally read strings of thousands of `0`s and `1`s. Writing it is tedious and confusing.
2. **Highly error-prone:** A single missing or flipped `0` or `1` can crash the entire program, and finding that mistake (debugging) is incredibly difficult.
3. **Machine dependent:** A machine code program written for an Intel CPU will not work on an ARM CPU (like the one in a smartphone). It is completely tied to one specific hardware design.

### Assembly Language

**Advantages:**
1. **Easier than Machine Language:** Using mnemonics (like `ADD` and `SUB`) is much easier to read, write, and remember than binary code.
2. **Fast and efficient:** It is highly optimized and runs very fast, almost as fast as machine code.
3. **Hardware manipulation:** Like machine code, it still allows deep, precise control over the computer's hardware and memory, which is useful for writing operating systems or controlling specific hardware devices.

**Disadvantages:**
1. **Still difficult to learn:** While easier than binary, it is still very complex and requires a deep understanding of the computer's internal architecture (like registers and memory addresses).
2. **Machine dependent:** Assembly language is strictly tied to specific CPU families. An assembly program written for one processor must be completely rewritten for a different processor.
3. **Long code:** It takes many lines of Assembly code to perform simple tasks that would take only one line in a High-Level Language.
4. **Requires a translator:** It must be translated by an Assembler before it can run.

### High-Level Languages (HLL)

**Advantages:**
1. **Machine independent (Portable):** A program written in a high-level language can run on many different types of computers with little or no modification.
2. **Easy to learn and use:** Because they use English-like words and standard mathematics, they are much easier to read, write, and teach.
3. **Faster program development:** Programmers can write software much faster because one line of high-level code can replace dozens of lines of assembly code.
4. **Easier to debug:** Errors are easier to locate and fix, and compilers/interpreters often point out exactly where the mistake is.

**Disadvantages:**
1. **Slower execution time:** High-level languages must be translated into machine code by a compiler or interpreter. This translation takes time, making the program run slower than machine or assembly code.
2. **Uses more memory:** High-level code relies on complex translation software and libraries, which generally take up more memory space than low-level code.
3. **Less control over hardware:** The programmer is kept away from the direct hardware, making it difficult to write programs that need extremely precise timing or direct hardware manipulation (like device drivers).

### Summary Comparison Table

| Feature | Machine Language | Assembly Language | High-Level Language |
| :--- | :--- | :--- | :--- |
| **Generations** | 1st Generation (1GL) | 2nd Generation (2GL) | 3rd Generation (3GL) and above |
| **Language format** | Binary (`0`s and `1`s) | Mnemonics (e.g., `ADD`, `MOV`) | English-like statements |
| **Machine dependency**| Highly machine-dependent | Machine-dependent | Machine-independent (Portable) |
| **Ease of learning** | Extremely difficult | Difficult | Much easier |
| **Execution speed** | Very fast | Fast | Slower |
| **Translator needed** | None | Assembler | Compiler or Interpreter |

## Key terms

| Term | Meaning |
| :--- | :--- |
| **Programming Language** | A formal set of rules, vocabulary, and grammar used to instruct a computer to perform tasks. |
| **Machine Language** | The lowest-level programming language consisting entirely of binary 0s and 1s, interpreted directly by the hardware. |
| **Assembly Language** | A low-level programming language that uses mnemonics as thin wrappers over machine code. |
| **Mnemonics** | Short alphabetical codes (like ADD, SUB) used in assembly language to represent machine operations. |
| **High-Level Language** | A programming language using English-like words that is machine-independent (portable). |
| **Assembler** | System software that translates assembly language into machine language. |
| **Machine independent** | The ability of a programming language to run on different types of computer systems without needing to be rewritten. |
| **Compiler / Interpreter** | System software used to translate High-Level Languages into machine code. |

## Exam tips and common mistakes

* **Syllabus quirks:** Remember that JAMB spells Perl as **Pearl** in this syllabus section. If you see "Pearl" in a multiple-choice list of languages, recognize it as a High-Level Language.
* **Dependency vs Independency:** The most frequently tested difference is machine dependency. Machine and Assembly languages are **machine-dependent**. High-Level languages are **machine-independent**.
* **Interpreted directly:** Do not confuse the word "interpreted" in "machine code is interpreted directly in hardware" with a High-Level Language Interpreter. It just means the CPU understands the binary instantly without software translation.
* **Assembly is Low-Level:** A very common mistake is thinking Assembly is high-level because it uses letters instead of numbers. It is **low-level** because it is tied directly to the CPU's architecture.
* **Thin wrapper/Symbolic:** If a question mentions "symbolic language" or a "thin wrapper over machine language," the answer is exactly Assembly Language.

## Quick summary

1. A Programming Language is a set of rules and instructions used to write computer programs.
2. Machine Language is the lowest level, consisting of binary (`1`s and `0`s), and is interpreted directly by the computer hardware with no translation needed.
3. Assembly Language is a low-level language that uses letter codes called mnemonics (like `ADD`, `SUB`) instead of binary, making it slightly easier for humans. It requires an Assembler to translate it.
4. High-Level Languages use English-like words (e.g., BASIC, Python, C, Java, Fortran). They are very easy for humans to read and write.
5. High-Level Languages are machine-independent, meaning programs can be transferred across different types of computers.
6. Machine and Assembly languages execute very quickly and use less memory, but are very difficult to write and are locked to specific hardware.
7. High-Level languages are easier to code and debug but execute slower because they require a translator (Compiler or Interpreter).

## Practice questions

**1. Which of the following best defines a programming language?**
- A. A device used to translate English to Hausa
- B. A set of rules and vocabulary used to give instructions to a computer
- C. A machine that converts data into information
- D. A system software used to boot the computer

**Answer: B.** A programming language provides the vocabulary and grammatical rules for instructing a computer to perform tasks.

**2. A language that is interpreted directly in the hardware using binary code is known as:**
- A. Assembly Language
- B. Machine Language
- C. High-Level Language
- D. Symbolic Language

**Answer: B.** Machine language consists of binary 0s and 1s and is the only language the CPU hardware understands directly without translation.

**3. The short alphabetical codes used in Assembly Language, such as ADD and SUB, are called:**
- A. Mnemonics
- B. Compilers
- C. Wrappers
- D. Pseudocodes

**Answer: A.** Mnemonics are the symbolic letter codes used in Assembly Language to represent machine code instructions.

**4. Which of the following is a major advantage of High-Level Languages?**
- A. They are machine dependent
- B. They execute faster than Machine Language
- C. They are machine independent
- D. They do not require translation

**Answer: C.** The primary advantage of high-level languages is that they are machine independent (portable), meaning they can run on different types of computers.

**5. Which of the following languages requires an Assembler to translate its code?**
- A. BASIC
- B. Machine Language
- C. Python
- D. Assembly Language

**Answer: D.** Assembly language uses an Assembler to translate its mnemonics into machine code. High-level languages like Python and BASIC use compilers or interpreters. 

**6. The JAMB syllabus refers to Assembly Language as a "thin wrapper" over what?**
- A. High-Level Language
- B. Machine Language
- C. System Software
- D. Java

**Answer: B.** Assembly language is a thin wrapper over machine language, meaning each assembly mnemonic matches up directly with one binary machine code instruction.

**7. Which of the following is NOT an example of a High-Level Language?**
- A. Fortran 2008
- B. Machine code
- C. Pearl (Perl)
- D. Java

**Answer: B.** Machine code is a low-level (first-generation) language. The others are high-level languages listed in the JAMB syllabus.

**8. What is the main disadvantage of Machine Language?**
- A. It is very slow to execute
- B. It cannot interact directly with the hardware
- C. It is highly error-prone and difficult for humans to write
- D. It requires a lot of system memory to translate

**Answer: C.** Writing code in thousands of 0s and 1s is extremely difficult, tedious, and easy to mess up for human programmers. (Option A is wrong because machine code is actually the fastest to execute).

**9. Why do High-Level Languages typically execute slower than Low-Level Languages?**
- A. Because they are older than machine language
- B. Because they must be translated into machine code before the hardware can understand them
- C. Because they use short mnemonics
- D. Because they are machine dependent

**Answer: B.** The CPU cannot understand English words. High-level code must be translated by a compiler or interpreter into binary, and this translation step slows down execution time.

**10. If a programmer writes software for a bank and wants the exact same code to run on a Windows PC, an Apple Mac, and a Linux server, they should use a:**
- A. Machine Language
- B. High-Level Language
- C. First-Generation Language
- D. Assembly Language

**Answer: B.** High-Level Languages are machine independent, meaning they are portable and can run on different operating systems and CPU types without needing to be completely rewritten.

<!-- COVERAGE
obj i | ## What is a Programming Language?
obj ii | ## Classification of Programming Languages
obj iii | ## Advantages and Disadvantages of Different Levels of PL
item a | ## What is a Programming Language?
item a | ## Classification of Programming Languages
item b | ## Advantages and Disadvantages of Different Levels of PL
-->
