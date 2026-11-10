# JAMB Computer Studies Notes: Database Package

## What JAMB expects

This topic covers Section C, Topic 3 of the JAMB Computer Studies syllabus: Database Package.

It covers the following content items:
- **a.** Definition of Database and examples of database packages
- **b.** Database organizations
- **c.** Different features of database format
- **d.** Basic operations of Database using MS Access
- **e.** Create database using MS Access
- **f.** Carry out operations on existing database using MS Access

By the end of these notes, you should be able to:
1. Define Database and give examples of Database packages (Dbase, Foxbase, MS Access, Oracle, etc.).
2. Define basic database terms (File, Record, Field, key, form, table, etc.).
3. List and explain different types of database organisation (Hierarchical, Network, and Relational).
4. List the application areas of Database in different organizations (Office, Home, Education, Government, Hospital, Agriculture, etc.).
5. Explain different features of database format in MS Access (files designed as tables, rows, columns, etc.).
6. Carry out steps to create a database in MS Access (define structure, indicate field type, enter and save data).
7. Carry out basic operations on an already created MS Access database (searching, modifying, sorting, reporting, etc.).
8. Close the MS Access database.

---

## What is a database and examples of packages?

A **database** is an organized, structured collection of related data stored on a computer. It is designed so that data can be easily accessed, managed, updated, and searched. You can think of a database as a highly efficient electronic filing cabinet. 

Software used to create, manage, and interact with databases is called a **Database Management System (DBMS)**, often simply referred to as a **database package**.

Common examples of database packages include:
- **MS Access (Microsoft Access):** A popular relational database package included in the Microsoft Office suite, widely used for personal and small business databases.
- **Oracle:** A powerful, large-scale database system used by massive corporations, banks, and governments to handle huge amounts of data securely.
- **MySQL and SQL Server:** Modern, heavily used database systems for running websites and online applications.
- **Dbase and Foxbase:** These were some of the earliest database packages used on older personal computers.

**Note on the syllabus wording:** The syllabus names *Dbase* and *Foxbase* as examples. While these programs are now obsolete and no longer used in modern computing, you must remember them because they are specifically listed in the JAMB syllabus and often appear in exam questions.

## Basic database terms

To understand how a database works, you must know its basic building blocks:

- **Table (or File):** A collection of all the related records about a specific subject. For example, a school database might have a "Students" table and a "Teachers" table. In older, non-relational systems, a table was often called a **File**.
- **Record (Row):** A complete set of information about a single entity (one person, one item, or one event). For example, a single row containing the ID, name, age, and class of the student *Amina* is one record.
- **Field (Column):** A single attribute or piece of information within a record. For example, the "First Name" column or the "Date of Birth" column. 
- **Key (Primary Key):** A special field that uniquely identifies each record in a table. No two records can have the same primary key. For example, a JAMB Registration Number or a student's Admission Number is a primary key, because no two students share the same number. A surname cannot be a primary key because two students might share it.
- **Form:** A graphical, user-friendly interface designed for entering, editing, or viewing one record at a time. It hides the complexity of the large table from the user.
- **Query:** A request to search for and retrieve specific data that meets certain conditions. For example, a query might ask the database to "Show me all students who scored above 250."
- **Report:** A formatted, professional-looking presentation of data extracted from tables or queries, designed specifically to be printed or shared as a document.

## Database organizations

Database organization (or a database model) describes how data is logically structured and linked together inside the system. There are three main types:

### 1. Hierarchical
In a hierarchical database, data is organized in a top-down, **tree-like structure**. It relies on a **one-to-many** relationship, where a "parent" record can have many "child" records, but a child can only have one parent. 
*Example:* A school folder (parent) connects to classes (children), and each class connects to specific students (grandchildren). It is rigid and difficult to reorganize.

