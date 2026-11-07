# JAMB Physics Notes: Measurement, Position, Distance and Displacement

## What JAMB expects

This topic is part of Section A, Topic 2(b) of the JAMB Physics syllabus. It introduces the fundamental tools for measuring length, the mathematical description of position, and the critical differences between moving a certain distance and being displaced. 

This file covers the following content items:
- (a) concept of displacement;
- (ii) distinction between distance and displacement;
- (iii) concept of position and coordinates;
- (iv) frame of reference.

By the end of these notes, you should be able to:
1. use strings, meter rule and engineering calipers, vernier calipers and micrometer screw gauge;
2. note the degree of accuracy;
3. identify distance travel in a specified direction;
4. use compass and protractor to locate points/directions;
5. use Cartesians systems to locate positions in $x-y$ plane;
6. plot graph and draw inference from the graph.

**Note on the syllabus wording:** The syllabus skips from content item "(a)" directly to "(ii)". In the objectives, "screw guage" is a typing error for "screw gauge". The notes below cover every point thoroughly, using correct spellings.

---

## Instruments for measuring length

**Objective i: use strings, meter rule and engineering calipers, vernier calipers and micrometer screw gauge.**

To describe position and displacement, we must first be able to measure length. Different instruments are used depending on the shape of the object and the level of precision required.

### 1. Strings and the Metre Rule
The standard laboratory **metre rule** is used for measuring straight-line distances (up to $1\ \text{m}$ or $100\ \text{cm}$). However, many paths in real life are not straight. 
- **Strings (Thread):** If you need to measure a curved path—such as a winding river on a map or the circumference of a round bucket—you lay a string carefully along the curve. You then straighten the string and measure its length against a standard metre rule. 
- **Precaution:** Ensure the string does not stretch easily, or your measurement will be inaccurate.

### 2. Engineering Calipers
Engineering calipers (or simply calipers) look like a pair of metallic compasses with bent legs. They do not have a measurement scale of their own.
- **Outside calipers:** These have legs that curve inward. They are used to measure the external diameter of objects (like a PVC water pipe for a borehole). You close the caliper around the pipe, remove it carefully, and place the points against a metre rule to read the length.
- **Inside calipers:** These have legs that curve outward. They are used to measure the internal diameter of hollow objects, like a cup or a cylinder.

### 3. Vernier Calipers
The **vernier caliper** is designed to measure small lengths, external diameters, internal diameters, and depths more accurately than a metre rule. 
It has two scales:
1. **The Main Scale:** Fixed, usually marked in centimetres ($\text{cm}$) and millimetres ($\text{mm}$).
2. **The Vernier Scale:** A sliding scale that allows you to read a fraction of a millimetre.

**How to read a vernier caliper:**
1. Read the value on the main scale just *before* the zero mark of the vernier scale.
2. Look along the vernier scale to find the exact line that aligns perfectly with a line on the main scale. Multiply this vernier reading by the instrument's accuracy ($0.01\ \text{cm}$).
3. Add the two values together.

[IMAGE: A close-up view of a vernier caliper scale. The main scale is marked in cm (from 2 to 4). The zero of the vernier scale is past the 3.1 cm mark on the main scale. The 4th division on the vernier scale aligns perfectly with a line on the main scale. Labels: "Main Scale: 3.1 cm", "Vernier Scale: 4th mark aligns", "Reading = 3.1 + (4 x 0.01) = 3.14 cm". Clean flat textbook illustration, white background.]

### 4. Micrometer Screw Gauge
The **micrometer screw gauge** is used for measuring extremely small thicknesses or diameters, such as the thickness of a razor blade, a coin, or a thin copper wire. 
It also has two scales:
1. **The Sleeve (Main Scale):** Fixed, marked in millimetres ($\text{mm}$) and half-millimetres.
2. **The Thimble (Circular Scale):** A rotating scale, usually with 50 divisions.

**How to read a micrometer screw gauge:**
1. Read the highest visible mark on the sleeve (main scale) in $\text{mm}$.
2. See which division on the thimble aligns with the central horizontal line of the sleeve. Multiply this number by $0.01\ \text{mm}$.
3. Add the two readings.

---

## Degree of accuracy and zero errors

**Objective ii: note the degree of accuracy.**

