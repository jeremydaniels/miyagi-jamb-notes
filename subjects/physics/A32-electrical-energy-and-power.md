# JAMB Physics Notes: Electrical Energy and Power

## What JAMB expects

This topic is Section A, Topic 32 of the JAMB Physics syllabus. It covers the principles of electrical energy, how it is calculated, paid for, transmitted over long distances, and safely distributed in our homes. 

According to the syllabus contents, this topic covers:
* (i) concepts of electrical energy and power;
* (ii) commercial unit of electric energy and power;
* (iii) electric power transmission;
* (v) heating effects of electric current;
* (vi) electrical wiring of houses;
* (vii) use of fuses.

By the end of these notes, you should be able to:
* i. apply the expressions of electrical energy and power to solve problems;
* ii. analyse how power is transmitted from the power station to the consumer;
* iii. identify the heating effects of current and its uses;
* iv. identify the advantages of parallel arrangement over series;
* v. determine the fuse rating.

**Note on the syllabus wording:** In the printed JAMB syllabus contents for this topic, the Roman numeral numbering skips directly from (iii) to (v), omitting (iv). We have covered all the printed items and objectives exactly as they are given, mapping them in order so you do not miss anything.

---

## Concepts of Electrical Energy and Power

When you turn on a torchlight, an electric fan, or a television, electrical energy from a battery or the mains supply is converted into other forms of energy like light, kinetic energy, or sound. 

**Electrical Energy ($E$ or $W$)** is the work done by an electromotive force (e.m.f.) in moving an electric charge through a circuit. 
From the definition of potential difference ($V$), the work done in moving a charge ($Q$) is given by:
$$W = QV$$

Since electric current ($I$) is the rate of flow of charge ($I = \frac{Q}{t}$, meaning $Q = It$), we can substitute $Q$ to get the fundamental equation for electrical energy:
$$E = VIt$$
where:
*   $E$ is the electrical energy in Joules ($\text{J}$)
*   $V$ is the potential difference in Volts ($\text{V}$)
*   $I$ is the current in Amperes ($\text{A}$)
*   $t$ is the time in seconds ($\text{s}$)

Using Ohm's Law ($V = IR$), we can derive two other useful formulas for electrical energy:
1. Substitute $V = IR$ into $E = VIt$:
   $$E = (IR)It = I^2Rt$$
2. Substitute $I = \frac{V}{R}$ into $E = VIt$:
   $$E = V\left(\frac{V}{R}\right)t = \frac{V^2}{R}t$$

**Electrical Power ($P$)** is the rate at which electrical energy is consumed or generated. 
$$P = \frac{E}{t}$$
Dividing our energy formulas by time ($t$), we get the three formulas for power:
$$P = VI$$
$$P = I^2R$$
$$P = \frac{V^2}{R}$$
where power ($P$) is measured in Watts ($\text{W}$). One Watt is equal to one Joule per second ($1\ \text{W} = 1\ \text{J s}^{-1}$).

### Applying expressions of electrical energy and power

JAMB frequently tests your ability to choose the right formula based on the values provided in the question.

**Worked Example 1: Finding electrical energy**
A $100\ \text{W}$ incandescent lamp is left switched on for $5\ \text{minutes}$. Calculate the electrical energy consumed in Joules.

**Working:**
1. Identify the given values: Power $P = 100\ \text{W}$, time $t = 5\ \text{minutes}$.
2. Convert time to the SI unit (seconds): $t = 5 \times 60 = 300\ \text{s}$. (This is a crucial step!).
3. State the formula connecting energy, power, and time: $E = Pt$.
4. Substitute the values with units: $E = 100\ \text{W} \times 300\ \text{s}$.
5. Calculate the result: $E = 30,000\ \text{J}$.
6. State the final answer: The energy consumed is $30,000\ \text{J}$ (or $30\ \text{kJ}$).

**Worked Example 2: Finding resistance from power rating**
An electric boiling ring is rated $1000\ \text{W}$, $200\ \text{V}$. What is the resistance of its heating element?

**Working:**
1. Identify the given values: Power $P = 1000\ \text{W}$, Voltage $V = 200\ \text{V}$.
2. Identify the required value: Resistance $R$.
3. Choose the power formula that connects $P$, $V$, and $R$: $P = \frac{V^2}{R}$.
4. Rearrange the formula to make $R$ the subject: $R = \frac{V^2}{P}$.
5. Substitute the values: $R = \frac{200^2}{1000} = \frac{40,000}{1000}$.
6. Calculate the final answer: $R = 40\ \Omega$.

