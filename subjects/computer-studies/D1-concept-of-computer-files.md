# JAMB Computer Studies Notes: Concept of Computer Files

## What JAMB expects

This topic is Section D, Topic 1 of the JAMB Computer Studies syllabus: Concept of Computer Files. It covers the following content items:

* (a) Definitions of basic terms
* (b) File organisations
* (c) Methods of accessing files
* (d) File classifications
* (e) Criteria for classifying files

By the end of these notes, you should be able to:

1. Define some basic terms (File, record, field, data item etc.).
2. Identify and use of basic data types (numeric, alphabetic, and alphanumeric).
3. Explain the relationship among file structure items (Data item – field - record-file-database).
4. Classify files according to how they are organised. (Serial, Sequential, Index and random).
5. Access files as appropriate (Serial, Sequential and Random).
6. Classify files into: Master, Transaction, Reference.
7. Explain the criteria used in classifying files (Nature of content, Organization method, Storage medium, Date, Size, etc.).

## Definitions of basic terms

**Objective 1: Define some basic terms (File, record, field, data item etc.).**

To understand how a computer stores and organises data, you need to know the basic terms that make up the filing system. Think of a computer file like a filing cabinet in a school principal's office, where every student has a folder, and every folder has a form with their details.

* **Data item:** This is the smallest unit of meaningful information. It is the actual value or specific piece of data entered into the system. For example, "Adebayo", "15", or "Science" are data items.
* **Field:** A field is a specific, reserved space or column meant to hold a particular type of data item. Using the school example, "First Name", "Age", and "Department" are fields.
* **Record:** A record is a complete collection of related fields treated as a single unit. It contains all the data about one specific person, thing, or event. For example, all the details (Name: Adebayo, Age: 15, Department: Science) make up one student's record.
* **File:** A computer file is a collection of related records stored together on a storage medium (like a hard drive or flash drive) under a single name. For example, a "Students_2024" file would contain the records of all the students in the school.
* **Database:** A database is a large collection of interrelated files stored together. For example, a school's database might contain a "Students" file, a "Teachers" file, and a "Fees" file, all linked together.

## Basic data types

**Objective 2: Identify and use of basic data types (numeric, alphabetic, and alphanumeric).**

When creating a field in a file, you must tell the computer what type of data is allowed in that space. This prevents mistakes, like someone typing a name into a phone number box.

The three basic data types are:

1. **Alphabetic:** This data type only allows letters of the alphabet (A to Z, both uppercase and lowercase) and sometimes spaces. No numbers or special symbols are allowed.
   * *Examples:* A person's name (Chukwuemeka), a city (Lagos), a country (Nigeria).
2. **Numeric:** This data type only allows numbers (0 to 9) and a decimal point. Numeric data is used for items that you might want to use in mathematical calculations (like addition or finding an average).
   * *Examples:* Age (17), Quantity (50), Price (₦1500.50). 
   * *Note:* A phone number like 08012345678 is usually NOT saved as a numeric data type because we do not perform maths (like multiplying phone numbers) on it, and saving it as a number would remove the leading zero.