The **degree of accuracy** (or precision limit) of an instrument is the smallest measurement it can take reliably. In physics, this is often determined by the smallest division on the scale. 
- **Metre Rule:** Smallest division is $1\ \text{mm}$ (or $0.1\ \text{cm}$).
- **Vernier Caliper:** Smallest division is usually $0.1\ \text{mm}$ (or $0.01\ \text{cm}$). It measures to 2 decimal places in $\text{cm}$.
- **Micrometer Screw Gauge:** Smallest division is $0.01\ \text{mm}$ (or $0.001\ \text{cm}$). It measures to 2 decimal places in $\text{mm}$.

### Zero Errors
A **zero error** occurs when an instrument gives a reading when it should read zero (for instance, when the jaws of a caliper or the anvil and spindle of a micrometer are completely closed). 
- **Positive zero error:** The instrument reads greater than zero. You must **subtract** this error from your final reading.
- **Negative zero error:** The instrument reads less than zero. You must **add** this error to your final reading.

The formula is:
$$\text{True Reading} = \text{Observed Reading} - \text{Zero Error}$$

### Worked Examples: Accuracy and Errors

**Example 1: Reading a Vernier Caliper**
The main scale reading of a vernier caliper is $4.2\ \text{cm}$. The 7th division on the vernier scale coincides exactly with a mark on the main scale. What is the length measured?
1. State the main scale reading: $4.2\ \text{cm}$.
2. Calculate the vernier scale reading by multiplying the coinciding division by the accuracy ($0.01\ \text{cm}$): $7 \times 0.01\ \text{cm} = 0.07\ \text{cm}$.
3. Add them to find the observed reading: $4.2\ \text{cm} + 0.07\ \text{cm} = 4.27\ \text{cm}$.
4. State the final answer: **$4.27\ \text{cm}$**.

**Example 2: Reading a Micrometer Screw Gauge**
The sleeve of a micrometer shows a reading of $5.5\ \text{mm}$. The thimble reading that aligns with the horizontal line is 32. Find the measured diameter.
1. State the main (sleeve) reading: $5.5\ \text{mm}$.
2. Calculate the thimble reading by multiplying by the accuracy ($0.01\ \text{mm}$): $32 \times 0.01\ \text{mm} = 0.32\ \text{mm}$.
3. Add them together: $5.5\ \text{mm} + 0.32\ \text{mm} = 5.82\ \text{mm}$.
4. State the final answer: **$5.82\ \text{mm}$**.

**Example 3: Correcting for Zero Error**
A student measures the thickness of a glass block with a micrometer screw gauge and gets an observed reading of $2.64\ \text{mm}$. If the instrument has a zero error of $-0.02\ \text{mm}$, what is the true thickness?
1. Write the formula: $\text{True Reading} = \text{Observed Reading} - \text{Zero Error}$.
2. Substitute the values with their signs: $\text{True Reading} = 2.64\ \text{mm} - (-0.02\ \text{mm})$.
3. Calculate the result (subtracting a negative is addition): $2.64\ \text{mm} + 0.02\ \text{mm} = 2.66\ \text{mm}$.
4. State the final answer: **$2.66\ \text{mm}$**.

---

## Concept of displacement

**Content a: concept of displacement.**

When an object moves from one position to another, we need a way to describe that change. **Displacement** is the distance moved by an object in a **specified direction**. 

It is a **vector quantity**, which means it has both magnitude (size) and direction. For example, if you travel from your house to a shop $50\ \text{m}$ due East, your displacement is "$50\ \text{m}$ East". If you return to your house, your total displacement becomes zero, because you have returned to your starting point. Displacement is entirely about the straight-line gap between where you started and where you finished, regardless of the route you took.

## Distinction between distance and displacement

**Content ii: distinction between distance and displacement.**

In everyday English, people use "distance" and "displacement" to mean the same thing. In physics, they are very different.

**Distance** is the total length of the actual path travelled by a body, regardless of direction. If you travel from Lagos to Ibadan along the winding expressway, the distance is the exact mileage your car covers (about $130\ \text{km}$). 

**Displacement** is the straight-line distance from the starting point to the end point in a given direction. If a helicopter flew in a perfectly straight line from your starting point in Lagos to your destination in Ibadan, that straight line represents the displacement (which would be shorter, about $110\ \text{km}$ North-East).

