# JAMB Computer Studies Notes: Computer Networking

## What JAMB expects

This topic is Section F, Topic 5 of the JAMB Computer Studies syllabus: Networking. It covers the following content items:

* (a) Definitions
* (b) Network types
* (c) Network topologies
* (d) Network devices

By the end of these notes, you should be able to:
1. Define computer network (objective i)
2. List and define various types of Networks: PAN, LAN, WAN, MAN, Intranet, Extranet, Internet (objective ii)
3. Explain the differences in basic network topologies: Star, Bus, Ring (objective iii)
4. Define and explain the use of network devices: Hub, Modems, Switches, Routers, Gateway, Repeaters, Access Points Interface (API), Network Interface Card (NIC) etc. (objective iv)

**Note on the syllabus wording:** In the list of network devices, the syllabus asks for "Access Points Interface (API)". In standard computer science, "API" stands for Application Programming Interface (which is software), while the device that provides wireless network signals is called a **Wireless Access Point (WAP)** or simply an **Access Point (AP)**. You should know the standard name, but be aware that a JAMB question might use the exact phrase "Access Points Interface (API)" to mean a wireless access point. We explain it under that name below.

---

## What is a computer network?

**Objective i: Define computer network**
**Content a: Definitions**

A **computer network** is a collection of two or more computers and other devices connected together to share resources and communicate with one another. 

When computers are not connected to any network, they are called **stand-alone** computers. Once connected, they become part of a network, often called **nodes** or **workstations**. 

### Why do we network computers?
1. **Resource sharing:** Instead of buying a printer for every computer in a school or office, all the computers can be connected to a network to share one single printer.
2. **Data and file sharing:** Users can easily send files to one another without needing to copy them onto a flash drive. 
3. **Communication:** Networks allow people to use emails, chat applications, and video conferencing.
4. **Cost savings:** Sharing hardware (like printers or scanners) and software (like network licenses for applications) saves money.

---

## Types of computer networks

**Objective ii: List and define various types of Networks**
**Content b: Network types**

Networks are generally classified by their geographical coverage (how far they stretch) or by their level of privacy.

### 1. Classification by geographical coverage (PAN, LAN, MAN, WAN)

These are the four main types based on physical distance:

* **PAN (Personal Area Network):** The smallest type of network. It covers a very short distance (usually within 10 metres) and is meant for one person. 
  * *Example:* Connecting your smartphone to a Bluetooth earpiece, or linking your laptop to your phone's Wi-Fi hotspot.
* **LAN (Local Area Network):** A network confined to a small geographical area, such as a single room, a building, a school, or a cybercafe. The devices are usually connected using cables (Ethernet) or Wi-Fi. 
  * *Example:* The JAMB CBT centre network where all the testing computers are connected to a local server in the same building.
* **MAN (Metropolitan Area Network):** A network that covers a larger physical area than a LAN but is smaller than a WAN. It usually spans a city, a large university campus, or a large metropolitan area. 
  * *Example:* A city's cable television network, or a university connecting its different faculties spread across a town.
* **WAN (Wide Area Network):** The largest type of network. It spans across cities, countries, or even continents. Because of the vast distances, WANs use satellite links, undersea cables, and telecommunication lines. 
  * *Example:* A Nigerian bank connecting all its branches in Lagos, Kano, and Enugu to its headquarters. The **Internet** is the largest WAN in the world.

**Comparison of PAN, LAN, MAN, and WAN:**

| Feature | PAN | LAN | MAN | WAN |
| :--- | :--- | :--- | :--- | :--- |
| **Meaning** | Personal Area Network | Local Area Network | Metropolitan Area Network | Wide Area Network |
| **Coverage Area** | A few metres (personal space) | A room, building, or school | A city or large campus | A country, continent, or the world |
| **Setup Cost** | Negligible (usually built-in) | Low to Medium | High | Very High |
| **Speed** | Slow to Moderate | Very High | Moderate to High | Varies (often slower than LAN due to distance) |
| **Common Example** | Bluetooth, Mobile Hotspot | Cybercafe, Office network | City cable TV network | The Internet, Nationwide bank network |

### 2. Classification by access and privacy (Intranet, Extranet, Internet)

