# JAMB Computer Studies Notes: System Development Life Cycle (SDLC)

## What JAMB expects

This topic is Section G, Topic 6 of the JAMB Computer Studies syllabus: System Development Life Cycle (SDLC). It covers the structured process used by computer professionals to build software and computer systems.

**THIS FILE COVERS:**
* **(a)** Definition of SDCL
* **(b)** Stages of SDLC

By the end of these notes, you should be able to:
* i. Define SDLC
* ii. Describe SDLC
* iii. Explain stages in SDLC
    - Preliminary study (Identification of the problem, Recognition of the Need)
    - Feasibility
    - Analysis
    - Design
    - Implementation (coding, testing, documentation and delivery)
    - Maintenance
    - Review
* iv. Draw diagram of a SDLC

**Note on the syllabus wording:** In the official syllabus content list, the acronym is printed once as "SDCL" (System Development Life Cycle), which is a typing error for **SDLC**. The objectives list it correctly as SDLC. Secondly, the syllabus places "Review" as the final stage after "Maintenance". While many textbooks put the review stage right after implementation (or treat them as ongoing together), we will follow the exact order and naming given in the syllabus.

---

## Definition of SDLC

**Objective i: Define SDLC**
**Content a: Definition of SDCL**

The **System Development Life Cycle (SDLC)** is a structured, step-by-step process used by software engineers and systems analysts to plan, design, develop, test, and deploy high-quality software or computer systems. 

It is called a "life cycle" because, just like a living organism, a software system is born (planned and created), grows and works (is used and maintained), and eventually dies (is replaced by a newer system, starting the cycle all over again).

## Describe SDLC

**Objective ii: Describe SDLC**

The SDLC provides a clear framework for building a system. Without a clear plan, programmers might build a system that is full of errors, costs too much money, or does not do what the users actually need. 

**Why do we use the SDLC?**
1. **To reduce risk:** It prevents the failure of large projects by breaking them down into manageable phases.
2. **To control costs and time:** It helps predict how much money and time the new system will take to build.
3. **To ensure quality:** By having dedicated stages for testing and review, the final system is much more reliable.

**Who uses the SDLC?**
A team of professionals uses the SDLC. The most important person in this process is the **Systems Analyst**. The systems analyst is the professional who studies the problems of the current system, designs the new one, and guides the programmers who write the code. 

*Example:* Imagine a large Nigerian secondary school that currently records all student fees in paper notebooks. The notebooks get torn, calculations are often wrong, and finding a student's payment history takes hours. If the school hires a software team to build a computerized "School Fee Management System," the team will use the SDLC to guide their work from start to finish.

---

## Stages of SDLC

**Objective iii: Explain stages in SDLC**
**Content b: Stages of SDLC**

The JAMB syllabus lists seven specific stages of the SDLC. They must be followed in a logical sequence. 

### 1. Preliminary study (Identification of the problem, Recognition of the Need)
Before any real work begins, a problem must be recognized. This stage is also known as problem identification. 
* **Recognition of the need:** The users or management realize that the current way of doing things (the old system) is failing, too slow, or too expensive.
* **Identification of the problem:** The systems analyst briefly looks at the current situation to define exactly what is wrong.
* *Example:* The school principal recognizes the need for a new system because the paper notebooks are causing the school to lose money and time. The core problem is identified: "Manual fee tracking is inefficient and insecure."

### 2. Feasibility
Once the problem is identified, the team must decide if building a new system is actually possible and worth the effort. This is called a **Feasibility Study**. A feasibility report usually checks several areas:
* **Technical Feasibility:** Does the technology exist to build this? Does the school have computers and electricity (or a generator/solar setup) to run the software?
* **Economic Feasibility:** Can the organization afford it? Will the benefits of the new system (saving time, stopping theft) outweigh the cost of building it?
* **Operational Feasibility:** Will the staff actually use it? Are the bursary staff willing to learn how to use a computer?
* **Schedule Feasibility:** Can the system be built in the time required (e.g., before the next school term begins)?

If the project is deemed feasible, management gives the "go-ahead" to proceed to the next stage.

### 3. Analysis
In the analysis stage, the systems analyst conducts a detailed investigation into how the current system works and what the new system must do. This is about gathering **requirements**.
The analyst gathers facts using several methods:
* **Interviews:** Talking directly to the staff (e.g., the school bursar) to ask what features they need.
* **Questionnaires:** Handing out printed forms to many users to gather their opinions quickly.
* **Observation:** Watching the staff do their work to see where the delays happen.
* **Document review:** Examining the current paper receipts and ledgers.

The output of this stage is a document called the **System Requirements Specification**, which clearly states *what* the new system will do, but not exactly *how* it will do it.