| Feature | Distance | Displacement |
| :--- | :--- | :--- |
| **Definition** | Length of the actual path travelled | Straight-line distance from start to finish in a specified direction |
| **Quantity type** | Scalar (magnitude only) | Vector (magnitude and direction) |
| **Dependence on path** | Depends heavily on the path taken | Independent of the path taken; depends only on initial and final positions |
| **Values** | Always positive | Can be positive, negative, or zero (if you return to start) |

[IMAGE: A diagram illustrating distance vs displacement. Point A (House) is on the left, Point B (School) is on the right. A winding, curvy dotted line connects A to B (labeled "Distance: actual path"). A thick, straight red arrow points directly from A to B (labeled "Displacement: straight-line vector"). Clean flat textbook illustration, white background.]

## Identifying distance traveled in a specified direction

**Objective iii: identify distance travel in a specified direction.**

When you calculate displacement, you are finding the net "distance travelled in a specified direction". Let us look at how to calculate these using some standard scenarios.

**Example 4: Motion in one dimension (Straight Line)**
A trader at a market walks $10\ \text{m}$ due East to a stall, realizes she forgot something, and walks $4\ \text{m}$ due West back along the same path. What is her total distance and her displacement from the starting point?
1. Calculate Distance: total path length $= 10\ \text{m} + 4\ \text{m} = 14\ \text{m}$.
2. Calculate Displacement: taking East as positive and West as negative, Displacement $= +10\ \text{m} - 4\ \text{m} = +6\ \text{m}$.
3. State the final answers: **Distance = $14\ \text{m}$**; **Displacement = $6\ \text{m}$ East**.

**Example 5: Motion in a circular path**
An athlete runs exactly half a lap around a circular track of radius $70\ \text{m}$ from point A to point B. What is the distance and magnitude of displacement? (Take $\pi = \frac{22}{7}$)
1. Write the formula for the distance (half circumference): $\text{Distance} = \pi \times r$.
2. Substitute the values: $\text{Distance} = \frac{22}{7} \times 70\ \text{m} = 220\ \text{m}$.
3. Write the formula for displacement (straight line from A to B across the circle, which is the diameter): $\text{Displacement} = 2 \times r$.
4. Substitute the values: $\text{Displacement} = 2 \times 70\ \text{m} = 140\ \text{m}$.
5. State the answers: **Distance = $220\ \text{m}$**; **Displacement = $140\ \text{m}$**.

---

## Locating points and directions using compass and protractor

**Objective iv: use compass and protractor to locate points/directions.**

When calculating displacement in two dimensions (like moving North, then East), we must combine vectors. This often requires locating points using geographical directions.
- **Compass Directions:** The four cardinal points are North (N), South (S), East (E), and West (W). 
- **Bearings:** In physics and geography, direction is often given as a 3-digit True Bearing measured *clockwise* from the North line (e.g., $045^\circ$, $090^\circ$ for East, $180^\circ$ for South).
- **Protractor:** When drawing scale diagrams on paper, a protractor is used to measure and draw the exact angle of the bearing.

For JAMB, you will usually solve these without a scale diagram, using the **Pythagoras theorem** (for magnitude) and **trigonometry** (for direction/bearing) because the movements form right-angled triangles.

**Example 6: Perpendicular movements and bearing**
A boy walks $3\ \text{km}$ due North, then $4\ \text{km}$ due East. Find his distance covered, the magnitude of his displacement, and his true bearing from the starting point.
1. Calculate Distance: $3\ \text{km} + 4\ \text{km} = 7\ \text{km}$.
2. Draw a mental triangle: The boy moves $3\ \text{km}$ up (N), then $4\ \text{km}$ right (E). The displacement $d$ is the hypotenuse.
3. Calculate magnitude using Pythagoras theorem: $d^2 = 3^2 + 4^2$.
4. $d^2 = 9 + 16 = 25$.
5. $d = \sqrt{25} = 5\ \text{km}$.
6. Calculate the bearing ($\theta$) from the North line. In the triangle, the side opposite the angle at the start is $4\ \text{km}$ (East), and the adjacent side is $3\ \text{km}$ (North). 
7. $\tan \theta = \frac{\text{Opposite}}{\text{Adjacent}} = \frac{4}{3} \approx 1.333$.
8. $\theta = \tan^{-1}(1.333) = 53^\circ$. Because this is clockwise from North, the bearing is $053^\circ$.
9. State the final answers: **Distance = $7\ \text{km}$**; **Displacement = $5\ \text{km}$ at bearing $053^\circ$**.