These networks use the same technology, but they differ in **who is allowed to access them**.

* **Intranet:** A strictly **private** network used within a single organisation. Only employees or members of that organisation can access it. For example, a company might have an Intranet where staff can view internal announcements and company policies. Outsiders cannot see it.
* **Extranet:** A private network (Intranet) that has been partially opened up to **authorised outsiders**. For example, a supermarket might allow its trusted suppliers to log into a specific part of its network to check stock levels so they know when to deliver more goods.
* **Internet:** A **public**, global network of networks. Anyone with an internet connection can access it. It links millions of private, public, academic, and government networks worldwide. 

---

## Network topologies

**Objective iii: Explain the differences in basic network topologies: Star, Bus, Ring**
**Content c: Network topologies**

A **network topology** refers to the physical layout or arrangement of connected devices (nodes) in a network. The syllabus focuses on three basic topologies: Star, Bus, and Ring.

### 1. Star Topology
In a Star topology, every computer on the network is connected to a central device (usually a **Switch** or a **Hub**). All data sent from one computer to another must pass through this central device. 

* **Advantage:** If one cable breaks, only the computer connected to that cable is affected; the rest of the network keeps working. It is very easy to add new computers.
* **Disadvantage:** If the central device (hub/switch) fails, the entire network goes down. It also requires a lot of cable because every computer needs its own line to the centre.
* *Note:* This is the most common topology used in modern LANs (like in homes and offices).

### 2. Bus Topology
In a Bus topology, all computers are connected to a single main cable called the **backbone** or **bus**. At each end of the main cable, there is a component called a **terminator** that stops signals from bouncing back and causing interference. Data travels along the main cable, and every computer checks to see if the data is meant for it.

* **Advantage:** It is very cheap and easy to set up for small networks because it uses the least amount of cable.
* **Disadvantage:** If the main backbone cable breaks, the entire network goes down. Also, as more computers are added, the network becomes very slow due to data collisions on the single cable.

### 3. Ring Topology
In a Ring topology, each computer is connected to exactly two other computers, forming a closed circle or ring. Data travels in one direction (unidirectional) from computer to computer until it reaches its destination. Some older systems used a special signal called a "token" that gets passed around the ring to prevent data collisions.

* **Advantage:** Data flows smoothly without collisions because it goes in one direction.
* **Disadvantage:** If any single computer breaks down or a cable gets cut, the ring is broken, and the entire network stops working (unless it is a more expensive "dual-ring" setup).

[IMAGE: A diagram showing three distinct network layouts. 1) Star: A central switch in the middle with lines radiating out to four computers. 2) Bus: A single horizontal line with terminators at both ends, with four computers attached to it via short drop lines. 3) Ring: Four computers connected in a closed circle. Style: clean flat textbook illustration, white background with clear labels.]

**Comparison of Star, Bus, and Ring Topologies:**

| Feature | Star | Bus | Ring |
| :--- | :--- | :--- | :--- |
| **Layout** | Central device with radiating connections | Single main backbone cable | Closed loop (circle) |
| **Cable required** | Most (one for each device) | Least | Moderate |
| **Effect of a cable break** | Only that specific computer loses connection | Entire network crashes | Entire network crashes |
| **Effect of central failure** | Entire network crashes | N/A (no central device) | N/A (no central device) |
| **Performance with many users** | Stays fast (if a switch is used) | Slows down greatly (collisions) | Better than Bus, as tokens manage traffic |

---

## Network devices

**Objective iv: Define and explain the use of network devices**
**Content d: Network devices**

To build a network, we need specific hardware devices to direct the flow of data. 

### 1. Network Interface Card (NIC)
A **NIC** is the circuit board or chip installed in a computer that allows it to connect to a network. Every device on a network must have a NIC. It converts data from the computer into a form that can be transmitted over the network cable or wireless signal. Every NIC has a unique, permanent hardware address burned into it by the manufacturer, known as a **MAC address**.

### 2. Hub
A **Hub** is a simple central connection device for a Star topology network. When a Hub receives data from one computer, it blindly **broadcasts** (copies and sends) that data to every other computer connected to it. This causes unnecessary traffic and makes the network slower, which is why Hubs are mostly obsolete and have been replaced by Switches.

