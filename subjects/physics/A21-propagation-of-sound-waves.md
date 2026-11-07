# JAMB Physics Notes: Propagation of Sound Waves

## What JAMB expects

This topic is Section 21 of the JAMB Physics syllabus: Propagation of Sound Waves. 

By the end of these notes, you should be able to:
1. determine the need for a material medium in the propagation of sound waves;
2. compare the speed of sound in solids, liquids and air;
3. relate the effects of temperature and pressure to the speed of sound in air;
4. solve problem on echoes, reverberation and speed;
5. compare the disadvantages and advantages of echoes;
6. solve problems on echo, reverberation and speed of sound.

*Note on the syllabus wording:* You will notice that objective (iv) and objective (vi) ask for almost exactly the same thing. To make sure we cover everything properly and give you plenty of practice, we have provided two separate calculation sections with different types of worked examples to build your confidence for the exam.

## The necessity for a material medium

**Objective i: determine the need for a material medium in the propagation of sound waves.**  
**Content (i): the necessity for a material medium.**

Sound is a **mechanical, longitudinal wave**. This means that it is produced by vibrating bodies and transfers energy through the physical compression and rarefaction (expansion) of particles. Because it relies entirely on the vibration of particles to pass energy along, **sound cannot travel through a vacuum (empty space)**. It absolutely requires a material medium—such as a solid, a liquid, or a gas—to propagate. 

### The Bell-Jar Experiment
The classic demonstration to prove that sound needs a material medium is the **Bell-Jar experiment**.

**Apparatus and Procedure:**
1. An electric bell is suspended by soft rubber bands inside a tightly sealed glass bell jar. (The rubber bands are important because they prevent the sound vibrations from travelling directly through the solid glass jar).
2. The jar is placed on a flat plate connected to a vacuum pump, which can suck the air out of the jar.
3. The switch is turned on, and the bell begins to ring. The hammer is clearly seen striking the gong, and a loud ringing sound is heard.
4. The vacuum pump is turned on to slowly remove the air from inside the jar.

**Observations:**
As the air is pumped out, reducing the air pressure, the sound of the ringing bell gradually becomes fainter and fainter, even though the hammer is still seen striking the gong with the exact same force. Eventually, when a near-perfect vacuum is created inside the jar (pressure approaches $0\ \text{Pa}$), the sound can no longer be heard at all. If air is allowed back into the jar, the sound of the bell is heard again.

**Conclusion:**
Sound requires a material medium (in this case, air) to travel from the bell to our ears. Note that light, being an electromagnetic wave, does not need a material medium. This is why you can still *see* the bell ringing inside the vacuum even when you cannot *hear* it.

[IMAGE: The Bell-Jar Experiment. A glass bell jar placed on a vacuum pump plate. Inside the jar, an electric bell is suspended by rubber bands. Wires lead outside to a battery and switch. An arrow points out from the pump plate labeled "To vacuum pump (air pumped out)". Clean flat textbook illustration, white background.]

## Speed of sound in solids, liquids and air

**Objective ii: compare the speed of sound in solids, liquids and air.**  
**Content (ii): speed of sound in solids, liquids and air.**

Sound waves travel at drastically different speeds depending on the material they are passing through. Two main properties of a medium determine the speed of sound ($v$):
1. **Elasticity ($E$):** How well and how quickly the particles bounce back to their original position after being displaced.
2. **Density ($\rho$):** The mass per unit volume of the medium.

The general formula (often known as the Newton-Laplace equation) is:
$$v = \sqrt{\frac{E}{\rho}}$$
Where:
*   $v$ = speed of sound (in $\text{m s}^{-1}$)
*   $E$ = elastic modulus of the medium (in $\text{N m}^{-2}$ or $\text{Pa}$)
*   $\rho$ = density of the medium (in $\text{kg m}^{-3}$)

Although denser materials generally slow down sound (because $\rho$ is in the denominator), materials that are very dense (like solids) also tend to have **extremely high elastic properties (rigidity)**. In physics, the elastic property of a solid completely overpowers its density. Therefore, sound travels much faster in highly elastic, rigid materials than in compressible gases.