---

## Frames of reference

**Content iv: frame of reference.**

Motion and position are entirely relative. You cannot say an object is moving or stationary unless you compare it to a background. 

A **frame of reference** is the coordinate system or physical environment from which measurements of position and motion are made. 
- **Example in Nigeria:** Imagine you are seated in a moving *danfo* (commercial bus). To you, the driver is at rest because you are both moving at the same speed inside the same frame of reference (the bus). However, to an okada rider parked by the side of the road (a different frame of reference fixed to the Earth), both you and the driver are moving at high speed.

Without choosing a frame of reference, we cannot assign coordinates or measure displacement.

---

## Concept of position and coordinates

**Content iii: concept of position and coordinates.**

**Position** is the exact location of an object in space at a given moment. 
To define position mathematically, we must set up a coordinate system within our chosen frame of reference. We must agree on a **reference point** or origin. The position of any object is then given by how far it is from this origin in specific directions, called **coordinates**.

## Using Cartesian systems to locate positions

**Objective v: use Cartesians systems to locate positions in x-y plane.**

The most common system for locating points on a flat surface (2D) is the **Cartesian coordinate system**. 
- It consists of two perpendicular axes: the horizontal **x-axis** and the vertical **y-axis**.
- The point where they cross is the **origin**, $(0,0)$.
- Any position on the plane is given as an ordered pair $(x, y)$.

### Calculating distance between two points on the x-y plane
If an object moves from position $P(x_1, y_1)$ to position $Q(x_2, y_2)$, we can find the magnitude of its straight-line displacement (distance between the two points) using a formula derived from the Pythagoras theorem:
$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

[IMAGE: A Cartesian coordinate graph. An x-axis and a y-axis meet at origin O. Two points are plotted: P(x1, y1) and Q(x2, y2). A straight diagonal line 'd' connects P to Q. Dotted lines form a right-angled triangle under the line PQ, with the horizontal leg labelled (x2 - x1) and the vertical leg labelled (y2 - y1). Clean flat textbook illustration, white background.]

**Example 7: Distance from the origin**
Find the displacement of a particle that moves from the origin to a point with coordinates $(6, 8)$ in metres.
1. Identify the coordinates: $(x_1, y_1) = (0, 0)$ and $(x_2, y_2) = (6, 8)$.
2. Write the distance formula: $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.
3. Substitute the values: $d = \sqrt{(6 - 0)^2 + (8 - 0)^2}$.
4. Simplify: $d = \sqrt{6^2 + 8^2} = \sqrt{36 + 64}$.
5. Calculate the final root: $d = \sqrt{100} = 10\ \text{m}$.
6. State the answer: **$10\ \text{m}$**.

**Example 8: Distance between two positive coordinates**
Find the distance between point $A(2, -1)$ and point $B(5, 3)$ on a Cartesian plane, where coordinates are in metres.
1. Identify the coordinates: $(x_1, y_1) = (2, -1)$ and $(x_2, y_2) = (5, 3)$.
2. Write the formula: $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.
3. Substitute carefully: $d = \sqrt{(5 - 2)^2 + (3 - (-1))^2}$.
4. Simplify inside the brackets: $d = \sqrt{(3)^2 + (3 + 1)^2} = \sqrt{3^2 + 4^2}$.
5. Square the numbers: $d = \sqrt{9 + 16} = \sqrt{25}$.
6. Calculate the final root: $d = 5\ \text{m}$.
7. State the answer: **$5\ \text{m}$**.