> **Common Mistakes:** When calculating energy in Joules, students often forget to convert time from minutes or hours into seconds. Always check your units! For example, if a question says $2\ \text{hours}$, you must multiply by $3600$ ($2 \times 3600 = 7200\ \text{s}$) before substituting into $E = Pt$.

---

## Commercial unit of electric energy and power

The Joule is a very small unit of energy. If the electricity company (e.g., PHCN/DisCos in Nigeria) billed you in Joules, a typical monthly bill would show billions of Joules. To make things simpler, electricity is sold in a larger commercial unit called the **kilowatt-hour ($\text{kWh}$)**. 

On a prepaid meter, when you buy "units" of electricity, you are actually buying kilowatt-hours. 

*   **1 kilowatt-hour ($\text{kWh}$)** is the electrical energy consumed by a $1\ \text{kW}$ ($1000\ \text{W}$) appliance operating continuously for $1\ \text{hour}$.

**Converting $\text{kWh}$ to Joules:**
$$1\ \text{kWh} = 1000\ \text{W} \times 3600\ \text{s}$$
$$1\ \text{kWh} = 3,600,000\ \text{J} = 3.6 \times 10^6\ \text{J}$$

**Calculating the Cost of Electricity:**
To find how much it costs to run appliances, you must first calculate the total energy used in $\text{kWh}$, and then multiply by the cost per unit.
$$\text{Energy (kWh)} = \text{Power (in kW)} \times \text{Time (in hours)}$$
$$\text{Total Cost} = \text{Energy (kWh)} \times \text{Price per kWh}$$

**Worked Example 3: Calculating electricity bills**
A family runs a "I-pass-my-neighbour" small generator substitute (an inverter setup) that powers four $50\ \text{W}$ standing fans and a $200\ \text{W}$ television for $8\ \text{hours}$. If the equivalent cost of grid electricity is ₦60 per $\text{kWh}$, calculate the cost of the energy used.

**Working:**
1. Calculate the total power consumed by the appliances in Watts: 
   Fans: $4 \times 50\ \text{W} = 200\ \text{W}$.
   Television: $200\ \text{W}$.
   Total Power = $200\ \text{W} + 200\ \text{W} = 400\ \text{W}$.
2. Convert total power from Watts to kilowatts by dividing by 1000:
   $P = \frac{400}{1000} = 0.4\ \text{kW}$.
3. Identify the time in hours: $t = 8\ \text{hours}$. (Do NOT convert to seconds here!).
4. Calculate the energy in $\text{kWh}$: 
   $E = 0.4\ \text{kW} \times 8\ \text{h} = 3.2\ \text{kWh}$.
5. Calculate the total cost: 
   Cost = $3.2\ \text{kWh} \times 60 = 192$.
6. Final answer: The energy costs ₦192.

---

## Electric Power Transmission

Electricity is generated in power stations that are often far from the cities where the power is needed. For example, Nigeria generates hydroelectricity at the Kainji Dam in Niger State and thermal electricity at the Egbin Power Station in Lagos State. This power must be sent across the country through thick cables called transmission lines (the National Grid).

### Analysing how power is transmitted

When electric current flows through transmission cables, some electrical energy is converted into heat due to the electrical resistance of the cables. This lost energy escapes into the air and is wasted. 
The power lost as heat is given by:
$$P_{\text{loss}} = I^2R$$
where $I$ is the current flowing through the cables, and $R$ is the total resistance of the cables.

Since the resistance $R$ of long cables cannot be easily reduced to zero, the only way to minimize power loss is to **reduce the current, $I$**. Notice that because the current is squared ($I^2$), even a small reduction in current leads to a massive reduction in power loss.

To transmit a given amount of power ($P_{\text{transmitted}} = IV$), if we reduce the current ($I$), we must increase the voltage ($V$) so that the total power remains the same. This is why **electric power is transmitted at very high voltages and low currents.**