3. **Alphanumeric:** This data type allows a mixture of alphabetic letters, numeric digits, and special characters (like @, #, -, /). It is the most flexible data type.
   * *Examples:* A JAMB registration number (2024123456AB), a home address (Plot 14, Awolowo Road), a password (Nig@2024!), an email address.

## Relationship among file structure items

**Objective 3: Explain the relationship among file structure items (Data item – field - record-file-database).**

The items in a computer file structure are related in a strict hierarchy, building from the smallest unit up to the largest, just like letters build words, words build sentences, and sentences build books.

1. **Character:** (The absolute smallest unit—a single letter, number, or symbol like 'A' or '7').
2. **Data item:** A group of characters forms a data item (e.g., "Musa").
3. **Field:** A data item is stored in a field (e.g., the "First Name" field).
4. **Record:** A group of related fields forms a record (e.g., Musa's complete student profile).
5. **File:** A group of related records forms a file (e.g., all the profiles of SS3 students).
6. **Database:** A group of related files forms a database (e.g., the complete school system containing student files, staff files, and library files).

[IMAGE: A pyramid diagram showing the file structure hierarchy. The bottom and widest block is labelled "Character (e.g., 'M')". The next level up is "Data Item (e.g., 'Musa')". Above that is "Field (e.g., 'First Name')". Above that is "Record (e.g., 'Musa, 17, SS3')". Above that is "File (e.g., 'SS3_Students.txt')". The top and narrowest block is "Database (e.g., 'School_System')". Clean flat textbook illustration, white background.]

## File organisations

**Objective 4: Classify files according to how they are organised. (Serial, Sequential, Index and random).**

**File organisation** refers to the physical way records are arranged and stored on a storage medium. How you organise a file depends on how you plan to use it later.

1. **Serial Organisation:**
   * Records are stored one after the other in the exact order they are received or entered into the computer. 
   * There is no sorting and no logical order (like alphabetical or numerical order).
   * *Example:* A shop's daily sales log book. If a customer buys garri at 8:00 AM, it is recorded first. If another buys rice at 8:05 AM, it is recorded second. 
2. **Sequential Organisation:**
   * Records are stored one after the other, but they are **sorted** in a specific logical order based on a "key field" (like alphabetical order by Name, or numerical order by ID number).
   * *Example:* A school attendance register where students' names are arranged alphabetically from A to Z.
3. **Index (Indexed Sequential) Organisation:**
   * Records are stored sequentially (sorted), but the computer also creates a separate **index** file.
   * This index works exactly like the index at the back of a textbook: it lists the key fields and gives the exact storage address (location) of each record.
   * *Note on the syllabus wording:* The syllabus lists this simply as "Index". In most textbooks, the full name is **Indexed Sequential** organisation.
4. **Random (Direct) Organisation:**
   * Records are not stored in any particular order. Instead, the computer uses a mathematical formula (called a hashing algorithm) on the record's key field to calculate the exact physical address where the record will be stored on the disk.
   * The records are scattered across the storage medium, but the computer knows exactly where to find each one instantly.

## Methods of accessing files

**Objective 5: Access files as appropriate (Serial, Sequential and Random).**

While file *organisation* is about how data is packed away, file **access** is about how the computer retrieves or reads the data when you need it. 

1. **Serial Access:**
   * To find a specific record, the computer must start at the very first record and read every single one until it finds the required data.
   * If the record you want is the 500th one, the computer must read records 1 to 499 first.
   * It is very slow for searching but good if you need to process every single record (e.g., printing monthly bank statements for all customers). Magnetic tapes use serial access.
2. **Sequential Access:**
   * Very similar to serial access, the computer reads records one by one in order. 
   * Because the file is sorted (sequential organisation), the computer knows when to stop searching. For instance, if you are looking for "Bello" and you reach records starting with "C", the computer knows "Bello" is missing and stops searching.
3. **Random (Direct) Access:**
   * The computer can jump directly to the exact location of the required record without having to read any of the preceding records.
   * This is extremely fast. It is used in systems where speed is critical, like an ATM transaction or checking a JAMB result online. Hard Disk Drives (HDDs), flash drives, and CDs support random access.

| Feature | Serial / Sequential Access | Random (Direct) Access |
| :--- | :--- | :--- |
| **Method** | Reads records one by one from the beginning. | Jumps directly to the needed record. |
| **Speed** | Slow, especially if the record is at the end. | Very fast, almost instant. |
| **Best used for** | Processing all records at once (e.g., payroll). | Finding a single specific record quickly (e.g., ATM balance inquiry). |
| **Storage Medium** | Magnetic tapes. | Hard disks, Flash drives, SSDs. |

## File classifications

**Objective 6: Classify files into: Master, Transaction, Reference.**

In a business or processing environment, files are classified by the role they play in the system.

### 1. Master file
A master file contains permanent or semi-permanent records about an organisation's main subjects (like customers, employees, or products). It is the most important file in a system and is kept up to date.
* *Characteristics:* Data here rarely changes completely, though it gets updated periodically.
* *Examples:* A bank's customer account file (containing account numbers, names, and current balances); a school's main student registry.

### 2. Transaction file
A transaction file contains temporary data about daily activities or events that have just happened. It is used to update the master file.
* *Characteristics:* It changes constantly and is usually cleared out or archived after the master file is updated.
* *Examples:* A daily record of all cash deposits and withdrawals at a bank branch. At the end of the day, these transactions are processed to update the balances in the Master file.

### 3. Reference file
A reference file (also called a table file) contains static (unchanging) data that is used for lookup purposes by other programs.
* *Characteristics:* The data inside is used for reference but is almost never altered by daily processing.
* *Examples:* A supermarket's price list (where the barcode scans and looks up the price); a table of tax rates used to calculate employee salaries; a list of Nigerian states and their capital cities.

## Criteria for classifying files

**Objective 7: Explain the criteria used in classifying files (Nature of content, Organization method, Storage medium, Date, Size, etc.).**

Files can be grouped or classified in several different ways depending on what aspect of the file you are looking at.

1. **By Nature of Content (Program and Data):**
   * **Program Files:** These contain instructions that tell the computer what to do. They are usually written by programmers and cannot be read like normal text. *Examples:* Software applications like Microsoft Word, game files, files ending in `.exe` or `.com`.
   * **Data Files:** These contain the actual work, text, or media created by the user. *Examples:* A typed letter (`.docx`), a photograph (`.jpg`), or a downloaded JAMB syllabus (`.pdf`).
2. **By Organization Method:**
   * Files can be classified by how their records are physically arranged inside them: Serial, Sequential, Indexed, or Random files (as explained in the "File organisations" section).
3. **By Storage Medium:**
   * Files are often classified by the physical device holding them.
   * *Tape files:* Stored on magnetic tape (must be accessed serially).
   * *Disk files:* Stored on Hard Disks or Floppy Disks (can be accessed randomly).
   * *Optical files:* Stored on CDs or DVDs.
4. **By Date:**
   * Files are classified by their timestamp (when they were made). 
   * **Creation date:** The exact day and time the file was first made.
   * **Modification date:** The date the file was last opened and edited. System administrators use these dates to know which files to backup (e.g., "only backup files modified today").
5. **By Size:**
   * Files can be classified by how much storage space they consume, measured in Bytes, Kilobytes (KB), Megabytes (MB), or Gigabytes (GB). 
   * For example, text files are generally small (a few KBs), while video files are very large (several GBs).

## Key terms

| Term | Meaning |
| :--- | :--- |
| **Data item** | The specific value stored in a field (e.g., "Aisha", "14"). |
| **Field** | A space in a record reserved for a specific piece of data. |
| **Record** | A collection of related fields treated as one unit (a complete profile). |
| **File** | A collection of related records stored together. |
| **Database** | A large collection of related files. |
| **Serial organisation** | Records stored in the order they arrive, with no sorting. |
| **Sequential organisation** | Records stored one after the other in a sorted, logical order. |
| **Random access** | A method of jumping directly to a record without reading previous ones. |
| **Master file** | A permanent file containing the main updated records of an organisation. |
| **Transaction file** | A temporary file containing daily activities used to update a master file. |
| **Reference file** | A file containing static, unchanging data used for lookups (e.g., price list). |
| **Alphanumeric** | A data type that allows letters, numbers, and special symbols. |

## Exam tips and common mistakes

* **Confusing Field and Record:** Remember that a *Field* is just one column (e.g., Age), while a *Record* is an entire row (e.g., Name, Age, and Class all together).
* **Alphanumeric vs Numeric:** Just because data contains numbers doesn't make it "Numeric". If it contains a mixture (like a house address "Plot 12") or if it's a number we don't do maths on (like a phone number), it is usually treated as Alphanumeric or Text.
* **Organisation vs Access:** "Organisation" is how data is *packed* on the disk. "Access" is how the computer *reads* it. You can have a sequentially organised file, but access it randomly if it's on a hard drive.
* **Master vs Transaction:** A common exam question compares these two. The master is the *permanent* main book, while the transaction is the *temporary* rough work used to update the master.
* **Magnetic Tape:** If a question mentions magnetic tape, the access method is *always* Serial.

## Quick summary

1. The file structure hierarchy goes from smallest to largest: Character → Data Item → Field → Record → File → Database.
2. The three basic data types are numeric (numbers only), alphabetic (letters only), and alphanumeric (letters, numbers, and symbols).
3. Files can be organised in four ways: Serial (order of arrival), Sequential (sorted order), Indexed (sorted with an index for fast searching), and Random (scattered but directly calculable).
4. Files can be accessed serially (one by one from the start) or randomly (jumping directly to the record).
5. A master file holds permanent, updated data; a transaction file holds temporary daily data; a reference file holds static lookup data.
6. Files can be classified based on the nature of their content into Program files (instructions like `.exe`) and Data files (user documents like `.docx`).
7. Other criteria for classifying files include their storage medium, the date they were created or modified, and their overall size.

## Practice questions

**1. Which of the following shows the correct hierarchy of file structure items from smallest to largest?**
- A. Field → Data item → Record → File → Database
- B. Data item → Field → Record → File → Database
- C. Record → Field → Data item → Database → File
- D. File → Record → Field → Data item → Database

**Answer: B.** The smallest meaningful unit is the data item, which fits into a field, a group of fields makes a record, records make a file, and files make a database.

**2. A student's residential address like "15, Awolowo Way, Ikeja" is best stored using which data type?**
- A. Numeric
- B. Alphabetic
- C. Alphanumeric
- D. Floating point

**Answer: C.** The address contains a mixture of numbers (15), letters (Awolowo Way, Ikeja), and special characters (commas), making it alphanumeric. 

**3. In a banking system, the file that contains the current balances of all customers and is permanent in nature is the:**
- A. Transaction file
- B. Reference file
- C. Master file
- D. Program file

**Answer: C.** The master file contains permanent or semi-permanent records (like customer accounts) that are updated periodically.

**4. A file organisation method where records are stored one after the other in the exact order they were collected, without any sorting, is known as:**
- A. Sequential organisation
- B. Serial organisation
- C. Random organisation
- D. Indexed organisation

**Answer: B.** Serial organisation stores records strictly in the order they arrive, unlike sequential which sorts them.

**5. Which of the following storage media strictly uses serial access?**
- A. Hard Disk Drive (HDD)
- B. Flash drive
- C. Magnetic tape
- D. Compact Disc (CD)

**Answer: C.** Magnetic tape works like an old cassette tape; the computer must roll through all preceding data to find a specific record, which is serial access.

**6. The primary purpose of a transaction file is to:**
- A. Store static data like tax rates
- B. Keep a permanent record of all employees
- C. Hold temporary data used to update the master file
- D. Contain instructions for the computer hardware

**Answer: C.** A transaction file collects daily events (like bank deposits) temporarily so they can be processed to update the permanent master file.

**7. Which of the following is an example of classifying a file based on its "Nature of Content"?**
- A. Differentiating between a 1MB file and a 2GB file
- B. Differentiating between a Program file and a Data file
- C. Differentiating between a Tape file and a Disk file
- D. Differentiating between a Master file and a Transaction file

**Answer: B.** "Nature of content" classifies files into Program files (instructions/software) and Data files (user-created documents).

**8. If a system requires extremely fast, instant access to a specific record without reading any other records, the best access method is:**
- A. Serial access
- B. Sequential access
- C. Indexed sequential access
- D. Random (Direct) access

**Answer: D.** Random (or direct) access jumps directly to the exact location of the record, making it the fastest method for finding single items.

**9. An area in a record reserved to hold a specific type of data item, such as a student's "Date of Birth", is called a:**
- A. File
- B. Field
- C. Database
- D. Directory

**Answer: B.** A field is the specific column or space designated to hold one particular piece of information in a record.

**10. A supermarket's barcode system uses a file containing prices of goods. The prices rarely change and are used only for looking up the cost of an item. This file is best described as a:**
- A. Transaction file
- B. Reference file
- C. Sequential file
- D. Program file

**Answer: B.** A reference file (or table file) contains static, lookup data such as a price list or tax rates.

<!-- COVERAGE
obj i | Definitions of basic terms
obj ii | Basic data types
obj iii | Relationship among file structure items
obj i | File organisations
obj ii | Methods of accessing files
obj iii | File classifications
obj iv | Criteria for classifying files
item a | Definitions of basic terms
item b | File organisations
item c | Methods of accessing files
item d | File classifications
item e | Criteria for classifying files
-->