**Example 9: Handling negative coordinates**
A drone flies from coordinate position $P(-4, -2)$ to $Q(1, 10)$, with units in km. Find the magnitude of displacement.
1. Identify coordinates: $(x_1, y_1) = (-4, -2)$ and $(x_2, y_2) = (1, 10)$.
2. Write the formula: $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.
3. Substitute: $d = \sqrt{(1 - (-4))^2 + (10 - (-2))^2}$.
4. Simplify brackets (minus a minus is a plus): $d = \sqrt{(1 + 4)^2 + (10 + 2)^2} = \sqrt{5^2 + 12^2}$.
5. Square the numbers: $d = \sqrt{25 + 144} = \sqrt{169}$.
6. Calculate the final root: $d = 13\ \text{km}$.
7. State the answer: **$13\ \text{km}$**.

---

## Plotting graphs and drawing inferences from graphs

**Objective vi: plot graph and draw inference from the graph.**

Physics heavily relies on graphs to show the relationship between physical quantities. The two most common graphs related to position are the **Distance-time graph** and the **Position-time graph**. 

### Rules for plotting good graphs
1. **Axes:** Time (the independent variable) is almost always plotted on the horizontal x-axis. Distance/Position (the dependent variable) goes on the vertical y-axis.
2. **Scales:** Choose a scale that makes the graph large (covering at least half the page) and easy to read (e.g., $1\ \text{cm}$ represents $2\ \text{units}$, $5\ \text{units}$, or $10\ \text{units}$).
3. **Line of best fit:** Draw a smooth curve or a straight line through the points. Do not join points zig-zag.

### Inferences from the Slope (Gradient)
The slope of a graph tells us the rate at which the vertical quantity changes with respect to the horizontal quantity.
- **Slope formula:** $\text{Slope} = \frac{\Delta y}{\Delta x} = \frac{y_2 - y_1}{x_2 - x_1}$.
- **Distance-time graph:** The slope represents **speed**. 
  - A straight diagonal line means *constant speed*.
  - A horizontal flat line (zero slope) means the body is *stationary* (at rest).
  - A curve getting steeper means the body is *accelerating*.
- **Position (Displacement)-time graph:** The slope represents **velocity**. Velocity can be negative (if the object is moving back towards the origin), so a position-time graph can have a downward slope, whereas a distance-time graph can never slope downwards.

**Example 10: Finding speed from a distance-time graph**
A car's distance-time graph is a straight line passing through the origin $(0,0)$ and a point $(5\ \text{s}, 20\ \text{m})$. Find the speed of the car.
1. Identify the points on the graph: $(t_1, d_1) = (0, 0)$ and $(t_2, d_2) = (5, 20)$.
2. Write the slope formula for speed: $\text{Speed} = \frac{d_2 - d_1}{t_2 - t_1}$.
3. Substitute: $\text{Speed} = \frac{20\ \text{m} - 0\ \text{m}}{5\ \text{s} - 0\ \text{s}}$.
4. Calculate: $\text{Speed} = \frac{20}{5} = 4\ \text{m s}^{-1}$.
5. State the answer: **$4\ \text{m s}^{-1}$**.

**Example 11: Negative slope on a position-time graph**
A position-time graph for a bicycle shows a straight line connecting the points $(2\ \text{s}, 50\ \text{m})$ and $(7\ \text{s}, 0\ \text{m})$. Find its velocity.
1. Identify points on the graph: $(t_1, x_1) = (2, 50)$ and $(t_2, x_2) = (7, 0)$.
2. Write the slope formula for velocity: $v = \frac{x_2 - x_1}{t_2 - t_1}$.
3. Substitute: $v = \frac{0\ \text{m} - 50\ \text{m}}{7\ \text{s} - 2\ \text{s}}$.
4. Calculate: $v = \frac{-50}{5} = -10\ \text{m s}^{-1}$.
5. State the answer: **$-10\ \text{m s}^{-1}$** (the negative sign indicates motion back towards the origin).

**Example 12: Finding velocity between two intervals**
From a straight-line position-time graph, a car passes point $(1\ \text{s}, 15\ \text{m})$ and later point $(4\ \text{s}, 30\ \text{m})$. What is its constant velocity?
1. Points are $(1, 15)$ and $(4, 30)$.
2. Formula: $v = \frac{30\ \text{m} - 15\ \text{m}}{4\ \text{s} - 1\ \text{s}}$.
3. Calculate: $v = \frac{15}{3} = 5\ \text{m s}^{-1}$.
4. State the answer: **$5\ \text{m s}^{-1}$**.

---

## Key terms