### 4. Design
If Analysis is about *what* the system will do, Design is about *how* it will do it. In this stage, the analysts and designers create the blueprint for the new system.
* **User Interface Design:** Drawing how the screens, buttons, and menus will look.
* **Database Design:** Planning how the data (student names, payment amounts, dates) will be stored and linked together.
* **Process Design:** Using tools like **Flowcharts** and **Algorithms** to plan the logic of the system (see `G3-algorithm-and-flowcharts.md`). 
No actual programming happens here; it is purely planning and creating diagrams.

### 5. Implementation (coding, testing, documentation and delivery)
This is the stage where the system is actually built and put into use. The syllabus breaks implementation into four clear parts:

1. **Coding:** Programmers take the design documents and write the actual computer instructions using a programming language (like Python, Java, or C++). 
2. **Testing:** The new system is run to find and fix errors (known as **bugs**). 
   * *Unit testing:* Testing individual parts of the code.
   * *System testing:* Testing the whole system together.
   * *User Acceptance Testing (UAT):* Letting the actual users try it to make sure it meets their needs.
3. **Documentation:** Writing manuals. This includes **User Manuals** (how to use the software) and **Technical Documentation** (how the code works, for future programmers).
4. **Delivery (Deployment):** Installing the new system for the users. There are four common methods to change over from the old system to the new one:
   * **Direct changeover:** The old system is thrown away and the new one is started immediately. (Risky, but cheap).
   * **Parallel running:** Both the old paper system and the new computer system are used at the same time until the new one is trusted. (Safest, but expensive and double the work).
   * **Phased implementation:** The system is introduced in stages (e.g., JSS classes first, then SSS classes later).
   * **Pilot running:** The new system is tried out in just one small part of the organization (e.g., only in the primary school section) before spreading it everywhere.

### 6. Maintenance
Once the system is delivered and being used, it enters the maintenance phase. This is the longest phase of the SDLC. Software needs to be updated over time. 
* **Corrective maintenance:** Fixing bugs that were not caught during testing.
* **Adaptive maintenance:** Updating the software to work with new technology (like a new version of Windows).
* **Perfective maintenance:** Adding new features that the users ask for over time.

### 7. Review
The syllabus lists "Review" as the final stage. This involves evaluating the system after it has been running for a while (often called a Post-Implementation Review). 
* The team checks if the system actually solved the original problem.
* They assess if the project stayed within its budget and time limits.
* If major new problems are found during the review, it might trigger a "Recognition of a Need", and the life cycle begins all over again.

---

## Diagram of a SDLC

**Objective iv: Draw diagram of a SDLC**

A standard SDLC diagram is usually drawn as a cycle (a circle) or as a "Waterfall" (steps going downwards, with arrows returning to the top), showing that the process is continuous. 

[IMAGE: A circular flowchart representing the System Development Life Cycle (SDLC). The circle is made of seven curved arrows pointing clockwise to show continuous flow. The steps are clearly labeled in the syllabus order: 1. Preliminary Study, 2. Feasibility, 3. Analysis, 4. Design, 5. Implementation, 6. Maintenance, 7. Review. An arrow should point from Review back to Preliminary Study to complete the cycle. Clean flat textbook illustration, white background, using professional blue and green colors.]

---

## Key terms

| Term | Meaning |
| --- | --- |
| **SDLC** | System Development Life Cycle; the step-by-step process used to develop computer systems. |
| **Systems Analyst** | The IT professional responsible for analyzing, designing, and managing the development of the system. |
| **Preliminary Study** | The first stage where the problem is identified and the need for a new system is recognized. |
| **Feasibility Study** | Evaluating whether the proposed system is technically, economically, and operationally possible. |
| **Analysis** | Gathering detailed requirements from users via interviews, questionnaires, and observation. |
| **Design** | Planning how the system will work using flowcharts, algorithms, and interface layouts. |
| **Coding** | Writing the actual program instructions in a programming language. |
| **Testing** | Finding and fixing errors (bugs) before the system is given to users. |
| **Parallel Running** | A delivery method where the old system and new system are operated side-by-side for a period of time. |
| **Maintenance** | The ongoing process of fixing bugs and updating the system after it has been delivered. |

---

## Exam tips and common mistakes

* **Order of stages:** You must know the exact order. Memorize it: **P**reliminary -> **F**easibility -> **A**nalysis -> **D**esign -> **I**mplementation -> **M**aintenance -> **R**eview. (PFADIMR).
* **Analysis vs. Design:** A very common mistake is confusing these two. *Analysis* involves fact-finding (interviews, questionnaires) to find out what is needed. *Design* involves drawing flowcharts and planning how to build it.
* **Implementation breakdown:** Remember that JAMB groups Coding, Testing, Documentation, and Delivery all under the "Implementation" stage. If a question asks which stage involves writing a user manual, the answer is Implementation.
* **Delivery methods:** JAMB loves asking about changeover methods. If they mention running both systems to avoid risk, it's **Parallel**. If they mention stopping the old one and starting the new one suddenly, it's **Direct**.
* **Systems Analyst role:** Remember that the Systems Analyst does the studying and designing, while the *Programmer* does the coding. 