**The Transmission Process (Step-by-Step):**
1. **Generation:** Electricity is generated at a moderate voltage (e.g., $11\ \text{kV}$ to $25\ \text{kV}$).
2. **Step-up Transformer:** At the power station, a step-up transformer increases the voltage to an extremely high level (e.g., $132\ \text{kV}$ or $330\ \text{kV}$ in Nigeria). This drops the current dramatically, ensuring very little heat is lost along the grid.
3. **Transmission:** The high-voltage electricity travels through the national grid cables supported by tall metal pylons.
4. **Step-down Transformer:** Before entering cities and eventually houses, step-down transformers at sub-stations reduce the dangerous high voltage down to safer, usable levels ($11\ \text{kV}$, then to $415\ \text{V}$ for heavy industry, and $240\ \text{V}$ for domestic homes).

[IMAGE: A flowchart showing electricity transmission. On the left, a power station connected to a step-up transformer. Thick cables suspended on tall metal pylons carry the power to the right. The cables connect to a step-down substation, which then feeds smaller wooden poles delivering power to a small house. Labels: "Power Station (11 kV)", "Step-up Transformer (330 kV)", "High Voltage Transmission Lines", "Step-down Substation (11 kV)", "Distribution to Homes (240 V)". Clean flat textbook illustration, white background.]

**Worked Example 4: Calculating Power Loss**
A power station transmits $20\ \text{kW}$ of power to a factory through cables with a total resistance of $0.5\ \Omega$. Calculate the power lost as heat in the cables if the power is transmitted at (a) $1000\ \text{V}$ and (b) $5000\ \text{V}$.

**Working for (a) $1000\ \text{V}$ transmission:**
1. Find the current in the cables: $I = \frac{P}{V} = \frac{20,000\ \text{W}}{1000\ \text{V}} = 20\ \text{A}$.
2. Calculate power loss using $I^2R$: $P_{\text{loss}} = (20\ \text{A})^2 \times 0.5\ \Omega$.
3. Result: $P_{\text{loss}} = 400 \times 0.5 = 200\ \text{W}$.

**Working for (b) $5000\ \text{V}$ transmission:**
1. Find the new current: $I = \frac{P}{V} = \frac{20,000\ \text{W}}{5000\ \text{V}} = 4\ \text{A}$.
2. Calculate power loss: $P_{\text{loss}} = (4\ \text{A})^2 \times 0.5\ \Omega$.
3. Result: $P_{\text{loss}} = 16 \times 0.5 = 8\ \text{W}$.

*Conclusion:* By stepping the voltage up by 5 times (from $1000\ \text{V}$ to $5000\ \text{V}$), the current dropped by 5 times, and the power lost dropped by $5^2 = 25$ times (from $200\ \text{W}$ to $8\ \text{W}$). High voltage transmission is incredibly effective!

> **Common Mistakes in Transmission Problems:** Students often try to calculate power loss using the formula $P = \frac{V^2}{R}$. They substitute the high transmission voltage (e.g., $10,000\ \text{V}$) into this formula. This is **completely wrong**. The $V$ in $\frac{V^2}{R}$ must be the voltage *drop across the cable itself*, not the transmission voltage. Always use $I^2R$ for transmission power loss calculations!

---

## Heating Effects of Electric Current

When electric current flows through a conductor, it encounters resistance. The electrons in the current collide with the atoms of the conductor, transferring kinetic energy to them. The atoms vibrate more vigorously, and the conductor becomes hot. 

The heat generated ($H$) is described by **Joule's Law of Heating**, which states that the heat produced in a resistor is directly proportional to the square of the current ($I^2$), the resistance ($R$), and the time ($t$) for which the current flows.
$$H = I^2Rt$$
*(Notice that this is exactly the same as the equation for electrical energy we derived earlier!)*

### Identifying uses of the heating effect

Engineers exploit the heating effect of current to design many everyday appliances. These devices contain a **heating element** (usually a coil of wire made from an alloy like Nichrome). Nichrome is chosen because it has a high resistance (so it generates lots of heat) and a high melting point (so it does not melt when it gets red-hot).

**Common uses include:**
1. **Electric Boiling Ring / Electric Kettle:** The heating element sits directly in the water. As current passes through, the $I^2R$ heat boils the water.
2. **Electric Iron:** The heating element is sandwiched between layers of mica (an electrical insulator but a good conductor of heat). The heat is transferred to the heavy metal soleplate for pressing clothes.
3. **Incandescent Filament Bulb:** An old-fashioned light bulb contains a very thin filament of Tungsten. Because it is so thin, it has a very high resistance. When current flows, the filament gets white-hot (about $2500\ ^\circ\text{C}$) and emits light. (Modern LED bulbs do not rely on the heating effect and are therefore much more energy-efficient).
4. **Fuses:** We will discuss these in detail in the last section, but they operate purely on the heating effect melting a wire to break a circuit.