### 2. Network
The network model is similar to the hierarchical model but more flexible. It is organized in a **web-like structure** (or graph). It allows **many-to-many** relationships, meaning a "child" record can have multiple "parent" records. 
*Example:* A student can be linked to multiple different teachers, and a teacher can be linked to multiple students.

### 3. Relational
This is the most common model used today (including in MS Access and Oracle). Data is organized into independent **tables** consisting of rows and columns. Different tables can be connected (related) to each other using common fields (keys). 
*Example:* A "Students" table and an "Exam Scores" table can be linked together using the student's Admission Number.

[IMAGE: Three diagrams showing database models. 1. Hierarchical: A top-down tree structure with one parent box connecting to three child boxes. 2. Network: A web-like structure where child boxes have multiple connections to different parent boxes. 3. Relational: A table grid showing rows and columns with a key linking to another table. Clean flat textbook style, white background.]

| Feature | Hierarchical | Network | Relational |
| :--- | :--- | :--- | :--- |
| **Structure shape** | Tree-like (top-down) | Web-like (graph) | Tables (grids of rows and columns) |
| **Relationships** | One-to-many | Many-to-many | Linked via common fields (keys) |
| **Flexibility** | Rigid, hard to modify | Complex to design | Highly flexible, easy to query |

## Application areas of databases

Databases are used in almost every sector of society to keep records organized and searchable:

- **Office:** Managing employee records, processing payrolls, tracking office inventory, and storing customer contact details.
- **Home:** Personal budgeting, digital address books, and cataloguing personal collections (like tracking owned books, music, or movies).
- **Education:** Managing student admissions (like the JAMB CBT portal), storing exam results, tracking library book loans, and keeping staff records.
- **Government:** Maintaining national census data, voter registration databases (e.g., INEC), tax collection records, and issuing driver's licenses and passports.
- **Hospital:** Managing electronic patient medical records, tracking doctor appointments, monitoring blood bank stock, and controlling pharmacy drug inventory.
- **Agriculture:** Tracking farm yields and harvests over different seasons, managing livestock breeding records, and keeping track of fertiliser inventory and weather data.

## Features of database format in MS Access

Microsoft Access structures its data in a specific relational format. You must understand how this format is built:

1. **Files designed as tables:** In MS Access, the actual data is stored in objects known as tables. Even when you use forms to enter data or queries to search it, they are all interacting with the underlying tables.
2. **Tables comprising rows and columns:** When you open a table (in Datasheet View), it looks like a grid, very similar to an Excel spreadsheet, made up of intersecting horizontal rows and vertical columns.
3. **Row containing related information about a record:** Each horizontal row represents exactly one complete record. For example, a single row holds the ID, Name, Age, and Class belonging to one specific student.
4. **Column containing specific type of information about a field:** Each vertical column represents one field and holds only one specific type of data for all the records. For example, a "Date of Birth" column will contain nothing but dates for every person in the table.

[IMAGE: A Microsoft Access table in Datasheet View showing columns labelled "ID", "First Name", and "Date of Birth", and rows containing sample student data. An arrow points to a single column with the label "Field (Column)", and another arrow points to a single horizontal row with the label "Record (Row)". Clean flat textbook illustration, white background.]

## Creating a database in MS Access

Creating a new database from scratch involves a standard sequence of steps:

### 1. Define structure of a database
Launch MS Access, select "Blank Database", give your file a name, and click "Create". You then switch your view to **Design View**. In Design View, you build the table's structure by typing out the names of the fields you want (for example: `StudentID`, `FirstName`, `Surname`, `DateOfBirth`).

### 2. Indicate field type
For every field name you type, you must select a **Data Type** from a drop-down list. This tells the database what kind of information is allowed in that column. Common types include:
- **Numeric (Number):** For numbers that hold mathematical value (e.g., age, test score).
- **Character / Text (Short Text):** For letters, words, or numbers that are not calculated (e.g., names, phone numbers).
- **Date/Time:** For calendar dates (e.g., date of birth).
- **Currency:** For money values (e.g., school fees).

