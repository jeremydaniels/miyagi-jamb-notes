# JAMB Computer Studies Notes: Computer Security

## What JAMB expects

This topic is Section I, Topic 2 of the JAMB Computer Studies syllabus: Basics and Applications of ICT – Computer Security.

By the end of these notes, you should be able to:

*   vi. Define computer security.
*   vii. Identify different types of computer security and their characteristics (Network security, Internet security (cyber), Application Security, Data security, Information security, End user security etc.).
*   viii. Identify appropriate security tools to use for the different types of computer security (Firewalls, antivirus software, encryption, etc.).
*   ix. Identify categories of application threats and their characteristics (Input, authorisation, session management, parameter tampering).
*   x. Identify basic dimensions of Information Security (Confidentiality, Integrity, and Availability (CIA)).
*   xi. Mention Network security Issues (unauthorised, intrusion, rules and configurations that protect confidentiality, integrity and accessibility using both software and hardware).
*   xii. Mention Network security methods (antivirus software, application security, behavioural analytics, data loss prevention, email security, firewalls, mobile device security, network segmentation, security and event management (SEIM), Virtual Private Network (VPN), Web security, wireless security, Network Access Control (NAC)).

**Note on the syllabus wording:** 
The syllabus contains a few typing errors that you should be aware of. 
1. In objective ix, the list of application threats ends suddenly with a comma ("...session management, parameter tampering,"), looking as if words were cut off. We will cover exactly what is printed. 
2. In objective xi, the syllabus says "unauthorised, intrusion"; this is meant to mean "unauthorised intrusion" (unapproved access by hackers). It also mentions "accessibility" alongside confidentiality and integrity; the standard industry term is "Availability" (forming the CIA triad), but JAMB sometimes uses them interchangeably. 
3. In objective xii, it lists "(SEIM)". The correct and globally used abbreviation is **SIEM** (Security Information and Event Management), though we will note the syllabus spelling. 
Finally, specific cyber risks (like malware types) are covered in the next topic, `I3-cyber-risks-and-protection.md`.

## Definition of computer security

**Objective vi: Define computer security.**

**Computer security** (also known as cybersecurity or IT security) is the practice of protecting computer systems, networks, devices, and digital data from theft, damage, unauthorised access, or malicious attacks. 

Think of a computer system like a physical bank. You need locks on the doors, a vault for the money, guards checking who comes in, and cameras watching everything. Computer security does the same thing for digital assets. It ensures that only the right people can access the information, that the information is not changed by criminals, and that the computer systems keep running when they are needed.

## Types of computer security and their characteristics

**Objective vii: Identify different types of computer security and their characteristics.**

Because modern computing is complex, security is divided into several areas, each protecting a different part of the system.

### 1. Network security
This is the practice of securing a computer network from intruders, whether they are targeted attackers (hackers) or opportunistic malware. It involves protecting the infrastructure (routers, switches, servers) so that unauthorized people cannot spy on network traffic or break into connected devices.
*   **Characteristics:** Focuses on the boundaries and the traffic inside a network (e.g., a school's computer lab network or a bank's internal network).

### 2. Internet security (cyber)
This deals with protecting systems and data specifically from threats that come from the global Internet. While network security might protect a local area network (LAN), internet security focuses on the rules and tools for safely interacting with the World Wide Web.
*   **Characteristics:** Defends against online threats like phishing, malicious websites, and downloads. It ensures browsers and web connections are safe.

### 3. Application Security
This focuses on keeping software and applications free from vulnerabilities. Hackers often try to find weaknesses in the code of software (like a banking app or the JAMB CBT software) to break in.
*   **Characteristics:** It involves writing secure code, testing software for bugs before it is released, and updating (patching) software regularly to fix newly discovered flaws.

### 4. Data security
This specifically protects the raw digital data (files, databases, records) from being stolen, corrupted, or destroyed. 
*   **Characteristics:** It heavily involves backups and encryption. If a thief steals a hard drive, data security ensures they cannot read the files on it.