[IMAGE: A cross-section of a traditional electric pressing iron. It shows the main cord entering at the back, connected to a coiled heating element (labelled "Nichrome heating element"). Above and below the element are thin sheets labelled "Mica insulation". Below the mica is a thick metal base labelled "Heavy metal soleplate". A simple thermostat switch is shown inside the handle. Clean flat textbook illustration, white background.]

---

## Electrical Wiring of Houses

Electricity is brought into homes using two main wires: the **Live wire** (usually colored brown or red) and the **Neutral wire** (colored blue or black). A third wire, the **Earth wire** (colored green/yellow), is included for safety. The standard domestic voltage supplied by the grid in Nigeria is $240\ \text{V}$ alternating current (a.c.).

### Advantages of parallel arrangement over series

When wiring a house, appliances (lamps, sockets, ceiling fans) can theoretically be connected either in series or in parallel. In practice, **all house wiring is done in parallel**. Let's examine why by comparing the two.

| Feature | Parallel Wiring (Used in homes) | Series Wiring |
| :--- | :--- | :--- |
| **Voltage across appliances** | Every appliance is connected directly across the Live and Neutral lines, meaning **every appliance gets the full $240\ \text{V}$**. | The $240\ \text{V}$ is shared among the appliances. If you connect many bulbs, they will all be very dim. |
| **Effect of a fault or switch** | Appliances operate **independently**. If one bulb blows or is switched off, current still flows through the other branches. The rest of the house stays lit. | There is only one path for current. If one bulb blows, the circuit is broken, and **every appliance in the house goes off**. |
| **Overall Resistance** | Adding more appliances in parallel **decreases** the total resistance, allowing the circuit to draw enough current from the supply to power them all. | Adding more appliances **increases** the total resistance, severely restricting the current. |

**The Ring Main Circuit**
In modern houses, wall sockets are often wired in a "ring main circuit". The live, neutral, and earth wires start from the consumer unit (fuse box), loop around the house from socket to socket, and return to the fuse box. This creates two parallel paths for the current to reach any socket, reducing the load on the cables and allowing thinner, cheaper cables to be used safely.

---

## Use of Fuses

A **fuse** is a safety device designed to protect a circuit and its appliances from excessive current. If too much current flows (due to a power surge, an overloaded socket, or a short circuit), the wires can get hot enough to start a fire. 

A fuse contains a short piece of wire (often tinned copper) with a low melting point. The fuse is always connected in series on the **Live wire** before the appliance. If the current exceeds a safe limit, the heating effect ($I^2R$) causes the fuse wire to melt (or "blow"). This breaks the circuit, stopping the current and keeping the appliance and house safe.

> **Crucial Rule:** A fuse must *always* be placed on the **Live wire**, never on the Neutral. If it were on the Neutral wire and blew, the circuit would break, but the appliance would still be connected to the high voltage from the Live wire. Anyone touching the internal parts of the appliance would receive a severe electric shock.

### How to determine the fuse rating

The **fuse rating** is the maximum current that the fuse will allow to pass without melting. Common standard fuse ratings for plugs are $3\ \text{A}$, $5\ \text{A}$, $10\ \text{A}$, and $13\ \text{A}$. 

To determine the correct fuse for an appliance, you must first calculate its normal operating current using $I = \frac{P}{V}$. The suitable fuse rating is the standard size that is **just slightly higher** than the normal operating current.

*   If the fuse rating is exactly equal to or less than the operating current, it will blow during normal use.
*   If the fuse rating is much too high (e.g., using a $13\ \text{A}$ fuse for a $1\ \text{A}$ device), it will not melt when a dangerous moderate fault occurs, defeating its purpose.

**Worked Example 5: Selecting a fuse**
An electric kettle is rated $2000\ \text{W}$, $240\ \text{V}$. Determine the most suitable fuse rating from the following options: $3\ \text{A}$, $5\ \text{A}$, $10\ \text{A}$, $13\ \text{A}$.