> **Note on the syllabus wording:** The syllabus asks you to indicate field types as "(numeric, character, **data**, text, etc.)". The word **"data"** here is a typing error in the official syllabus; it should be **"date"**. Standard database packages use a "Date/Time" field type, not a "data" field type.

### 3. Enter data
Once the structure is built and saved, you switch the table to **Datasheet View**. The field names you created become the column headers. You can now click into the empty rows and type in the real information (the records) for each person or item.

### 4. Save data
As you work, you must save the table by clicking the Save icon (the floppy disk) on the Quick Access Toolbar or pressing `Ctrl + S`. This saves the table's structure and the data entered to the computer's hard drive.

## Basic operations on an existing MS Access database

Once your database is created and populated with data, you can carry out several operations on it:

- **Inserting:** Adding a brand new record. You can do this by typing into the empty row at the bottom of a table, or by using a Form to input the new details.
- **Searching / Selecting:** Finding specific data. You can use the "Find" tool (`Ctrl + F`) to jump to a specific word (e.g., finding the name "Emeka"). For more complex searches, you use a **Query** to select only the records that meet certain conditions (e.g., "Select all students in SS3 who live in Lagos").
- **Modifying:** Editing or updating existing data. If a student's phone number changes, you locate their record, delete the old number, and type in the new one.
- **Sorting:** Arranging records in a specific, logical order to make them easier to read. You can sort names alphabetically from A to Z (Ascending) or Z to A (Descending), or sort numbers from smallest to largest.
- **Reporting:** Generating a formal document. The Report tool takes the data from your tables or queries and formats it beautifully for printing, allowing you to add page numbers, titles, and group summaries.

## Closing the MS Access database

When you are finished with your work, it is important to close the database safely so no data is corrupted.
1. Save any open tables, forms, or queries.
2. Click the **File** tab on the ribbon (or the Office Button in older versions).
3. Click **Close Database** to close the current file without shutting down the MS Access software itself.
4. Alternatively, to close the database and exit the MS Access application completely, click the **X** button at the top right of the window, or press `Alt + F4`.

---

## Key terms

| Term | Meaning |
| :--- | :--- |
| **Database** | An organized, structured collection of related data for easy access and management. |
| **DBMS** | Database Management System; the software used to manage databases (e.g., MS Access, Oracle). |
| **Table (File)** | A collection of related records, arranged in a grid of rows and columns. |
| **Record (Row)** | A complete set of information about one specific entity (e.g., all details for one student). |
| **Field (Column)** | A single attribute or specific type of data within a record (e.g., Age). |
| **Primary Key** | A unique field that identifies each record, ensuring no two records are identical. |
| **Form** | A graphical interface used for entering or viewing one record at a time. |
| **Query** | A request to search for and retrieve specific data based on rules or conditions. |
| **Report** | A formatted presentation of database data designed to be printed. |

## Exam tips and common mistakes

- **Row = Record** and **Column = Field**. JAMB frequently tests this distinction. Never mix them up.
- Know the difference between the three database models: **Hierarchical** (tree, one-to-many), **Network** (web, many-to-many), and **Relational** (tables). MS Access is relational.
- A **Primary Key** must be strictly unique (e.g., Admission Number or NIN). A person's name cannot be a primary key because two people can share the same name.
- When creating a database, you must **define the structure** (in Design View) and set **field types** *before* you can **enter data** (in Datasheet View).
- **Searching/Querying** is for finding data, while **Sorting** is for arranging data (e.g., A to Z). Do not confuse the two.
- Remember the syllabus typo: when the syllabus lists "data" as a field type, it means **Date**.

## Quick summary