### 3. Switch
A **Switch** is a "smart" central connection device. Unlike a Hub, a Switch learns the MAC addresses of the devices connected to it. When it receives data, it reads the destination address and sends the data **only to the specific computer** it is meant for. This greatly improves network speed and security.

### 4. Router
A **Router** is a device that connects two or more **different networks** together (for example, connecting your home LAN to the public Internet WAN). Routers use IP (Internet Protocol) addresses to figure out the best and fastest path to send data packets from the source to the destination. 

### 5. Modem
The word "Modem" stands for **MOdulator-DEModulator**. Computers use digital signals (1s and 0s), but telephone and older cable lines use analog (continuous wave) signals. A modem is used to connect a computer network to an Internet Service Provider (ISP). 
* **Modulation:** It converts digital signals from the computer into analog signals to travel over the telephone line.
* **Demodulation:** It converts analog signals coming from the line back into digital signals the computer can understand.

### 6. Repeater
Signals lose strength as they travel over long distances along cables (a problem called *attenuation*). A **Repeater** is a device that receives a weak signal, cleans it, amplifies (boosts) it, and re-transmits it so it can travel further distances without losing data. 

### 7. Gateway
A **Gateway** is a powerful network point or device that connects two entirely different networks that use completely different rules (protocols) and architectures. While a router connects networks of the same type, a gateway translates data so that two completely incompatible networks can communicate. 

### 8. Access Points Interface (API) / Wireless Access Point (WAP)
*Recall the syllabus wording note: The syllabus calls this "Access Points Interface (API)". In reality, this device is a Wireless Access Point (WAP).*
An **Access Point** is a device that creates a wireless local area network (WLAN). It connects to a wired router or switch via a cable, and then projects a Wi-Fi signal so that wireless devices (laptops, phones) can connect to the wired network. 

**Summary comparison of central connection devices:**

| Device | What it does | "Smart" or "Dumb"? | Connects... |
| :--- | :--- | :--- | :--- |
| **Hub** | Broadcasts data to all ports | Dumb (Layer 1) | Devices in the same LAN |
| **Switch** | Sends data only to the specific destination port | Smart (Layer 2) | Devices in the same LAN |
| **Router** | Routes data between different networks | Very Smart (Layer 3) | Different networks (e.g., LAN to WAN) |
| **Gateway** | Translates data between incompatible networks | Advanced | Two completely different networks |

---

## Key terms

| Term | Meaning |
| :--- | :--- |
| **Network** | Two or more connected computing devices that share resources and data. |
| **Topology** | The physical or logical layout of a network. |
| **Node / Workstation** | Any computing device connected to a network. |
| **PAN** | Personal Area Network (e.g., Bluetooth). |
| **LAN** | Local Area Network (e.g., a school computer room). |
| **WAN** | Wide Area Network (e.g., the Internet, nationwide bank). |
| **Intranet** | A private network strictly for members of one organisation. |
| **Extranet** | An Intranet that is partially accessible to authorised outsiders. |
| **NIC** | Network Interface Card; hardware that allows a computer to join a network. |
| **Modem** | Device that translates digital signals to analog (and vice versa). |

---

## Exam tips and common mistakes

* **Hub vs. Switch:** JAMB frequently tests this difference. Remember: A Hub broadcasts to *everyone*, causing traffic jams. A Switch sends data *only* to the intended recipient.
* **Router vs. Gateway:** A Router links networks (like a LAN to the Internet) using IP addresses. A Gateway links *incompatible* networks by translating their completely different rules.
* **Bus topology single point of failure:** In a Star topology, a cut cable affects one computer. In a Bus topology, a cut main cable crashes the *entire* network. 
* **Intranet vs Extranet:** If a question mentions "suppliers", "vendors", or "authorised outsiders" logging into a company's private network, the answer is Extranet, not Intranet.
* **Syllabus trap:** If you see "Access Points Interface (API)" in a question about wireless devices, know that it refers to a Wireless Access Point. 
* **Modem function:** Always remember MOdulator (digital to analog) and DEModulator (analog to digital). 

---

## Quick summary