**Working:**
1. State the formula for current: $I = \frac{P}{V}$.
2. Substitute the values: $I = \frac{2000\ \text{W}}{240\ \text{V}}$.
3. Calculate the normal operating current: $I \approx 8.33\ \text{A}$.
4. Choose the fuse rating: The fuse must be slightly above $8.33\ \text{A}$. The next standard value available in the options is $10\ \text{A}$.
5. Final answer: A $10\ \text{A}$ fuse is the most suitable.

---

## Key terms

| Term | Meaning |
| :--- | :--- |
| **Electrical Energy** | The work done in moving an electric charge through a circuit. Measured in Joules ($\text{J}$) or $\text{kWh}$. |
| **Electrical Power** | The rate at which electrical energy is consumed or dissipated. Measured in Watts ($\text{W}$). |
| **Kilowatt-hour (kWh)** | The commercial unit of electrical energy; the energy consumed by a $1000\ \text{W}$ appliance running for $1\ \text{hour}$. |
| **Step-up Transformer** | A device at power stations that increases voltage and decreases current for efficient long-distance transmission. |
| **Joule's Law of Heating** | The heat produced by a current is proportional to the square of the current, the resistance, and the time ($H = I^2Rt$). |
| **Parallel Circuit** | A circuit arrangement where appliances are connected side-by-side. If one fails, the others continue to work. Used in house wiring. |
| **Fuse** | A safety device with a low-melting-point wire that melts and breaks the circuit if the current becomes dangerously high. |
| **Fuse Rating** | The maximum current a fuse can carry without melting. |

---

## Exam tips and common mistakes

*   **Time Units in Joules vs. kWh:** If you are asked for energy in **Joules**, time *must* be in seconds. If you are asked for energy in **kWh** (or to find the cost on an electric bill), leave power in **kW** and time in **hours**.
*   **The Transmission Trap:** When asked for power loss in cables during transmission, never use $P_{\text{loss}} = \frac{V^2}{R}$ with the transmission voltage. Always find the transmitted current first ($I = \frac{P}{V}$), and then use $P_{\text{loss}} = I^2R$.
*   **Missing the Square:** A very common careless error is writing $H = I^2R$ but forgetting to actually square the value of $I$ in your calculator.
*   **Fuse Wire Placement:** JAMB often asks where a fuse should be connected. The answer is always the **Live wire**.
*   **Bulbs in Series:** If a JAMB theory question states that bulbs are connected in series and one goes bad, remember that *all* of them will go off because the circuit is broken.

---

## Quick summary

1. Electrical energy is calculated as $E = VIt = I^2Rt = \frac{V^2}{R}t$. Its SI unit is the Joule ($\text{J}$).
2. Electrical power is the rate of energy usage: $P = VI = I^2R = \frac{V^2}{R}$. Its SI unit is the Watt ($\text{W}$).
3. The commercial unit of electrical energy used for billing is the kilowatt-hour ($\text{kWh}$). $1\ \text{kWh} = 3.6 \times 10^6\ \text{J}$.
4. Power is transmitted over long distances at very high voltages. This reduces the transmitted current, which in turn drastically reduces the $I^2R$ heat loss in the cables.
5. The heating effect of current ($H = I^2Rt$) is applied in devices like boiling rings, electric kettles, and pressing irons, which use high-resistance wire.
6. Houses are wired in parallel so that every appliance receives the full mains voltage ($240\ \text{V}$) and can be operated independently without affecting others.
7. A fuse is placed on the live wire for safety. Its rating should be slightly higher than the normal operating current of the appliance to handle minor, safe surges but blow during a dangerous fault.

---

## Practice questions

**1. Calculate the cost of running a $2\ \text{kW}$ electric heater for $5\ \text{hours}$ if electrical energy costs ₦40 per $\text{kWh}$.**
- A. ₦200
- B. ₦400
- C. ₦800
- D. ₦4,000

**Answer: B.** 
1. Energy in $\text{kWh} = \text{Power (kW)} \times \text{Time (h)}$.
2. $E = 2\ \text{kW} \times 5\ \text{h} = 10\ \text{kWh}$.
3. Cost = $E \times \text{price per kWh} = 10 \times 40$.
4. Cost = ₦400.

**2. A $40\ \text{W}$ light bulb is switched on for $2\ \text{minutes}$. Calculate the energy consumed in Joules.**
- A. $80\ \text{J}$
- B. $4,800\ \text{J}$
- C. $8,000\ \text{J}$
- D. $240,000\ \text{J}$