### 5. Information security (InfoSec)
While data security focuses on the raw data, Information Security is a broader term that protects the *meaning* and *value* of that data, whether it is physical (like printed paper records) or digital. It ensures information is only seen by authorized people, is accurate, and is available when needed.
*   **Characteristics:** Governed by policies, laws (like Nigeria's Data Protection Act), and the CIA triad (discussed below).

### 6. End user security
This is the most critical layer because human beings are often the weakest link in computer security. End user security involves educating the people who use the computers so they do not accidentally let attackers in.
*   **Characteristics:** Focuses on training users to recognise scams (like fake emails claiming their BVN is blocked), use strong passwords, and avoid plugging in unknown USB flash drives.

## Security tools for different types of security

**Objective viii: Identify appropriate security tool to use for the different types of computer security.**

Different security domains require specific tools. Here is how they pair up:

| Type of Security | Appropriate Security Tools | How it Works |
| :--- | :--- | :--- |
| **Network Security** | **Firewalls**, Intrusion Detection Systems (IDS) | A firewall acts as a guard between a trusted internal network and the untrusted internet, blocking dangerous traffic. |
| **Internet Security** | **Web filters**, Secure Gateways, HTTPS | Blocks access to known dangerous websites and ensures data sent over the internet is hidden. |
| **Application Security** | **Patch management software**, Code scanners | Scans apps for coding mistakes and applies software updates (patches) to fix bugs. |
| **Data / Information Security** | **Encryption**, Backup drives | Encryption scrambles data into unreadable text (ciphertext). Even if stolen, it cannot be read without a secret key. |
| **End User Security** | **Antivirus software**, Multi-Factor Authentication (MFA) | Antivirus software scans a user's computer for malware. MFA requires users to provide two pieces of evidence (e.g., a password and a code sent to their phone) to log in. |

[IMAGE: A diagram showing a layered defense system: an outer wall labelled "Firewall" protecting a network, a vault labelled "Encryption" protecting data inside, and a magnifying glass labelled "Antivirus" inspecting a file on a computer. Clean flat textbook illustration, white background.]

## Categories of application threats

**Objective ix: Identify categories of application threats and their characteristics.**

Applications (like websites, school portals, and mobile apps) face specific types of attacks that try to manipulate how the software works.

### 1. Input threats (e.g., SQL Injection, Cross-Site Scripting)
Applications often ask users to type something into a box (like a username or a search query). If the application does not check this input properly, a hacker can type in malicious computer commands instead of normal text.
*   **Characteristics:** The attacker sends hostile data to trick the application into executing unintended commands. For example, typing a database command into a login box to bypass the password check (SQL Injection).

### 2. Authorisation threats
Authentication is proving *who* you are; authorisation is checking *what you are allowed to do*. Authorisation threats happen when a user accesses parts of the application they should not be allowed to see.
*   **Characteristics:** A normal user finds a way to gain "admin" or "root" privileges (Privilege Escalation), allowing them to delete other people's accounts or view restricted files.

### 3. Session management threats
When you log into a website (like an email account), the server gives your browser a temporary ID card called a "session token" or "cookie" so you do not have to type your password on every single page click.
*   **Characteristics:** If an attacker steals this session token, they can impersonate you and use your account without ever knowing your password. This is called Session Hijacking.

### 4. Parameter tampering
Many web applications pass information (parameters) in the background or in the website's URL. For example, an online store might have a hidden field saying the price of a shoe is `amount=5000`.
*   **Characteristics:** Parameter tampering involves a hacker intercepting and changing this background data before it reaches the server (for example, changing the shoe's price from 5000 to 5 before checking out).

## Basic dimensions of Information Security (The CIA Triad)

**Objective x: Identify basic dimensions of Information Security (Confidentiality, Integrity, and Availability).**

The core of all information security is a model known as the **CIA Triad**. Every security rule or tool is designed to protect one or more of these three dimensions:

1.  **Confidentiality:** 
    *   **Meaning:** Keeping information secret from people who are not supposed to see it.
    *   **Example:** When checking your JAMB result, only you (with your registration number) should see your score.
    *   **Tools used:** Passwords, biometrics (fingerprints), and encryption.
2.  **Integrity:** 
    *   **Meaning:** Ensuring that information is accurate, complete, and has not been altered or tampered with by unauthorised people.
    *   **Example:** A hacker must not be able to change an account balance from ₦2,000 to ₦20,000,000.
    *   **Tools used:** File permissions, backups, and digital signatures.
3.  **Availability:** 
    *   **Meaning:** Ensuring that systems and data are accessible to authorised users whenever they need them.
    *   *(Note: As mentioned earlier, the syllabus sometimes uses the word "accessibility" for this concept).*
    *   **Example:** A bank's ATM or mobile app must be online and working when a customer needs to transfer money.
    *   **Tools used:** Backup generators for power cuts, duplicate servers (redundancy), and protection against attacks that try to crash the server.

[IMAGE: A triangle diagram labelled "The CIA Triad". The three points of the triangle are labelled "Confidentiality (Secrecy)", "Integrity (Accuracy)", and "Availability (Accessibility)". In the centre of the triangle is a shield icon representing Information Security. Clean flat textbook illustration, white background.]

## Network security issues

**Objective xi: Mention Network security Issues.**

Managing a network involves dealing with several constant issues and configuring hardware and software to enforce the CIA triad.

*   **Unauthorised Intrusion:** This is when a hacker, malware, or an uninvited person breaks into the network. This breaks *confidentiality* and can lead to data theft.
*   **Poor Rules and Configurations:** Network devices like routers and firewalls rely on "rules" (Access Control Lists) to know what traffic to allow. If an IT administrator misconfigures these rules (e.g., accidentally leaving an administrative port open to the public internet), it creates a massive security hole.
*   **Protecting CIA using Software:** Software issues involve making sure operating systems are patched, antivirus is running, and software firewalls are active on individual computers to stop malware from spreading inside the network.
*   **Protecting CIA using Hardware:** Hardware issues involve physically securing servers (so no one can just walk away with them), using hardware firewalls at the network border, and ensuring routers are properly configured to drop bad traffic.

## Network security methods

**Objective xii: Mention Network security methods.**

To combat the issues mentioned above, network administrators use a combination of methods and tools. The syllabus specifically names the following:

1.  **Antivirus software:** Programs installed on computers and servers that scan for, detect, and remove malicious software (malware) like viruses, worms, and trojans.
2.  **Application security:** Enforcing rules that ensure only safe, approved software can run on the network, and protecting those applications from input or authorisation threats.
3.  **Behavioural analytics:** Instead of looking for known viruses, this method uses software to watch how users and devices normally behave. If an employee's computer suddenly starts downloading gigabytes of sensitive files at 2:00 AM, the system flags it as an anomaly.
4.  **Data Loss Prevention (DLP):** Software designed to ensure that sensitive information (like customer BVNs or credit card numbers) is not accidentally or maliciously sent outside the company network. It can block emails or USB transfers containing restricted data.
5.  **Email security:** Systems that filter out spam, block phishing attacks (fake emails designed to steal passwords), and scan email attachments for viruses before they reach the user's inbox.
6.  **Firewalls:** Both hardware and software barriers that monitor and control incoming and outgoing network traffic based on predetermined security rules. They are the first line of defence in network security.
7.  **Mobile device security:** Methods for protecting smartphones and tablets connected to the network, often using Mobile Device Management (MDM) software to enforce passwords or remotely wipe a lost phone.
8.  **Network segmentation:** Breaking a large network into smaller, isolated parts (subnets). For example, keeping a school's administrative network totally separate from the students' Wi-Fi network. If a student's laptop has a virus, it cannot easily spread to the admin computers.
9.  **Security and Event Management (SIEM):** *(Note: Spelled SEIM in the syllabus).* A centralized system that collects logs and alerts from all firewalls, servers, and antivirus programs in the network, allowing security teams to analyze and respond to attacks in real time.
10. **Virtual Private Network (VPN):** A tool that creates a secure, encrypted "tunnel" over the public internet. If a worker is using public Wi-Fi at a cafe, a VPN ensures their data is scrambled and safe from eavesdroppers.
11. **Web security:** Gateways and filters that block employees from visiting dangerous or malicious websites and ensure internet traffic is encrypted.
12. **Wireless security:** Protecting Wi-Fi networks using strong encryption protocols (like WPA2 or WPA3) so that unauthorized people outside the building cannot connect to the wireless network or intercept data.
13. **Network Access Control (NAC):** A system that checks any device trying to connect to the network. If a laptop does not have an updated antivirus or the right password, the NAC will block it from joining the network.

## Key terms

| Term | Meaning |
| :--- | :--- |
| **Computer Security** | The protection of computer systems and data from harm, theft, and unauthorized use. |
| **CIA Triad** | The three core principles of information security: Confidentiality, Integrity, and Availability. |
| **Confidentiality** | Ensuring that data is kept private and only seen by authorized people. |
| **Integrity** | Ensuring that data remains accurate and has not been improperly changed. |
| **Availability** | Ensuring that systems and data are accessible when authorized users need them. |
| **Firewall** | A network security tool that monitors and controls incoming and outgoing traffic based on rules. |
| **Encryption** | The process of scrambling data so it is unreadable to anyone without the decryption key. |
| **Parameter Tampering** | An application threat where a hacker alters background data (like URLs or hidden form fields) sent to a server. |
| **SIEM / SEIM** | Security Information and Event Management; a system that logs and analyzes security alerts across a network. |
| **VPN** | Virtual Private Network; an encrypted connection over the internet that protects data in transit. |
| **Network Segmentation** | Dividing a computer network into smaller subnets to improve security and control. |
| **Data Loss Prevention (DLP)** | Tools that stop sensitive data from being sent outside the network. |

## Exam tips and common mistakes

*   **Syllabus quirk alert:** Remember that JAMB might use the word **accessibility** to mean **Availability** in the CIA triad. Also, watch out for the spelling **SEIM** instead of **SIEM** in multiple-choice options.
*   **Confidentiality vs. Integrity:** A very common mistake is confusing these two. If a hacker *reads* your private message, that breaks Confidentiality. If a hacker *alters* your bank balance, that breaks Integrity. 
*   **Data vs. Information Security:** Data security usually refers to protecting the physical/raw data storage (like encrypting a hard drive), while Information security is the broader policy of keeping the meaning of that data secure (the CIA triad).
*   **Firewalls vs. Antivirus:** Firewalls control network *traffic* (like a gatekeeper), while antivirus software scans for malicious *files* (like a doctor checking for disease). Know the difference!
*   **VPN:** Always associate VPN with "encryption" or a "secure tunnel" over a public network.

## Quick summary

1.  Computer security involves protecting digital systems, networks, and data from unauthorized access, damage, or theft.
2.  Security is divided into several types, including network, internet, application, data, information, and end-user security.
3.  Application threats include input manipulation (like SQL injection), authorisation flaws, session hijacking, and parameter tampering.
4.  The CIA triad stands for Confidentiality (secrecy), Integrity (accuracy), and Availability (accessibility). It is the foundation of information security.
5.  Network security involves managing rules, configurations, hardware, and software to prevent unauthorized intrusions.
6.  Tools like firewalls, VPNs, antivirus software, and encryption are matched to specific security needs.
7.  Advanced network security methods include Network Segmentation, Data Loss Prevention (DLP), Network Access Control (NAC), and SIEM/SEIM.

## Practice questions

**1. Which of the following best defines computer security?**

- A. The process of connecting multiple computers to share resources over the internet
- B. The protection of computer systems and information from theft, damage, and unauthorized use
- C. The physical maintenance and cleaning of computer hardware
- D. The development of software applications for end users

**Answer: B.** Computer security focuses on defending systems, networks, and data from malicious attacks, theft, and damage. Option A describes networking, and C describes computer maintenance.

**2. Which core dimension of information security ensures that data has not been altered by unauthorized persons?**

- A. Confidentiality
- B. Availability
- C. Integrity
- D. Accessibility

**Answer: C.** Integrity ensures that data is accurate and untampered with. Confidentiality keeps it secret, and Availability/Accessibility ensures it can be reached when needed.

**3. The security tool primarily used to monitor and block unauthorized traffic at the boundary of a network is a:**

- A. Web browser
- B. Firewall
- C. Word processor
- D. Flash drive

**Answer: B.** A firewall acts as a barrier between a trusted internal network and an untrusted external network (like the internet), filtering traffic based on rules. Option A is for browsing, C is for typing documents, and D is for storage.

**4. A student logs into a portal, and an attacker steals their "cookie" to use the account without a password. What type of application threat is this?**

- A. Session management threat
- B. Input threat
- C. Parameter tampering
- D. Data loss prevention

**Answer: A.** Stealing a session token or cookie to impersonate a user is a session management threat (session hijacking). Parameter tampering involves altering background data sent to the server.

**5. Which security method creates an encrypted tunnel over the internet to ensure safe communication?**

- A. Network Access Control (NAC)
- B. Antivirus software
- C. Security Information and Event Management (SEIM)
- D. Virtual Private Network (VPN)

**Answer: D.** A VPN encrypts internet traffic, providing a secure tunnel over a public network. NAC is for checking devices before they join a local network.

**6. Which of the following is an example of an "Input" application threat?**

- A. Forgetting a password
- B. Typing a database command into a login box to bypass security
- C. Encrypting a hard drive
- D. A power cut shutting down a server

**Answer: B.** Typing hostile code (like SQL Injection) into a form field is an input threat, where the attacker uses the input mechanism to send harmful commands.

**7. In the context of the JAMB syllabus, what does the abbreviation SEIM (or SIEM) relate to?**

- A. Software that manages email marketing
- B. A centralized system for logging and analyzing security events
- C. A tool used exclusively for creating web pages
- D. The physical lock used on a server room door

**Answer: B.** Security Information and Event Management (SIEM/SEIM) collects and analyzes security logs and events across a network to detect threats.

**8. An organization divides its main network into smaller, isolated sections to stop malware from spreading easily. This network security method is called:**

- A. Network segmentation
- B. Behavioural analytics
- C. Email security
- D. Mobile device security

**Answer: A.** Network segmentation splits a computer network into smaller subnets, improving security by isolating issues and restricting access between different parts of the network.

**9. What is the primary characteristic of Data Loss Prevention (DLP) methods?**

- A. They recover files that have been accidentally deleted from the Recycle Bin
- B. They ensure that sensitive information is not sent outside the company network
- C. They stop hardware from overheating and melting data
- D. They block all internet access for employees

**Answer: B.** DLP software monitors and controls data transfers to prevent sensitive information (like passwords or customer data) from leaking or being exfiltrated from the network.

**10. Which of the following best represents "Confidentiality" in the CIA triad?**

- A. Using a backup generator to keep a website running
- B. Encrypting a file so only someone with the correct password can read it
- C. Using a digital signature to prove a file hasn't been changed
- D. Updating antivirus software

**Answer: B.** Encryption ensures that unauthorized people cannot read the data, which directly protects confidentiality (secrecy). Option A is Availability, and Option C is Integrity.

<!-- COVERAGE
obj vi | Definition of computer security
obj vii | Types of computer security and their characteristics
obj viii | Security tools for different types of security
obj ix | Categories of application threats
obj x | Basic dimensions of Information Security (The CIA Triad)
obj xi | Network security issues
obj xii | Network security methods
-->