1. A computer network is formed when two or more computers are connected to share resources like files, hardware, and communication.
2. Based on distance, networks are classified into PAN (personal), LAN (local building/campus), MAN (city), and WAN (country/world).
3. Based on access, an Intranet is totally private, an Extranet allows some trusted outsiders, and the Internet is fully public.
4. Topologies describe the layout of a network. A Star network uses a central hub/switch, a Bus network uses a single main backbone cable, and a Ring network connects devices in a closed loop.
5. A NIC (Network Interface Card) is required for any computer to join a network.
6. A Switch is smarter than a Hub because it directs data only to the specific destination rather than broadcasting it everywhere.
7. A Router connects different networks (e.g., linking a home LAN to the Internet), while a Modem converts digital data to analog to travel over telephone or cable lines.
8. A Repeater boosts weak signals so they can travel longer distances without dropping. 

---

## Practice questions

**1. A computer network confined to a small geographical area such as a school building is called a:**
- A. Wide Area Network (WAN)
- B. Personal Area Network (PAN)
- C. Local Area Network (LAN)
- D. Metropolitan Area Network (MAN)

**Answer: C.** A Local Area Network (LAN) spans a small area like a single building, cybercafe, or school.

**2. Which network topology consists of a single central cable to which all computers are connected?**
- A. Star topology
- B. Ring topology
- C. Mesh topology
- D. Bus topology

**Answer: D.** The Bus topology uses a single main backbone cable with terminators at both ends.

**3. The device that converts digital signals from a computer into analog signals to travel over telephone lines is the:**
- A. Switch
- B. Modem
- C. Repeater
- D. Hub

**Answer: B.** The Modem (Modulator-Demodulator) translates between digital signals (for computers) and analog signals (for telephone lines).

**4. What is the major difference between an Intranet and an Extranet?**
- A. An Intranet is faster than an Extranet.
- B. An Extranet allows authorised outsiders to access the network, while an Intranet is strictly for internal staff.
- C. An Intranet is public, while an Extranet is private.
- D. An Extranet is used globally, while an Intranet is only for Bluetooth.

**Answer: B.** Extranets are essentially Intranets that have been partially opened up for trusted external partners like suppliers or clients.

**5. In a Star topology, what happens if the central device fails?**
- A. Only one node will go offline.
- B. The network will become faster.
- C. The entire network will fail.
- D. The network switches to ring topology.

**Answer: C.** Because all data in a Star topology must pass through the central device (hub/switch), a failure of this device causes the whole network to crash.

**6. Which of the following devices is used to amplify weakened signals so they can travel a longer distance?**
- A. Repeater
- B. Gateway
- C. NIC
- D. Access Point

**Answer: A.** A Repeater cleans and boosts (amplifies) attenuated signals so they can travel further.

**7. A central device that blindly broadcasts data to all computers connected to it, causing network traffic, is known as a:**
- A. Router
- B. Hub
- C. Switch
- D. Gateway

**Answer: B.** A Hub is a basic ("dumb") device that copies and broadcasts data to every port. A Switch (a tempting wrong option) is smarter and sends data only to the specific intended port.

**8. The hardware component installed in a computer that allows it to physically connect to a network is the:**
- A. Network Interface Card (NIC)
- B. Modulator
- C. Repeater
- D. Bus backbone

**Answer: A.** The Network Interface Card (NIC) connects the computer to the network and holds the MAC address.

**9. According to the syllabus terminology, which device allows wireless devices to connect to a wired network?**
- A. Gateway
- B. Access Points Interface (API)
- C. Modem
- D. Hub

**Answer: B.** The syllabus uses the term "Access Points Interface (API)" to refer to the device commonly known as a Wireless Access Point (WAP).

**10. A network that links the headquarters of a bank in Lagos to its branches in Kano and Enugu is best described as a:**
- A. PAN
- B. LAN
- C. WAN
- D. MAN

**Answer: C.** A Wide Area Network (WAN) covers large geographical distances such as crossing multiple states, countries, or continents.

<!-- COVERAGE
obj i | What is a computer network?
obj ii | Types of computer networks
obj iii | Network topologies
obj iv | Network devices
item a | What is a computer network?
item b | Types of computer networks
item c | Network topologies
item d | Network devices
-->