**Answer: B.**
1. Formula for energy: $E = Pt$.
2. Convert time to seconds: $t = 2 \times 60 = 120\ \text{s}$.
3. Substitute: $E = 40\ \text{W} \times 120\ \text{s}$.
4. Calculate: $E = 4,800\ \text{J}$.
The mistake in Option A comes from failing to convert minutes to seconds ($40 \times 2 = 80$).

**3. An electric iron is rated $1500\ \text{W}$, $250\ \text{V}$. Which of the following fuse ratings is the most suitable to protect it?**
- A. $3\ \text{A}$
- B. $5\ \text{A}$
- C. $10\ \text{A}$
- D. $15\ \text{A}$

**Answer: C.**
1. Calculate normal operating current: $I = \frac{P}{V}$.
2. $I = \frac{1500}{250} = 6.0\ \text{A}$.
3. The most suitable fuse is the standard rating slightly above the operating current. $10\ \text{A}$ is suitable. (A $5\ \text{A}$ fuse would blow instantly under normal use).

**4. Why is electrical power from generating stations transmitted over long distances at very high voltages?**
- A. To increase the speed at which electricity travels
- B. To increase the current in the transmission lines
- C. To reduce the resistance of the transmission cables
- D. To minimize power loss as heat in the cables

**Answer: D.** Stepping up the voltage drastically reduces the current required to transmit a given amount of power. Since power lost as heat is $I^2R$, a lower current means significantly minimized power loss.

**5. A generating station transmits $20\ \text{kW}$ of power at $1000\ \text{V}$ through transmission lines with a total resistance of $0.5\ \Omega$. Calculate the power lost in the lines.**
- A. $20\ \text{W}$
- B. $200\ \text{W}$
- C. $10,000\ \text{W}$
- D. $2,000,000\ \text{W}$

**Answer: B.**
1. Find transmitted current: $I = \frac{P}{V} = \frac{20,000}{1000} = 20\ \text{A}$.
2. Formula for power loss: $P_{\text{loss}} = I^2R$.
3. Substitute: $P_{\text{loss}} = (20)^2 \times 0.5 = 400 \times 0.5 = 200\ \text{W}$.
The tempting wrong Option D comes from the common mistake of using $\frac{V^2}{R}$ with the transmission voltage ($\frac{1000^2}{0.5} = 2,000,000$).

**6. What is the resistance of the heating element in a $1000\ \text{W}$, $200\ \text{V}$ boiling ring?**
- A. $5\ \Omega$
- B. $20\ \Omega$
- C. $40\ \Omega$
- D. $50\ \Omega$

**Answer: C.**
1. Formula connecting $P$, $V$, and $R$: $P = \frac{V^2}{R}$.
2. Rearrange for $R$: $R = \frac{V^2}{P}$.
3. Substitute: $R = \frac{200^2}{1000} = \frac{40,000}{1000}$.
4. Calculate: $R = 40\ \Omega$.

**7. Which of the following is a major advantage of wiring household appliances in parallel rather than in series?**
- A. It reduces the cost of electricity consumed
- B. A fault in one appliance does not stop the others from working
- C. It increases the overall resistance of the circuit
- D. It allows different appliances to share the main voltage

**Answer: B.** In a parallel circuit, there are multiple independent paths for current. If one appliance breaks or is switched off, the circuit is not broken for the other appliances. Also, they do not share the voltage; every appliance gets the full mains voltage.

**8. The rate at which electrical energy is converted into heat or other forms of energy in a circuit is called**
- A. Electromotive force
- B. Electrical work
- C. Electrical power
- D. Potential difference

**Answer: C.** Power is defined as the rate of doing work or the rate at which energy is used ($P = \frac{E}{t}$).

**9. Which of the following expressions does NOT represent electrical power?**
- A. $I^2 R$
- B. $VI$
- C. $I R^2$
- D. $\frac{V^2}{R}$

**Answer: C.** $IR^2$ is not a valid formula for power. The correct formulas, derived from Ohm's Law and $P = VI$, are $I^2R$, $VI$, and $\frac{V^2}{R}$.

**10. For maximum safety, an electrical fuse in a household circuit must be connected to the**
- A. Neutral wire
- B. Live wire
- C. Earth wire
- D. Metal casing of the appliance

**Answer: B.** The fuse must always be connected on the Live wire before the appliance. This ensures that if the fuse blows, the appliance is completely disconnected from the high-voltage supply, preventing electric shocks.