| Term | Meaning |
| :--- | :--- |
| **Displacement** | The straight-line distance between an initial and final position in a specified direction (Vector). |
| **Distance** | The total length of the actual path travelled by a body (Scalar). |
| **Position** | The location of an object in space relative to a reference point or origin. |
| **Frame of Reference** | A system of coordinates or a physical environment from which motion is observed and measured. |
| **Zero Error** | A reading shown by a measuring instrument when it should be zero. It must be subtracted from observed readings. |
| **Vernier Caliper** | An instrument for measuring small lengths (inner/outer diameters, depth) accurate to $0.01\ \text{cm}$. |
| **Micrometer Screw Gauge** | An instrument for measuring very small thicknesses accurate to $0.01\ \text{mm}$. |
| **Cartesian Coordinates** | A system defining a point on a plane using an ordered pair $(x, y)$ corresponding to distances from two perpendicular axes. |

---

## Exam tips and common mistakes

- **Adding instead of subtracting zero error.** The correct formula is always: True reading = Observed - Zero error. If the zero error is negative (e.g., $-0.02$), you end up doing observed $- (-0.02)$, which becomes *addition*. Think carefully about the signs!
- **Mistaking distance for displacement.** Remember that an athlete running one full lap of a $400\ \text{m}$ track covers a distance of $400\ \text{m}$, but their displacement is **$0\ \text{m}$** because they returned to the starting point.
- **Squaring negative numbers incorrectly in coordinates.** When calculating distance between points, if you get $(y_2 - y_1) = -3$, remember that $(-3)^2 = +9$. A common student mistake is to write $-9$ and subtract it from the other term.
- **Forgetting units for instrument precision.** A vernier caliper measures to 2 decimal places in **cm** ($0.01\ \text{cm}$). A micrometer measures to 2 decimal places in **mm** ($0.01\ \text{mm}$). Do not mix up the units.
- **Misinterpreting graphs.** Remember: the slope of a distance-time graph is *speed*, but the slope of a position-time (or displacement-time) graph is *velocity*.

---

## Quick summary

1. Strings and metre rules are used for long or curved lengths. Calipers, vernier calipers (accuracy $0.01\ \text{cm}$), and micrometer screw gauges (accuracy $0.01\ \text{mm}$) are used for small and highly precise measurements.
2. The true reading of an instrument is its observed reading minus its zero error.
3. Distance is a scalar quantity (path length), while displacement is a vector quantity (straight-line distance in a specific direction).
4. Displacement in 2D space often forms a right-angled triangle, solved using the Pythagoras theorem for magnitude and trigonometry (tangent) for the bearing.
5. The Cartesian system locates points in a 2D plane using $(x,y)$ coordinates. The distance between them is $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$.
6. Position and motion are relative; they must be described relative to a specific frame of reference.
7. On a distance-time graph, a straight diagonal line means constant speed, a horizontal line means the body is at rest, and the slope equals the speed.

---

## Practice questions

**1. Which of the following instruments gives the most precise measurement of the diameter of a thin copper wire?**
- A. Metre rule
- B. Vernier calipers
- C. Micrometer screw gauge
- D. Engineer's outside calipers

**Answer: C.** The micrometer screw gauge has an accuracy of $0.01\ \text{mm}$, which is more precise than the vernier caliper ($0.1\ \text{mm}$) and the metre rule ($1\ \text{mm}$).

**2. A vernier caliper has a zero error of $-0.03\ \text{cm}$. If the measured reading on an object is $2.45\ \text{cm}$, the true reading is:**
- A. $2.42\ \text{cm}$
- B. $2.45\ \text{cm}$
- C. $2.48\ \text{cm}$
- D. $2.40\ \text{cm}$

**Answer: C.** 
1. Formula: $\text{True} = \text{Observed} - \text{Zero Error}$.
2. Substitute: $\text{True} = 2.45\ \text{cm} - (-0.03\ \text{cm})$.
3. Calculate: $2.45 + 0.03 = 2.48\ \text{cm}$. 
*Mistake behind A: Subtracting the value without recognizing the negative sign.*

**3. The main scale of a micrometer screw gauge reads $5.5\ \text{mm}$ and the thimble reading is 32. If there is a zero error of $+0.04\ \text{mm}$, what is the corrected reading?**
- A. $5.86\ \text{mm}$
- B. $5.82\ \text{mm}$
- C. $5.78\ \text{mm}$
- D. $5.54\ \text{mm}$