---

## Quick summary

1. The System Development Life Cycle (SDLC) is a structured approach used to build, maintain, and replace computer systems.
2. The **Preliminary Study** stage identifies the core problem and recognizes the need for a new solution.
3. The **Feasibility** stage determines if the project is possible technically, financially, and practically.
4. The **Analysis** stage involves gathering facts using tools like interviews and questionnaires to define system requirements.
5. The **Design** stage plans the user interface, database, and logic (using flowcharts/algorithms).
6. **Implementation** involves writing the code, testing for bugs, writing documentation, and delivering the system to users (using methods like direct or parallel changeover).
7. **Maintenance** involves fixing future bugs and updating the system, while the **Review** evaluates the system's overall success, completing the cycle.

---

## Practice questions

**1. The stage in the System Development Life Cycle where the problem is first identified and the need for a new system is recognized is called:**
- A. Analysis
- B. Feasibility
- C. Preliminary study
- D. Review

**Answer: C.** Preliminary study is the very first stage where the current problem is identified and the need for a solution is recognized.

**2. Which of the following is NOT a method used to gather facts during the Analysis stage?**
- A. Interviews
- B. Coding
- C. Questionnaires
- D. Observation

**Answer: B.** Coding is part of the Implementation stage, not the Analysis stage. Interviews, questionnaires, and observation are fact-finding techniques used in Analysis.

**3. The study conducted to determine if a proposed system is worth the cost and can be built with available technology is the:**
- A. Implementation study
- B. Feasibility study
- C. Maintenance study
- D. Preliminary study

**Answer: B.** The Feasibility study determines if the project is technically, economically, and operationally possible.

**4. According to the JAMB syllabus, which of the following activities is part of the Implementation stage?**
- A. Identifying the problem
- B. Testing the software
- C. Conducting interviews
- D. Drawing flowcharts

**Answer: B.** The syllabus explicitly lists coding, testing, documentation, and delivery as the components of the Implementation stage. Drawing flowcharts belongs to Design.

**5. A delivery strategy where the old manual system and the new computerized system are used at the same time to ensure the new one works correctly is known as:**
- A. Direct changeover
- B. Parallel running
- C. Phased implementation
- D. Pilot running

**Answer: B.** Parallel running involves running both systems simultaneously. If the new system fails, the organization can still rely on the old one.

**6. Which computer professional is primarily responsible for investigating the old system and designing the new one?**
- A. Programmer
- B. Database Administrator
- C. Network Engineer
- D. Systems Analyst

**Answer: D.** The Systems Analyst is the lead professional responsible for analyzing requirements and designing the system throughout the SDLC.

**7. In the SDLC, writing the user manual and technical guides falls under:**
- A. Analysis
- B. Design
- C. Implementation
- D. Review

**Answer: C.** Documentation (writing manuals) is explicitly grouped under the Implementation stage (coding, testing, documentation, and delivery).

**8. Which of the following shows the correct sequence of the first four stages of the SDLC?**
- A. Analysis -> Design -> Preliminary study -> Feasibility
- B. Preliminary study -> Feasibility -> Analysis -> Design
- C. Feasibility -> Preliminary study -> Design -> Analysis
- D. Preliminary study -> Analysis -> Feasibility -> Design

**Answer: B.** The correct syllabus order is Preliminary study -> Feasibility -> Analysis -> Design -> Implementation -> Maintenance -> Review.

**9. The longest phase in the System Development Life Cycle, which involves fixing hidden bugs and updating the system over many years, is:**
- A. Maintenance
- B. Implementation
- C. Review
- D. Feasibility

**Answer: A.** Maintenance is the ongoing phase that happens after delivery to ensure the software continues to work properly over its lifetime. 

**10. What is the main purpose of the Design stage in the SDLC?**
- A. To gather user requirements using questionnaires
- B. To write the actual program code in Python
- C. To evaluate if the project stayed within budget
- D. To create blueprints, flowcharts, and interface layouts for the new system

**Answer: D.** The Design stage focuses on "how" the system will work by creating blueprints, flowcharts, and database structures. Gathering requirements is Analysis, writing code is Implementation, and evaluating budget is Review.

<!-- COVERAGE
obj i | Definition of SDLC
obj ii | Describe SDLC
obj iii | Stages of SDLC
obj iv | Diagram of a SDLC
item a | Definition of SDLC
item b | Stages of SDLC
-->