| Medium | Approximate Speed ($v$) | Reason |
| --- | --- | --- |
| **Solids** (e.g., steel, wood, iron) | Highest (usually $4000$ to $6000\ \text{m s}^{-1}$) | Solids are very rigid and highly elastic (high Young's Modulus). Particles are tightly packed and instantly transmit vibrations to their neighbours. |
| **Liquids** (e.g., water) | Intermediate (about $1500\ \text{m s}^{-1}$) | Liquids are less elastic (more compressible) than solids, but more elastic than gases (they have a moderate Bulk Modulus). |
| **Gases / Air** | Lowest (about $330$ to $343\ \text{m s}^{-1}$) | Gases are highly compressible and have the lowest elastic properties. The particles are far apart, so energy transfer takes longer. |

**Summary comparison:**
$$v_{\text{solid}} > v_{\text{liquid}} > v_{\text{gas}}$$

Because of this difference, if someone strikes a long metal pipe and you put your ear to the other end, you will hear two sounds. The first sound arrives very quickly through the solid metal, and a fainter second sound arrives slightly later through the air inside the pipe.

## Effects of temperature and pressure on the speed of sound in air

**Objective iii: relate the effects of temperature and pressure to the speed of sound in air.**

In gases (like air), the speed of sound is affected by several environmental factors. JAMB frequently tests whether you know exactly *which* factors change the speed and which do not. 

### 1. Effect of Temperature (Very Important)
The speed of sound in a gas is **directly proportional to the square root of its absolute temperature (Kelvin)**.
$$v \propto \sqrt{T}$$

This means that on a hot day, sound travels faster than on a cold day. If the absolute temperature of a gas is quadrupled, the speed of sound is doubled (since $\sqrt{4} = 2$). 

When comparing the speed at two different temperatures, use the formula:
$$\frac{v_1}{v_2} = \sqrt{\frac{T_1}{T_2}}$$
*(Where $T$ MUST be in Kelvin. To convert Celsius to Kelvin, use $T(\text{K}) = \theta(^\circ\text{C}) + 273$.)*

### 2. Effect of Pressure (The JAMB Trick)
**A change in atmospheric pressure has NO EFFECT on the speed of sound in a gas, provided the temperature remains constant.** 

*Why?* According to Boyle's law, if you increase the pressure ($P$) of a gas at a constant temperature, you compress it, meaning its density ($\rho$) increases proportionally. Since $v = \sqrt{\frac{\gamma P}{\rho}}$ (where $\gamma$ is a constant for the gas), if $P$ doubles, $\rho$ also doubles. The ratio $\frac{P}{\rho}$ stays exactly the same, and the speed of sound remains unchanged. Never fall for exam questions that say "if pressure is doubled, what happens to the speed of sound?" The answer is always: it remains the same.

### 3. Effect of Humidity (Moisture)
Water vapour (H₂O) has a lower molar mass than the nitrogen (N₂) and oxygen (O₂) that make up most of dry air. Because water molecules are lighter, moist air is actually **less dense** than dry air. Since sound travels faster in less dense gases, **an increase in humidity increases the speed of sound**. Sound travels faster in the humid air of the rainy season than during the dry, dusty Harmattan.

### 4. Effect of Wind
If the wind is blowing in the same direction that the sound is travelling, the speeds add up ($v_{\text{effective}} = v_{\text{sound}} + v_{\text{wind}}$). If the wind blows directly against the sound, you subtract the wind speed.

## Reflection of sound: echoes, reverberation and their applications

**Content (iii): reflection of sound; echoes, reverberation and their applications.**

When sound waves hit a hard, rigid surface (like a tall building, a steep cliff, or a mountain), they bounce back. This is called the **reflection of sound**. The laws of reflection for sound are exactly the same as those for light (angle of incidence equals angle of reflection).

### Echoes
An **echo** is a distinct, delayed reflection of a sound wave. For the human ear to distinguish an echo from the original sound, the reflected sound must arrive at least **$0.1\ \text{s}$** after the original sound. This is because the human brain retains a sound sensation for about a tenth of a second. 

To hear a distinct echo in air (assuming $v = 340\ \text{m s}^{-1}$), the sound must travel for at least $0.1\ \text{s}$. 
Distance travelled = $v \times t = 340 \times 0.1 = 34\ \text{m}$.
Since the sound has to travel to the wall and back, the wall must be at least $\frac{34\ \text{m}}{2} = 17\ \text{m}$ away.

### Reverberation
**Reverberation** is the persistence or prolongation of sound in an enclosure due to multiple, rapid reflections off the walls, ceiling, and floor. Unlike a clear echo, the time delay between the reflections is less than $0.1\ \text{s}$, so they blend together into a continuous, rolling blur of noise. This is very common in empty halls or large, unfurnished rooms.

### Applications of Echoes and Reflection
1. **SONAR (Sound Navigation and Ranging):** Ships send high-frequency sound (ultrasound) into the water. By measuring how long it takes for the echo to bounce off a submarine, a school of fish, or the seabed, they can calculate depth and map the ocean floor.
2. **Medical Ultrasound Imaging:** High-frequency sound waves are directed into the human body. Different tissues reflect sound differently, creating live images of internal organs or a developing fetus.
3. **Oil and Mineral Exploration:** Geologists set off small explosions at the surface. The sound waves travel deep into the earth and bounce off different rock layers. By analysing these seismic echoes, they can locate underground oil, gas, or minerals.
4. **Animal Navigation (Echolocation):** Bats and dolphins emit ultrasonic clicks and listen for the echoes to navigate and hunt in total darkness (like in the Ogbunike caves).

[IMAGE: A ship on the ocean surface using SONAR. A sound pulse (labeled 'transmitted pulse') travels downwards to the uneven seabed. Another wave (labeled 'reflected echo') travels back up to a receiver on the ship. The depth of the water is marked 'd'. Clean flat textbook illustration, white background.]

## Advantages and disadvantages of echoes and reverberations

**Content (iv): advantages and disadvantages of echoes and reverberations.**  
**Objective v: compare the disadvantages and advantages of echoes.**

| Phenomenon | Advantages | Disadvantages |
| --- | --- | --- |
| **Echoes** | - Used for accurately measuring distances (e.g., SONAR).<br>- Used by bats and dolphins for finding food and navigating.<br>- Vital for ultrasound scans in medicine. | - Can cause confusion in speech and communication if heard too loudly.<br>- Creates noise pollution if repeatedly reflected in residential areas. |
| **Reverberation** | - A small, controlled amount of reverberation gives music a rich, full sound in concert halls (it creates good "acoustics"). | - Too much reverberation blurs syllables, making human speech completely unintelligible in large empty halls.<br>- Amplifies background noise, causing a nuisance. |

**How to reduce unwanted reverberation:** To stop sound from bouncing around excessively, large spaces (like cinemas in Ikeja or the National Arts Theatre) are fitted with sound-absorbing materials. Heavy curtains, padded seats, acoustic ceiling tiles, and carpets are used to absorb the sound waves rather than reflect them.

## Solving problems on echoes, reverberation and speed

**Objective iv: solve problem on echoes, reverberation and speed.**

When dealing with echoes, the sound must travel to the obstacle and then travel back to the listener. 
If the distance to the obstacle is $d$, the **total distance** the sound travels is $2d$. 

The formula for the speed of sound $v$ using echoes is:
$$v = \frac{2d}{t}$$
Where:
*   $v$ = speed of sound (in $\text{m s}^{-1}$)
*   $d$ = distance between the source and the reflecting surface (in $\text{m}$)
*   $t$ = total time taken for the echo to be heard (in $\text{s}$)

**Worked Example 1: Calculating distance using an echo**
A student standing in front of a vertical cliff claps his hands and hears the echo $2.5\ \text{s}$ later. If the speed of sound in air is $340\ \text{m s}^{-1}$, how far is the cliff from the student?

1. **State the given values:**
   Speed $v = 340\ \text{m s}^{-1}$, time $t = 2.5\ \text{s}$.
2. **State the formula for echo distance:**
   By rearranging $v = \frac{2d}{t}$, we get $d = \frac{v \times t}{2}$.
3. **Substitute the values with units:**
   $d = \frac{340\ \text{m s}^{-1} \times 2.5\ \text{s}}{2}$.
4. **Calculate the total distance travelled (numerator):**
   $340 \times 2.5 = 850\ \text{m}$.
5. **Divide by 2 to find the one-way distance:**
   $d = \frac{850}{2} = 425\ \text{m}$.
6. **State the final answer:**
   The cliff is $425\ \text{m}$ away.

**Worked Example 2: Finding time for an echo in a borehole**
A boy shouts into a dry borehole in his village that is $85\ \text{m}$ deep. How long will it take for the echo to return to him? (Assume the speed of sound is $340\ \text{m s}^{-1}$).

1. **State the given values:**
   Distance $d = 85\ \text{m}$, speed $v = 340\ \text{m s}^{-1}$.
2. **State the formula relating speed, distance and time for an echo:**
   $t = \frac{2d}{v}$.
3. **Substitute the values with units:**
   $t = \frac{2 \times 85\ \text{m}}{340\ \text{m s}^{-1}}$.
4. **Calculate the numerator (total round-trip distance):**
   $2 \times 85 = 170\ \text{m}$.
5. **Divide by the speed:**
   $t = \frac{170}{340} = 0.5\ \text{s}$.
6. **State the final answer:**
   The boy hears the echo after $0.5\ \text{s}$.

**Worked Example 3: Multiple echoes between two cliffs**
A man stands between two parallel cliffs. He fires a gun and hears the first echo after $1.5\ \text{s}$ and the second echo after $2.5\ \text{s}$. If the speed of sound is $330\ \text{m s}^{-1}$, what is the distance between the two cliffs?

1. **State the given values:** 
   $v = 330\ \text{m s}^{-1}$, $t_1 = 1.5\ \text{s}$, $t_2 = 2.5\ \text{s}$.
2. **Calculate the distance to the nearer cliff ($d_1$):**
   $d_1 = \frac{v \times t_1}{2}$.
3. **Substitute and solve for $d_1$:**
   $d_1 = \frac{330\ \text{m s}^{-1} \times 1.5\ \text{s}}{2} = \frac{495}{2} = 247.5\ \text{m}$.
4. **Calculate the distance to the farther cliff ($d_2$):**
   $d_2 = \frac{v \times t_2}{2}$.
5. **Substitute and solve for $d_2$:**
   $d_2 = \frac{330\ \text{m s}^{-1} \times 2.5\ \text{s}}{2} = \frac{825}{2} = 412.5\ \text{m}$.
6. **Add the two distances to find total distance ($D$):**
   $D = d_1 + d_2 = 247.5\ \text{m} + 412.5\ \text{m} = 660\ \text{m}$.
7. **State the final answer:** 
   The total distance between the cliffs is $660\ \text{m}$.

[IMAGE: Diagram showing a man standing between two tall parallel cliffs. A dashed line represents the distance 'd1' to the left cliff, and a longer dashed line represents the distance 'd2' to the right cliff. The total distance between the cliffs is marked 'D = d1 + d2'. Clean flat textbook illustration, white background.]

## Further problems on echo, reverberation and speed of sound

**Objective vi: solve problems on echo, reverberation and speed of sound.**

Not all problems involve echoes. Sometimes you need to calculate the direct speed of sound (where no reflection occurs), or you must calculate how the speed of sound changes with temperature or when travelling through different media.

**Worked Example 4: Direct speed (No echo)**
During a heavy rainstorm in Lagos, a girl sees a flash of lightning and hears the thunder $3.5\ \text{s}$ later. How far away did the lightning strike? (Assume the speed of sound is $340\ \text{m s}^{-1}$ and that light travels almost instantaneously).

1. **State the given values:**
   Speed $v = 340\ \text{m s}^{-1}$, time $t = 3.5\ \text{s}$.
2. **Choose the direct sound formula (no reflection):**
   Because the sound is travelling directly from the cloud to the girl (it is NOT bouncing back), do not use the echo formula. Use standard speed: $d = v \times t$.
3. **Substitute the values with units:**
   $d = 340\ \text{m s}^{-1} \times 3.5\ \text{s}$.
4. **Calculate the product:**
   $340 \times 3.5 = 1190\ \text{m}$.
5. **State the final answer:**
   The lightning struck $1190\ \text{m}$ away.

**Worked Example 5: Speed in different media**
A worker strikes one end of a straight steel pipe that is $1020\ \text{m}$ long. A colleague at the other end hears two distinct sounds. If the speed of sound in steel is $5100\ \text{m s}^{-1}$ and in air is $340\ \text{m s}^{-1}$, what is the time interval between the two sounds?

1. **State the given values:**
   Distance $d = 1020\ \text{m}$, $v_{\text{steel}} = 5100\ \text{m s}^{-1}$, $v_{\text{air}} = 340\ \text{m s}^{-1}$.
2. **Calculate the time taken for sound to travel through the air:**
   $t_{\text{air}} = \frac{d}{v_{\text{air}}} = \frac{1020\ \text{m}}{340\ \text{m s}^{-1}}$.
3. **Solve for $t_{\text{air}}$:**
   $t_{\text{air}} = 3.0\ \text{s}$.
4. **Calculate the time taken for sound to travel through the steel pipe:**
   $t_{\text{steel}} = \frac{d}{v_{\text{steel}}} = \frac{1020\ \text{m}}{5100\ \text{m s}^{-1}}$.
5. **Solve for $t_{\text{steel}}$:**
   $t_{\text{steel}} = 0.2\ \text{s}$.
6. **Calculate the time interval between hearing them:**
   $\Delta t = 3.0\ \text{s} - 0.2\ \text{s} = 2.8\ \text{s}$.
7. **State the final answer:**
   The time interval is $2.8\ \text{s}$.

**Worked Example 6: Temperature effect on speed**
If the speed of sound in air at $16^\circ\text{C}$ is $340\ \text{m s}^{-1}$, calculate its speed at $51^\circ\text{C}$.

1. **State the given values:**
   $v_1 = 340\ \text{m s}^{-1}$, initial temperature $\theta_1 = 16^\circ\text{C}$, final temperature $\theta_2 = 51^\circ\text{C}$.
2. **Convert temperatures to Kelvin (crucial step):**
   $T_1 = 16 + 273 = 289\ \text{K}$, and $T_2 = 51 + 273 = 324\ \text{K}$.
3. **State the formula relating speed of sound and temperature:**
   $\frac{v_1}{v_2} = \sqrt{\frac{T_1}{T_2}}$.
4. **Rearrange to solve for $v_2$:**
   $v_2 = v_1 \times \sqrt{\frac{T_2}{T_1}}$.
5. **Substitute the values:**
   $v_2 = 340 \times \sqrt{\frac{324}{289}}$.
6. **Calculate the square roots:**
   $\sqrt{324} = 18$, and $\sqrt{289} = 17$.
7. **Simplify the expression:**
   $v_2 = 340 \times \frac{18}{17} = 20 \times 18 = 360\ \text{m s}^{-1}$.
8. **State the final answer:**
   The speed at $51^\circ\text{C}$ is $360\ \text{m s}^{-1}$.

## Key terms

| Term | Meaning |
| --- | --- |
| **Material Medium** | A substance (solid, liquid, or gas) through which a mechanical wave like sound can travel. |
| **Vacuum** | A space entirely devoid of matter ($0\ \text{Pa}$ pressure); sound cannot travel through it. |
| **Echo** | The distinct repetition of a sound resulting from reflection off a rigid surface (time delay $> 0.1\ \text{s}$). |
| **Reverberation** | The prolonged blending and persistence of sound in an enclosed space due to multiple rapid reflections (time delay $< 0.1\ \text{s}$). |
| **SONAR** | Sound Navigation and Ranging; a technique that uses sound propagation (usually underwater) to navigate or map depths. |
| **Elasticity** | The property of a material that allows it to return to its original shape; the main reason sound travels fastest in solids. |
| **Acoustics** | The branch of physics concerned with the properties of sound; also refers to the qualities of a room that determine how sound is heard in it. |

## Exam tips and common mistakes

- **Forgetting to divide by 2 in echo problems:** This is the most common mistake! If a question says an *echo* is heard after $4\ \text{s}$, the sound took $2\ \text{s}$ to get to the wall and $2\ \text{s}$ to come back. Always use $d = \frac{v \times t}{2}$.
- **Mixing up Direct Sound and Echoes:** If you see lightning and hear thunder, that is direct sound (use $d = v \times t$). If you shout at a wall and hear it back, that is an echo (use $d = \frac{v \times t}{2}$).
- **The Pressure Trick:** Remember that changes in atmospheric pressure do **not** change the speed of sound at a constant temperature. If a question asks what happens to the speed of sound if pressure is doubled, the answer is "it remains unchanged."
- **Celsius vs Kelvin:** In the temperature formula $v \propto \sqrt{T}$, the temperature $T$ must ALWAYS be in Kelvin. If JAMB gives you Celsius, add $273$ before doing any maths.
- **Humidity Increases Speed:** It feels counter-intuitive, but moist/humid air is less dense than dry air. Sound travels faster in humid air.

## Quick summary

1. Sound is a mechanical longitudinal wave that requires a material medium (like solids, liquids, or gases) to propagate; it cannot travel through a vacuum.
2. The speed of sound is highest in solids, intermediate in liquids, and lowest in gases because solids have much greater elastic properties.
3. In a gas, the speed of sound is directly proportional to the square root of its absolute (Kelvin) temperature ($v \propto \sqrt{T}$).
4. The speed of sound in air is independent of pressure changes at constant temperature, but it increases if humidity (moisture) increases.
5. An echo is a distinct reflection of sound, calculated using the formula $v = \frac{2d}{t}$. The reflecting obstacle must be at least $17\ \text{m}$ away to hear a distinct echo in air.
6. Reverberation is the blurring and persistence of sound in an enclosed hall due to multiple rapid reflections; it can be controlled using soft, sound-absorbing materials.
7. Echoes have numerous real-world applications, including SONAR, medical ultrasound scans, and oil exploration.

## Practice questions

**1. Which of the following experiments demonstrates that sound cannot travel through a vacuum?**
- A. The simple pendulum experiment
- B. The Bell-Jar experiment
- C. The ripple tank experiment
- D. The resonance tube experiment

**Answer: B.**
1. Sound is a mechanical wave that requires a material medium to transmit energy.
2. The Bell-Jar experiment places a ringing bell inside a sealed jar.
3. A vacuum pump reduces the pressure to nearly $0\ \text{Pa}$, causing the sound to fade away.
4. This proves that at $0\ \text{Pa}$ (a vacuum), sound speed $v = 0\ \text{m s}^{-1}$ because there are no particles to vibrate.
5. The mistake behind option C is choosing an experiment used to show the properties of water waves (which also travel at a given $v$ but are not related to sound in a vacuum).

**2. A sound wave takes $0.05\ \text{s}$ to travel through a $250\ \text{m}$ steel pipe. What is the speed of sound in the steel?**
- A. $12.5\ \text{m s}^{-1}$
- B. $1250\ \text{m s}^{-1}$
- C. $5000\ \text{m s}^{-1}$
- D. $10000\ \text{m s}^{-1}$

**Answer: C.**
1. Identify the given values: direct distance $d = 250\ \text{m}$, time $t = 0.05\ \text{s}$.
2. Use the direct speed formula (no reflection): $v = \frac{d}{t}$.
3. Substitute the values: $v = \frac{250\ \text{m}}{0.05\ \text{s}}$.
4. Calculate the speed: $v = 5000\ \text{m s}^{-1}$.
5. The mistake behind option A is wrongly multiplying distance and time ($250 \times 0.05 = 12.5\ \text{m s}^{-1}$).

**3. The speed of sound in air at $300\ \text{K}$ is $340\ \text{m s}^{-1}$. If the temperature remains constant but the atmospheric pressure is doubled, what is the new speed of sound?**
- A. $170\ \text{m s}^{-1}$
- B. $340\ \text{m s}^{-1}$
- C. $680\ \text{m s}^{-1}$
- D. $1360\ \text{m s}^{-1}$

**Answer: B.**
1. Identify given values: initial speed $v_1 = 340\ \text{m s}^{-1}$, pressure is doubled, temperature is constant.
2. Recall that for a gas at constant temperature, pressure has no effect on the speed of sound.
3. This is because density increases proportionally with pressure, keeping the ratio $\frac{P}{\rho}$ constant.
4. Therefore, the new speed is identical: $v_2 = v_1 = 340\ \text{m s}^{-1}$.
5. The mistake behind option C is wrongly assuming speed is directly proportional to pressure and doubling the speed ($340 \times 2 = 680\ \text{m s}^{-1}$).

**4. The speed of sound in air at $0^\circ\text{C}$ is $330\ \text{m s}^{-1}$. At what temperature will its speed be $660\ \text{m s}^{-1}$?**
- A. $273^\circ\text{C}$
- B. $546^\circ\text{C}$
- C. $819^\circ\text{C}$
- D. $1092^\circ\text{C}$

**Answer: C.**
1. The speed doubles from $330\ \text{m s}^{-1}$ to $660\ \text{m s}^{-1}$. 
2. Since $v \propto \sqrt{T}$, to double the speed, the Kelvin temperature must be multiplied by $4$ (since $\sqrt{4} = 2$). 
3. Convert initial temperature to Kelvin: $T_1 = 0^\circ\text{C} + 273 = 273\ \text{K}$. 
4. Calculate new Kelvin temperature: $T_2 = 273 \times 4 = 1092\ \text{K}$. 
5. Convert back to Celsius: $\theta_2 = 1092 - 273 = 819^\circ\text{C}$.
6. The mistake behind option D is forgetting to convert the final answer back to Celsius from Kelvin.

**5. A boy fires a gun and hears the echo from a distant cliff $3.0\ \text{s}$ later. If the speed of sound is $340\ \text{m s}^{-1}$, how far is the cliff from the boy?**
- A. $340\ \text{m}$
- B. $510\ \text{m}$
- C. $1020\ \text{m}$
- D. $2040\ \text{m}$

**Answer: B.**
1. Identify the given values: speed $v = 340\ \text{m s}^{-1}$, echo time $t = 3.0\ \text{s}$.
2. Use the echo distance formula: $d = \frac{v \times t}{2}$. 
3. Substitute the values: $d = \frac{340\ \text{m s}^{-1} \times 3.0\ \text{s}}{2}$. 
4. Calculate the distance: $d = \frac{1020\ \text{m}}{2} = 510\ \text{m}$.
5. The mistake behind option C is using the direct formula ($d = v \times t = 1020\ \text{m}$) and forgetting to divide by 2 for a round trip.

**6. A ship sends a SONAR pulse downwards to the seabed and receives the echo after $0.8\ \text{s}$. If the depth of the sea is $600\ \text{m}$, what is the speed of sound in the water?**
- A. $750\ \text{m s}^{-1}$
- B. $1200\ \text{m s}^{-1}$
- C. $1500\ \text{m s}^{-1}$
- D. $3000\ \text{m s}^{-1}$

**Answer: C.**
1. Identify given values: echo time $t = 0.8\ \text{s}$, one-way distance $d = 600\ \text{m}$.
2. Use the rearranged echo formula: $v = \frac{2d}{t}$. 
3. Substitute the values: $v = \frac{2 \times 600\ \text{m}}{0.8\ \text{s}}$. 
4. Calculate the speed: $v = \frac{1200\ \text{m}}{0.8\ \text{s}} = 1500\ \text{m s}^{-1}$.
5. The mistake behind option A is forgetting to multiply the depth by 2 (calculating $v = \frac{600}{0.8} = 750\ \text{m s}^{-1}$).

**7. Which of the following is a direct disadvantage of reverberation in a large concert hall?**
- A. It causes the hall's structural walls to weaken
- B. It makes speech and music indistinct and blurry
- C. It rapidly decreases the speed of sound in the hall
- D. It completely prevents sound waves from reflecting

**Answer: B.**
1. Reverberation is the prolonged persistence of sound due to multiple rapid reflections.
2. If the time gap between reflections is less than $0.1\ \text{s}$, the human ear cannot distinguish them.
3. This overlapping of sound waves causes syllables and musical notes to run into each other, blurring the sound.
4. The actual speed of sound remains $v \approx 340\ \text{m s}^{-1}$ and does not decrease.
5. The mistake behind option C is wrongly assuming that bouncing around slows down the actual wave speed ($v$), whereas it only affects acoustic clarity.

**8. A girl stands $165\ \text{m}$ away from a high vertical wall and claps her hands steadily. At what time interval must she clap so that each new clap exactly coincides with the echo of the previous clap? (Speed of sound = $330\ \text{m s}^{-1}$)**
- A. $0.25\ \text{s}$
- B. $0.50\ \text{s}$
- C. $1.00\ \text{s}$
- D. $2.00\ \text{s}$

**Answer: C.**
1. She needs to wait exactly the amount of time it takes for one clap's echo to return.
2. Identify given values: distance $d = 165\ \text{m}$, speed $v = 330\ \text{m s}^{-1}$.
3. State the echo formula for time: $t = \frac{2d}{v}$. 
4. Substitute the values: $t = \frac{2 \times 165\ \text{m}}{330\ \text{m s}^{-1}} = \frac{330\ \text{m}}{330\ \text{m s}^{-1}} = 1.00\ \text{s}$.
5. The mistake behind option B is forgetting to multiply the distance by 2 for the echo's round trip, which yields $0.50\ \text{s}$.

**9. Which of these atmospheric conditions increases the speed of sound in air?**
- A. A decrease in absolute temperature
- B. An increase in humidity
- C. An increase in atmospheric pressure
- D. A decrease in pitch

**Answer: B.**
1. The speed of sound in a gas is given by the relation $v = \sqrt{\frac{\gamma P}{\rho}}$.
2. Water vapour (H₂O) has a lower molar mass than dry air (N₂ and O₂).
3. Therefore, an increase in humidity decreases the overall density ($\rho$) of the air.
4. Since density $\rho$ is in the denominator, a lower density results in a higher speed $v$ (e.g., faster than $340\ \text{m s}^{-1}$).
5. The mistake behind option C is assuming pressure changes $v$; but if temperature is constant, changing pressure changes density proportionally, keeping $v$ constant.

**10. A man is situated between two parallel cliffs $A$ and $B$, which are $510\ \text{m}$ apart. He is closer to cliff A. He fires a gun and hears the first echo after $1.0\ \text{s}$. How long after hearing the *first* echo will he hear the *second* echo? (Speed of sound = $340\ \text{m s}^{-1}$)**
- A. $1.0\ \text{s}$
- B. $2.0\ \text{s}$
- C. $3.0\ \text{s}$
- D. $4.0\ \text{s}$

**Answer: A.**
1. Calculate distance to the closer cliff A: $d_A = \frac{v \times t_A}{2} = \frac{340\ \text{m s}^{-1} \times 1.0\ \text{s}}{2} = 170\ \text{m}$.
2. Calculate distance to the farther cliff B: $d_B = 510\ \text{m} - 170\ \text{m} = 340\ \text{m}$.
3. Calculate time for the echo from cliff B (the second echo) to arrive: $t_B = \frac{2 \times d_B}{v} = \frac{2 \times 340\ \text{m}}{340\ \text{m s}^{-1}} = 2.0\ \text{s}$.
4. The question asks for the time *after* the first echo: $\Delta t = t_B - t_A = 2.0\ \text{s} - 1.0\ \text{s} = 1.0\ \text{s}$. 
5. The mistake behind option B is stopping at the absolute time the second echo is heard ($2.0\ \text{s}$), rather than subtracting the delay of the first echo.