**Answer: C.**
1. Observed reading: $5.5\ \text{mm} + (32 \times 0.01\ \text{mm}) = 5.82\ \text{mm}$.
2. True reading: $5.82\ \text{mm} - (+0.04\ \text{mm})$.
3. Calculate: $5.78\ \text{mm}$.
*Mistake behind A: Adding a positive zero error instead of subtracting it.*

**4. Which of the following statements is true about displacement but NOT true about distance?**
- A. It is measured in metres.
- B. It depends on the path taken.
- C. It is the actual length of travel.
- D. It has a specified direction.

**Answer: D.** Displacement is a vector, meaning it requires a specified direction. Distance is a scalar and does not have a specified direction.

**5. A car travels halfway around a circular roundabout of radius $14\ \text{m}$. What is the distance travelled and the magnitude of its displacement? (Take $\pi = \frac{22}{7}$)**
- A. $44\ \text{m}$, $44\ \text{m}$
- B. $44\ \text{m}$, $28\ \text{m}$
- C. $28\ \text{m}$, $44\ \text{m}$
- D. $88\ \text{m}$, $28\ \text{m}$

**Answer: B.**
1. Distance (half circumference) $= \pi r = \frac{22}{7} \times 14\ \text{m} = 44\ \text{m}$.
2. Displacement (straight line across circle) $= \text{diameter} = 2 \times 14\ \text{m} = 28\ \text{m}$.
*Mistake behind D: Calculating the full circumference for distance instead of half.*

**6. A boy walks $8\ \text{km}$ due North, then $6\ \text{km}$ due East. What is his displacement from the starting point?**
- A. $14\ \text{km}$, $037^\circ$
- B. $10\ \text{km}$, $037^\circ$
- C. $10\ \text{km}$, $053^\circ$
- D. $14\ \text{km}$, $053^\circ$

**Answer: B.**
1. Magnitude: $d = \sqrt{8^2 + 6^2} = \sqrt{64 + 36} = \sqrt{100} = 10\ \text{km}$.
2. Direction (from North): Opposite is East ($6\ \text{km}$), Adjacent is North ($8\ \text{km}$).
3. $\tan \theta = \frac{6}{8} = 0.75$.
4. $\theta = \tan^{-1}(0.75) \approx 37^\circ$. (Bearing $037^\circ$).
*Mistake behind A: Adding the values as scalars ($8+6=14$) to find distance instead of vector displacement.*

**7. To accurately measure the length of a curvy road on a map, one should use:**
- A. A straight metre rule directly on the map
- B. A pair of engineer's calipers
- C. A string and a metre rule
- D. A micrometer screw gauge

**Answer: C.** A string is flexible and can be laid along the exact curves of the road, and then stretched straight to be measured against a metre rule.

**8. What is the distance between the points $A(-3, 2)$ and $B(5, -4)$ on a Cartesian plane?**
- A. $2\ \text{m}$
- B. $8\ \text{m}$
- C. $10\ \text{m}$
- D. $14\ \text{m}$

**Answer: C.**
1. $x_2 - x_1 = 5 - (-3) = 8$.
2. $y_2 - y_1 = -4 - 2 = -6$.
3. $d = \sqrt{8^2 + (-6)^2} = \sqrt{64 + 36} = \sqrt{100}$.
4. $d = 10\ \text{m}$.
*Mistake behind D: Simply adding the differences $8 + 6 = 14$ instead of using the Pythagoras square root formula.*

**9. A straight-line distance-time graph that passes through the origin implies that the body is:**
- A. accelerating uniformly
- B. moving with constant speed
- C. at rest
- D. decelerating

**Answer: B.** A straight line with a steady slope on a distance-time graph shows that distance is changing at a constant rate, which means the speed is constant.

**10. Two moving objects can only be said to be truly moving or at rest when compared against a background or coordinate system. This concept in physics is referred to as:**
- A. Degree of accuracy
- B. Frame of reference
- C. Cartesian plane
- D. Vector resolution

**Answer: B.** A frame of reference is the environment or coordinate system from which an observer measures position and motion.