1. A database is a structured collection of data. Software used to create them includes MS Access, Oracle, Dbase, Foxbase, and MySQL.
2. In a relational database, data is stored in tables consisting of rows (records) and columns (fields).
3. A record contains all related information about one entity, while a field contains one specific type of information for all entities.
4. The three main database organizations are hierarchical (tree-like), network (web-like), and relational (tables).
5. Databases are used in offices, homes, schools, government, hospitals, and agriculture for efficient record-keeping.
6. To create a database in MS Access, you define the structure, assign field data types (text, numeric, date), enter the data, and save it.
7. Basic database operations include inserting new records, modifying existing ones, sorting data, searching/querying, and generating reports.
8. A database can be safely closed by selecting "Close Database" from the File menu or closing the application window.

## Practice questions

**1. Which of the following is NOT an example of a database package?**

- A. Microsoft Access
- B. Oracle
- C. Dbase
- D. Adobe Dreamweaver

**Answer: D.** Adobe Dreamweaver is a web design package. Access, Oracle, and Dbase are examples of database management systems.

**2. In a relational database table, a single column is referred to as a**

- A. record
- B. field
- C. file
- D. primary key

**Answer: B.** A column represents a field, which contains a specific type of information for all records. A horizontal row represents a record.

**3. A school's database has a table for students. Which of the following is the most suitable field to use as a primary key?**

- A. Surname
- B. Date of Birth
- C. Admission Number
- D. State of Origin

**Answer: C.** A primary key must be unique to each record. Two students can have the same surname or date of birth, but the Admission Number is unique to one student.

**4. Which type of database organization links data in a rigid top-down, tree-like structure?**

- A. Network
- B. Relational
- C. Hierarchical
- D. Sequential

**Answer: C.** The hierarchical model organizes data like a tree with one-to-many parent-child relationships. The network model is web-like, and the relational model uses tables.

**5. What is the first step when creating a new database table in MS Access?**

- A. Entering the actual data
- B. Defining the structure and field names
- C. Sorting the records
- D. Generating a printable report

**Answer: B.** Before you can enter data, you must define the table's structure by naming the fields and setting their data types.

**6. When using MS Access, the database format ensures that a single row contains**

- A. related information about a single record
- B. specific types of information about a field
- C. all the tables in the file
- D. formatting instructions for a report

**Answer: A.** A row contains related information making up one complete record (e.g., all details for one person), while a column contains field data.

**7. An organization wants to arrange its employee records alphabetically from Z to A. Which database operation is required?**

- A. Searching
- B. Modifying
- C. Inserting
- D. Sorting

**Answer: D.** Sorting is the operation used to arrange records in a specific order (ascending or descending). Searching finds records without changing their order.

**8. The use of a database to store patient medical history and drug inventory is an application area in**

- A. Agriculture
- B. Government
- C. Hospitals
- D. Education

**Answer: C.** Hospitals use databases for patient records and medical inventory. Education uses them for student results, and agriculture for tracking crop yields.

**9. In the context of MS Access data types, the JAMB syllabus lists "data" as a type. What is the actual standard MS Access data type this refers to?**

- A. Text
- B. Numeric
- C. Date/Time
- D. Currency

**Answer: C.** "Data" is a common typing error in the syllabus for Date/Time, which is the standard field type used to store dates such as a Date of Birth.

**10. Which MS Access operation is used to present database information in a neat, formatted layout suitable for printing?**

- A. Sorting
- B. Reporting
- C. Selecting
- D. Modifying

**Answer: B.** Reporting takes data from tables or queries and formats it into a professional presentation that is ready to be printed.

<!-- COVERAGE
obj i | What is a database and examples of packages?
obj ii | Basic database terms
obj iii | Database organizations
obj iv | Application areas of databases
obj i | Features of database format in MS Access
obj ii | Creating a database in MS Access
obj iii | Basic operations on an existing MS Access database
obj iv | Closing the MS Access database
item a | What is a database and examples of packages?
item b | Database organizations
item c | Features of database format in MS Access
item d | Basic operations on an existing MS Access database
item e | Creating a database in MS Access
item f | Basic operations on an existing MS Access database
-->
