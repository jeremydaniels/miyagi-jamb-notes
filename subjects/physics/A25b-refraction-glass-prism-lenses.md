# JAMB Physics Notes: Refraction Through Glass Prisms and Lenses

## What JAMB expects

This topic is part of Section A, Topic 25 of the JAMB Physics syllabus. It covers the refraction of light through glass prisms and curved surfaces (lenses). Because refraction is a very broad topic, it is split across multiple files. The basic laws of refraction, Snell's law, real and apparent depth, and total internal reflection are covered in `A25a-refraction-at-plane-surfaces.md`. Optical instruments are covered in `A26-optical-instruments.md`. This file covers prisms and lenses.

This file covers the content item **(b) Glass Prism**:
- (i) use of the minimum deviation formula
- (ii) type of lenses; triangular, rectangular etc.
- (iii) use of lens formula and Newton's formula
- (v) magnification

By the end of these notes, you should be able to:
- iii. determine the focal length of curved surfaces;
- viii. use of lens formula and ray diagrams to solve optical numerical problems;
- ix. determine the magnification of an image;
- x. calculate the refractive index of a glass prism using minimum deviation formula;
- xi. ray tracing through an optical prism.

**Note on the syllabus wording:** 
- The syllabus item (b)(ii) reads "type of lenses; triangular, rectangular etc." Traditionally, optical glass shapes are called *rectangular glass blocks*, *triangular glass prisms*, and spherical *lenses* (convex or concave). We will explain the shapes of glass media, but focus heavily on convex and concave lenses as they are the true "curved surfaces" JAMB tests you on.
- The syllabus writes "Newton's formular ($F^2 = ab$)". This contains a typing error for "formula". We will use the standard JAMB notation $f^2 = ab$ (often written with lowercase $f$).
- The numbering in the syllabus skips item (iv) under section (b).

## Glass Prism

A **glass prism** is a solid piece of transparent glass with flat, polished surfaces that refract light. Prisms and lenses are the main optical components used to control light in instruments.

### Type of lenses; triangular, rectangular etc.

When light passes from air into a block of glass, it bends (refracts) because light travels slower in glass than in air. The shape of the glass determines how the light behaves as it enters and leaves. 

Glass optical components come in several distinct shapes:
1. **Rectangular Glass Blocks:** The opposite faces are parallel. A ray of light entering a rectangular block emerges parallel to its original path, but slightly shifted to the side (this is called lateral displacement).
2. **Triangular Glass Prisms:** A block of glass with a triangular cross-section. Because the refracting faces are not parallel, a ray of light is bent towards the thickest part (the base) of the prism. 
3. **Curved Lenses:** True lenses have at least one curved (usually spherical) surface. There are two main types:
   - **Convex (Converging) Lenses:** Thicker in the middle than at the edges. They bend parallel rays of light inward so that they meet at a focal point.
   - **Concave (Diverging) Lenses:** Thinner in the middle than at the edges. They spread parallel rays of light outward so they appear to diverge from a point.

### Ray tracing through an optical prism

When a ray of monochromatic light (light of a single colour, like from a red laser) passes through a triangular glass prism, it is refracted twice: once when entering the glass, and once when leaving the glass. 

**Procedure for ray tracing:**
1. A triangular glass prism is placed on a sheet of white paper and its outline is traced.
2. A straight line is drawn at an angle to one face to represent the **incident ray**. Two pins are stuck vertically on this line.
3. Looking horizontally through the opposite face of the prism, the experimenter places two more pins so they appear to line up exactly with the images of the first two pins. 
4. The line joining these new pins is drawn to represent the **emergent ray**.

**Key angles in a prism:**
- **Angle of Incidence ($i$):** The angle between the incident ray and the normal (a line drawn at $90^\circ$ to the glass surface).
- **Angle of Emergence ($e$):** The angle between the emergent ray and the normal on the other side.
- **Refracting Angle ($A$):** The top angle of the prism where the two refracting faces meet.
- **Angle of Deviation ($D$):** The angle between the original path of the incident ray and the final path of the emergent ray. It measures how much the light has been "bent" out of its original path.

[IMAGE: A ray diagram showing a single ray of light passing through a triangular glass prism. The ray strikes the left face at angle $i$ to the dashed normal line, bends towards the normal inside the glass, and hits the right face. It emerges, bending away from the normal at angle $e$. Dotted lines extend the initial incident ray forward and the final emergent ray backward to show the angle of deviation $D$ where they cross. The top angle of the prism is labelled $A$. Clean flat textbook illustration, white background.]

*Note: If white light is used instead of monochromatic light, the prism will separate it into its component colours (dispersion) because different colours bend by different amounts. This is covered fully in `A27-dispersion-and-electromagnetic-spectrum.md`.*

### Use of the minimum deviation formula

If you gradually increase the angle of incidence ($i$) and measure the corresponding angle of deviation ($D$), you will find that $D$ first decreases, reaches a minimum value, and then starts to increase again. This forms a U-shaped graph. 

The lowest point on this graph is called the **Angle of Minimum Deviation ($D_m$)**. 

At the position of minimum deviation, the light passes through the prism perfectly symmetrically. This means:
1. The angle of incidence equals the angle of emergence ($i = e$).
2. The refracted ray inside the glass travels perfectly parallel to the base of the prism (assuming the prism is isosceles or equilateral).
3. The angles of refraction at both boundaries inside the prism are equal ($r_1 = r_2$).

At this special point, the refractive index ($n$) of the glass can be calculated using the **minimum deviation formula**:
$$n = \frac{\sin\left(\frac{A + D_m}{2}\right)}{\sin\left(\frac{A}{2}\right)}$$

where:
- $n$ is the refractive index of the prism (no units).
- $A$ is the refracting angle of the prism (in degrees).
- $D_m$ is the angle of minimum deviation (in degrees).

### Calculating the refractive index of a glass prism using the minimum deviation formula

Here is how JAMB tests calculations using the minimum deviation formula. 

**Worked Example 1: Finding refractive index**
**Question:** An equilateral glass prism has an angle of minimum deviation of $30^\circ$. Calculate the refractive index of the glass. (Assume $\sin 45^\circ = 0.7071$ and $\sin 30^\circ = 0.5000$).
**Working:**
1. State the known values: Because it is an equilateral prism, the refracting angle $A = 60^\circ$. The minimum deviation $D_m = 30^\circ$.
2. Write the formula: $n = \frac{\sin[(A + D_m)/2]}{\sin[A/2]}$.
3. Substitute the values: $n = \frac{\sin[(60^\circ + 30^\circ)/2]}{\sin[60^\circ/2]}$.
4. Simplify the angles: $n = \frac{\sin(90^\circ/2)}{\sin(30^\circ)} = \frac{\sin(45^\circ)}{\sin(30^\circ)}$.
5. Calculate the final answer: $n = \frac{0.7071}{0.5000} = 1.414$.
**Answer:** The refractive index is $1.41$ (no units).

**Worked Example 2: Finding minimum deviation from refractive index**
**Question:** A triangular prism of refracting angle $60^\circ$ is made of glass of refractive index $\sqrt{3}$. Calculate its angle of minimum deviation.
**Working:**
1. State the known values: $A = 60^\circ$, $n = \sqrt{3}$.
2. Write the formula: $n = \frac{\sin[(A + D_m)/2]}{\sin[A/2]}$.
3. Substitute the values: $\sqrt{3} = \frac{\sin[(60^\circ + D_m)/2]}{\sin[60^\circ/2]}$.
4. Simplify the denominator: $\sin(30^\circ) = 0.5 = \frac{1}{2}$. Thus, $\sqrt{3} = \frac{\sin[(60^\circ + D_m)/2]}{0.5}$.
5. Multiply both sides by $0.5$: $\frac{\sqrt{3}}{2} = \sin\left(\frac{60^\circ + D_m}{2}\right)$.
6. Find the inverse sine. We know from trigonometry that $\sin(60^\circ) = \frac{\sqrt{3}}{2}$, so: $60^\circ = \frac{60^\circ + D_m}{2}$.
7. Solve for $D_m$: $120^\circ = 60^\circ + D_m \implies D_m = 120^\circ - 60^\circ = 60^\circ$.
**Answer:** The angle of minimum deviation is $60^\circ$.

**Worked Example 3: The thin prism approximation**
If a prism is very thin (refracting angle $A$ is small, usually less than $10^\circ$), the sines in the formula can be approximated directly to the angles in radians. This simplifies to the **thin prism formula**: 
$$D = (n - 1)A$$
**Question:** A thin glass prism has a refracting angle of $4^\circ$ and a refractive index of $1.5$. Calculate the angle of deviation.
**Working:**
1. State the known values: $A = 4^\circ$, $n = 1.5$.
2. Write the thin prism formula: $D = (n - 1)A$.
3. Substitute the values: $D = (1.5 - 1) \times 4^\circ$.
4. Calculate: $D = 0.5 \times 4^\circ = 2.0^\circ$.
**Answer:** The deviation is $2.0^\circ$.

### Determination of focal length of curved surfaces

A spherical lens has several key features:
- **Principal Axis:** The imaginary straight line passing symmetrically through the center of the lens.
- **Optical Centre ($C$):** The exact geometric center of the lens. A ray of light passing through the optical centre goes straight through without being bent.
- **Principal Focus ($F$):** For a convex lens, it is the point on the principal axis where rays parallel to the axis converge after passing through the lens. For a concave lens, it is the point from which parallel rays appear to diverge.
- **Focal Length ($f$):** The distance between the optical centre and the principal focus.

**How to determine the focal length experimentally:**
1. **Focusing a distant object (Rough method):** Hold a convex lens facing a distant, brightly lit object (like a distant pole or a tree outside). Place a white screen behind the lens and move it back and forth until a sharp, inverted image of the tree forms on the screen. Because the object is very far away (effectively at infinity), the image forms exactly at the principal focus. The distance between the lens and the screen is measured with a ruler; this distance is the focal length, $f$.
2. **Illuminated object and plane mirror (No parallax method):** Place a plane mirror flat on a table and lay a convex lens directly on it. Clamp a pin (the object) horizontally above the lens on a retort stand. Look down from above and move the pin up and down until the pin and its inverted image (reflected back up by the mirror) lie at exactly the same height with no parallax (they move together when you shift your head side to side). The distance from the pin to the lens is the focal length, $f$.
3. **Using the lens formula:** Measure the object distance ($u$) and the corresponding sharp image distance ($v$) on a screen for various positions. Use a graph of $\frac{1}{v}$ against $\frac{1}{u}$ (which yields straight line intercepts of $\frac{1}{f}$) or the lens formula to calculate $f$. 

### Using the lens formula and ray diagrams to solve optical numerical problems

To understand where an image will form, we draw ray diagrams using two standard rules:
1. A ray traveling parallel to the principal axis bends through the lens and passes through the principal focus ($F$).
2. A ray traveling directly through the optical centre ($C$) passes straight through without bending.

Where these two rays cross, the image is formed.
- **Real image:** Formed when light rays actually meet. It can be captured on a screen and is always inverted (upside down).
- **Virtual image:** Formed when light rays only *appear* to meet (they spread apart on the far side, so we must trace them backward with dotted lines). It cannot be caught on a screen and is always erect (upright).

[IMAGE: Two ray diagrams side by side. Left: A convex lens with an upright arrow object placed beyond 2F. A ray parallel to the axis passes through F on the right; a ray through the optical center goes straight. They meet between F and 2F on the right, forming a real, inverted, diminished arrow image. Right: A concave lens with an upright arrow object. A ray parallel to the axis diverges as if coming from F on the left; a ray through the center goes straight. Dotted lines trace back to intersect on the left side, forming a virtual, erect, diminished arrow image. Clean flat textbook style, white background.]

#### Sign Convention

To calculate exact positions, we use formulas. You must obey a **Sign Convention**. In Nigerian secondary schools and JAMB exams, the standard convention is **"Real is Positive"**.
- $u$ (object distance from optical centre) is positive for real objects.
- $v$ (image distance from optical centre) is **positive for real images**, and **negative for virtual images**.
- $f$ (focal length) is **positive for convex (converging) lenses**, and **negative for concave (diverging) lenses**.

*(Note: Some modern textbooks use the Cartesian sign convention where distances to the left are negative. JAMB questions are traditionally designed around the "Real is Positive" convention, which we use exclusively here to prevent confusion).*

### Use of lens formula and Newton's formula

**1. The Lens Formula:**
$$\frac{1}{f} = \frac{1}{u} + \frac{1}{v}$$
where:
- $f$ = focal length (in $\text{m}$ or $\text{cm}$)
- $u$ = object distance (in $\text{m}$ or $\text{cm}$)
- $v$ = image distance (in $\text{m}$ or $\text{cm}$)

**2. Newton's Formula:**
A useful shortcut for convex lenses when distances are given from the *principal focus* rather than the optical centre. JAMB lists this as $F^2 = ab$.
$$f^2 = ab$$
where:
- $f$ = focal length (in $\text{m}$ or $\text{cm}$)
- $a$ = distance of the object from the focus ($a = u - f$)
- $b$ = distance of the image from the focus ($b = v - f$)

**Worked Example 4: Convex lens standard calculation**
**Question:** An object is placed $20\text{ cm}$ from a convex lens of focal length $15\text{ cm}$. Find the image distance and state the nature of the image.
**Working:**
1. Identify knowns: A convex lens means $f = +15\text{ cm}$. Object distance $u = +20\text{ cm}$.
2. Write the formula: $\frac{1}{f} = \frac{1}{u} + \frac{1}{v}$.
3. Substitute values: $\frac{1}{15\text{ cm}} = \frac{1}{20\text{ cm}} + \frac{1}{v}$.
4. Rearrange for $v$: $\frac{1}{v} = \frac{1}{15} - \frac{1}{20}$.
5. Find a common denominator ($60$): $\frac{1}{v} = \frac{4}{60} - \frac{3}{60} = \frac{1}{60}\text{ cm}^{-1}$.
6. Invert both sides: $v = +60\text{ cm}$.
**Answer:** The image is $60\text{ cm}$ from the lens. Because $v$ is positive, it is a **real and inverted** image.

**Worked Example 5: Using Newton's Formula**
**Question:** Let's solve the exact same setup as Example 4, but using Newton's formula. An object is placed $20\text{ cm}$ from a convex lens of focal length $15\text{ cm}$. Find the image distance from the lens.
**Working:**
1. Identify $f$: $f = 15\text{ cm}$.
2. Calculate $a$ (distance of object from focus): $a = u - f = 20\text{ cm} - 15\text{ cm} = 5\text{ cm}$.
3. Write Newton's formula: $f^2 = ab$.
4. Substitute values: $(15\text{ cm})^2 = 5\text{ cm} \times b$.
5. Calculate $b$: $225\text{ cm}^2 = 5\text{ cm} \times b \implies b = \frac{225}{5} = 45\text{ cm}$.
6. Remember $b$ is the distance from the focus. To find $v$ (distance from the lens), add $f$: $v = f + b = 15\text{ cm} + 45\text{ cm} = 60\text{ cm}$.
**Answer:** The image is $60\text{ cm}$ from the lens. (This perfectly matches the standard formula).

**Worked Example 6: Concave lens calculation**
**Question:** An object is placed $30\text{ cm}$ from a concave lens of focal length $15\text{ cm}$. Calculate the image distance.
**Working:**
1. Identify knowns: Concave lens means $f$ MUST be negative. $f = -15\text{ cm}$. $u = +30\text{ cm}$.
2. Write the formula: $\frac{1}{v} = \frac{1}{f} - \frac{1}{u}$.
3. Substitute values: $\frac{1}{v} = \frac{1}{-15\text{ cm}} - \frac{1}{30\text{ cm}}$.
4. Find a common denominator ($30$): $\frac{1}{v} = \frac{-2}{30} - \frac{1}{30} = \frac{-3}{30}\text{ cm}^{-1}$.
5. Simplify: $\frac{1}{v} = \frac{-1}{10}\text{ cm}^{-1}$.
6. Invert both sides: $v = -10\text{ cm}$.
**Answer:** The image distance is $10\text{ cm}$. The negative sign means it is a **virtual** image, formed on the same side as the object.

### Magnification

Magnification ($m$) tells us how many times larger or smaller the image is compared to the object. It is a ratio and therefore has no units.

Formula for linear magnification:
$$m = \frac{\text{Height of image }(h_i)}{\text{Height of object }(h_o)} = \frac{\text{Image distance }(v)}{\text{Object distance }(u)}$$

By combining the magnification formula ($v = mu$) with the lens formula ($\frac{1}{f} = \frac{1}{u} + \frac{1}{v}$), we can derive very useful shortcuts for JAMB calculations:
$$m = \frac{v}{f} - 1 \quad \text{or} \quad m = \frac{f}{u - f}$$

*(Note: When using these shortcuts with the "Real is Positive" convention, remember that $v$ will be negative for a virtual image, which might change the sign of your magnification depending on how you substitute. It is often safer to stick to the basic lens formula unless you are very confident with your signs.)*

### Determining the magnification of an image

Let's solve standard optical problems applying magnification rules.

**Worked Example 7: Finding object distance given magnification**
**Question:** A convex lens of focal length $20\text{ cm}$ forms a real image that is $4$ times the size of the object. How far is the object from the lens?
**Working:**
1. Identify knowns: $f = +20\text{ cm}$. Magnification $m = 4$. Real image means $v$ is positive.
2. Relate $v$ and $u$: $m = \frac{v}{u} \implies 4 = \frac{v}{u} \implies v = 4u$.
3. Write the lens formula: $\frac{1}{f} = \frac{1}{u} + \frac{1}{v}$.
4. Substitute $v$: $\frac{1}{20} = \frac{1}{u} + \frac{1}{4u}$.
5. Add the fractions using a common denominator of $4u$: $\frac{1}{20} = \frac{4}{4u} + \frac{1}{4u} = \frac{5}{4u}$.
6. Cross-multiply: $4u \times 1 = 20 \times 5 \implies 4u = 100\text{ cm}$.
7. Solve for $u$: $u = \frac{100}{4} = 25\text{ cm}$.
**Answer:** The object is $25\text{ cm}$ from the lens.

**Worked Example 8: Finding image height**
**Question:** A concave lens with a focal length of $10\text{ cm}$ forms an image of a pin which is placed $15\text{ cm}$ away. If the pin is $5\text{ cm}$ tall, determine the height of the image.
**Working:**
1. Find $v$ first. Concave lens means $f = -10\text{ cm}$. $u = +15\text{ cm}$.
2. Formula: $\frac{1}{v} = \frac{1}{f} - \frac{1}{u} = \frac{1}{-10} - \frac{1}{15} = \frac{-3}{30} - \frac{2}{30} = \frac{-5}{30}\text{ cm}^{-1} = \frac{-1}{6}\text{ cm}^{-1}$.
3. Invert to find $v$: $v = -6\text{ cm}$.
4. Find magnification (using absolute values for distance): $m = \frac{|v|}{u} = \frac{6\text{ cm}}{15\text{ cm}} = 0.4$.
5. Use magnification to find image height: $m = \frac{h_i}{h_o} \implies 0.4 = \frac{h_i}{5\text{ cm}}$.
6. Solve for $h_i$: $h_i = 0.4 \times 5\text{ cm} = 2.0\text{ cm}$.
**Answer:** The image height is $2.0\text{ cm}$. (Because it is a concave lens, the image is always virtual, erect, and diminished).

**Worked Example 9: Virtual image from a convex lens**
**Question:** A convex lens has a focal length of $10\text{ cm}$. An object is placed $5\text{ cm}$ from it. Find the magnification of the image.
**Working:**
1. Identify knowns: Convex lens $f = +10\text{ cm}$, $u = +5\text{ cm}$.
2. Find $v$: $\frac{1}{v} = \frac{1}{f} - \frac{1}{u} = \frac{1}{10} - \frac{1}{5} = \frac{1}{10} - \frac{2}{10} = \frac{-1}{10}\text{ cm}^{-1}$.
3. Invert for $v$: $v = -10\text{ cm}$. The image is virtual.
4. Calculate magnification: $m = \frac{|v|}{u} = \frac{10\text{ cm}}{5\text{ cm}} = 2$.
**Answer:** The magnification is $2$.

## Key terms

| Term | Meaning |
| --- | --- |
| **Glass Prism** | A transparent block, usually with a triangular cross-section, used to refract or disperse light. |
| **Angle of Deviation ($D$)** | The angle between the original path of an incident ray and the final path of the emergent ray. |
| **Minimum Deviation ($D_m$)** | The smallest angle of deviation achievable by a specific prism. Occurs symmetrically when $i = e$. |
| **Convex Lens** | A converging lens, thicker in the middle. Forms real or virtual images depending on object distance. |
| **Concave Lens** | A diverging lens, thinner in the middle. Forms only virtual, erect, and diminished images. |
| **Optical Centre ($C$)** | The exact geometric center of a lens. Light passing through it does not deviate. |
| **Principal Focus ($F$)** | The point where rays parallel to the principal axis converge (convex) or appear to diverge from (concave). |
| **Focal Length ($f$)** | The distance between the optical centre and the principal focus. |
| **Real Image** | An image formed by the actual intersection of light rays; can be caught on a physical screen. |
| **Virtual Image** | An image formed where light rays only appear to originate; cannot be caught on a screen. |
| **Magnification ($m$)** | The ratio of the image height to the object height, or image distance to object distance ($v/u$). |

## Exam tips and common mistakes

- **Sign errors are the most common mistake in optics calculations.** Using the "Real is Positive" convention: ALWAYS make $f$ negative for concave lenses. ALWAYS make $v$ negative when the question states the image is virtual.
- **Don't forget to invert the final fraction.** In the lens formula, solving to get $\frac{1}{v} = \frac{1}{60\text{ cm}}$ means $v = 60\text{ cm}$. Students often rush, stop at the fraction, and mistakenly pick an option like $0.016\text{ cm}$.
- **Newton's formula ($f^2 = ab$) variables.** Remember that $a$ and $b$ are distances from the **focus**, not from the lens. If a question asks for the distance of the image from the *lens* ($v$), you must add the focal length to $b$ ($v = f + b$).
- **Minimum deviation conditions.** JAMB often tests this theoretically. Remember: at minimum deviation, angle of incidence equals angle of emergence, and the ray inside the prism is parallel to the base.
- **Concave lens properties.** A concave lens ALWAYS produces an image that is Virtual, Erect, and Diminished, no matter where you place the real object. If a question describes a magnified virtual image, it MUST be from a convex lens (acting as a magnifying glass).

## Quick summary

1. A triangular glass prism refracts and deviates light. The angle of deviation ($D$) is minimum when the angle of incidence equals the angle of emergence.
2. The refractive index of a prism can be found using the minimum deviation formula: $n = \frac{\sin[(A + D_m)/2]}{\sin[A/2]}$. For very thin prisms, $D = (n-1)A$.
3. Convex lenses are converging and have a positive focal length; concave lenses are diverging and have a negative focal length.
4. Ray tracing rules state that a ray parallel to the principal axis passes through the focus, and a ray passing through the optical centre is undeviated.
5. In the "Real is positive" sign convention, real objects and images have positive distances, while virtual images have negative distances.
6. The lens formula is $\frac{1}{f} = \frac{1}{u} + \frac{1}{v}$ and Newton's formula is $f^2 = ab$.
7. Magnification ($m$) is the ratio of image size to object size, given by $m = \frac{v}{u}$ or $m = \frac{h_i}{h_o}$.

## Practice questions

**1. An equilateral glass prism has an angle of minimum deviation of $30^\circ$. Calculate its refractive index. (Assume $\sin 45^\circ = 0.707$ and $\sin 30^\circ = 0.500$).**
- A. $1.00$
- B. $1.41$
- C. $1.50$
- D. $1.73$

**Answer: B.**
1. Identify the given values: Refracting angle for an equilateral prism $A = 60^\circ$, minimum deviation $D_m = 30^\circ$.
2. Write the minimum deviation formula: $n = \frac{\sin[(A + D_m)/2]}{\sin[A/2]}$.
3. Substitute the values: $n = \frac{\sin[(60^\circ + 30^\circ)/2]}{\sin[60^\circ/2]} = \frac{\sin(45^\circ)}{\sin(30^\circ)}$.
4. Insert the sine values: $n = \frac{0.707}{0.500}$.
5. Evaluate the final answer: $n = 1.414 \approx 1.41$.
The most tempting wrong option is C ($1.50$), which comes from the mistake of ignoring the sines entirely and just dividing $(60^\circ + 30^\circ) / 60^\circ = 1.50$.

**2. An object is placed $10\text{ cm}$ from a convex lens of focal length $15\text{ cm}$. Calculate the image distance.**
- A. $30\text{ cm}$
- B. $-30\text{ cm}$
- C. $6\text{ cm}$
- D. $-6\text{ cm}$

**Answer: B.**
1. State the knowns: Convex lens means $f = +15\text{ cm}$. Object distance $u = +10\text{ cm}$.
2. Write the lens formula rearranged for $v$: $\frac{1}{v} = \frac{1}{f} - \frac{1}{u}$.
3. Substitute the values: $\frac{1}{v} = \frac{1}{15} - \frac{1}{10}$.
4. Find a common denominator ($30$): $\frac{1}{v} = \frac{2}{30} - \frac{3}{30} = \frac{-1}{30}\text{ cm}^{-1}$.
5. Invert to find $v$: $v = -30\text{ cm}$.
The most tempting wrong option is A ($30\text{ cm}$), which comes from ignoring the negative sign, incorrectly assuming the image is real when an object placed closer than the focal length of a convex lens produces a virtual image.

**3. Using Newton's formula, calculate the focal length of a lens if an object is $4\text{ cm}$ from the principal focus and its real image is $9\text{ cm}$ from the principal focus on the other side.**
- A. $36\text{ cm}$
- B. $13\text{ cm}$
- C. $6\text{ cm}$
- D. $5\text{ cm}$

**Answer: C.**
1. State the knowns: Object distance from focus $a = 4\text{ cm}$. Image distance from focus $b = 9\text{ cm}$.
2. Write Newton's formula: $f^2 = ab$.
3. Substitute the values: $f^2 = 4\text{ cm} \times 9\text{ cm}$.
4. Multiply: $f^2 = 36\text{ cm}^2$.
5. Find the square root: $f = \sqrt{36} = 6\text{ cm}$.
The most tempting wrong option is A ($36\text{ cm}$), which comes from the mistake of forgetting to find the square root of $ab$ at the final step.

**4. A convex lens of focal length $20\text{ cm}$ forms a real image that is twice the size of the object. Determine the distance of the object from the lens.**
- A. $10\text{ cm}$
- B. $30\text{ cm}$
- C. $40\text{ cm}$
- D. $60\text{ cm}$

**Answer: B.**
1. State the knowns: Magnification $m = 2$. Real image means $v$ is positive, so $v = 2u$. $f = +20\text{ cm}$.
2. Write the lens formula: $\frac{1}{f} = \frac{1}{u} + \frac{1}{v}$.
3. Substitute $v$ and $f$: $\frac{1}{20} = \frac{1}{u} + \frac{1}{2u}$.
4. Find a common denominator: $\frac{1}{20} = \frac{2}{2u} + \frac{1}{2u} = \frac{3}{2u}$.
5. Cross multiply: $2u = 60\text{ cm}$.
6. Solve for $u$: $u = \frac{60}{2} = 30\text{ cm}$.
The most tempting wrong option is A ($10\text{ cm}$), which comes from the mistake of treating the image as virtual ($v = -2u$), which gives $\frac{1}{20} = \frac{1}{u} - \frac{1}{2u} = \frac{1}{2u} \implies u = 10\text{ cm}$.

**5. An object is placed $20\text{ cm}$ from a concave lens of focal length $20\text{ cm}$. The magnification produced is:**
- A. $0.5$
- B. $1.0$
- C. $2.0$
- D. Infinity

**Answer: A.**
1. State the knowns: Concave lens means $f = -20\text{ cm}$. Object distance $u = +20\text{ cm}$.
2. Use the lens formula to find $v$: $\frac{1}{v} = \frac{1}{f} - \frac{1}{u} = \frac{1}{-20} - \frac{1}{20}$.
3. Add the fractions: $\frac{1}{v} = \frac{-2}{20} = \frac{-1}{10}\text{ cm}^{-1}$.
4. Invert to find $v$: $v = -10\text{ cm}$.
5. Calculate magnification: $m = \frac{|v|}{u} = \frac{10}{20} = 0.5$.
The most tempting wrong option is D (Infinity), which comes from the mistake of forgetting the negative sign for the concave lens focal length, giving $\frac{1}{v} = \frac{1}{20} - \frac{1}{20} = 0$, causing $v$ to equal infinity.

**6. A glass prism with a refracting angle of $60^\circ$ has a refractive index of $\sqrt{3}$. What is its angle of minimum deviation?**
- A. $30^\circ$
- B. $45^\circ$
- C. $60^\circ$
- D. $90^\circ$

**Answer: C.**
1. State the formula: $n = \frac{\sin[(A + D_m)/2]}{\sin[A/2]}$.
2. Substitute knowns ($A=60^\circ, n=\sqrt{3}$): $\sqrt{3} = \frac{\sin[(60^\circ + D_m)/2]}{\sin(30^\circ)}$.
3. Insert $\sin(30^\circ) = 0.5$: $\sqrt{3} = \frac{\sin[(60^\circ + D_m)/2]}{0.5}$.
4. Multiply by $0.5$: $\frac{\sqrt{3}}{2} = \sin\left(\frac{60^\circ + D_m}{2}\right)$.
5. Since $\sin(60^\circ) = \frac{\sqrt{3}}{2}$, equate the angles: $60^\circ = \frac{60^\circ + D_m}{2}$.
6. Solve for $D_m$: $120^\circ = 60^\circ + D_m \implies D_m = 60^\circ$.
The most tempting wrong option is A ($30^\circ$), which students often pick by confusing the final angle $60^\circ$ with the $(A+D_m)/2$ term and improperly halving it again.

**7. A thin prism of refracting angle $4^\circ$ is made of glass of refractive index $1.5$. Calculate the angle of deviation.**
- A. $1.0^\circ$
- B. $2.0^\circ$
- C. $4.0^\circ$
- D. $6.0^\circ$

**Answer: B.**
1. State the given values: $A = 4^\circ$, $n = 1.5$.
2. Recall the formula for a thin prism: $D = (n - 1)A$.
3. Substitute the values: $D = (1.5 - 1) \times 4^\circ$.
4. Multiply: $D = 0.5 \times 4^\circ = 2.0^\circ$.
The most tempting wrong option is D ($6.0^\circ$), which comes from the mistake of multiplying $n \times A$ ($1.5 \times 4$) rather than $(n-1) \times A$.

**8. An object $5\text{ cm}$ tall is placed $15\text{ cm}$ away from a concave lens of focal length $10\text{ cm}$. Determine the height of the image.**
- A. $2.0\text{ cm}$
- B. $3.3\text{ cm}$
- C. $7.5\text{ cm}$
- D. $10.0\text{ cm}$

**Answer: A.**
1. State the knowns: Concave lens $f = -10\text{ cm}$, $u = 15\text{ cm}$, $h_o = 5\text{ cm}$.
2. Find $v$ using the lens formula: $\frac{1}{v} = \frac{1}{-10} - \frac{1}{15}$.
3. Find a common denominator ($30$): $\frac{1}{v} = \frac{-3}{30} - \frac{2}{30} = \frac{-5}{30}\text{ cm}^{-1}$.
4. Invert to find $v$: $v = \frac{-30}{5} = -6\text{ cm}$.
5. Find the linear magnification: $m = \frac{|v|}{u} = \frac{6}{15} = 0.4$.
6. Calculate image height: $h_i = m \times h_o = 0.4 \times 5\text{ cm} = 2.0\text{ cm}$.
The most tempting wrong option is D ($10.0\text{ cm}$), which comes from incorrectly using a positive focal length ($f = +10\text{ cm}$), which would give $v = 30\text{ cm}$, $m = 2$, and $h_i = 10\text{ cm}$.

**9. At the position of minimum deviation in a triangular glass prism, the light ray passes symmetrically. Which of the following conditions is mathematically true?**
- A. $i = A$
- B. $i = e$
- C. $D_m = i + e$
- D. $r = A$

**Answer: B.**
1. Recognize the rules of minimum deviation: light travels symmetrically through the prism.
2. The angle of incidence ($i$) on the first face must exactly equal the angle of emergence ($e$) on the second face.
3. Therefore, $i = e$ is the correct mathematical condition.
The most tempting wrong option is C ($D_m = i + e$), which is a corrupted version of the true general prism formula $D = (i + e) - A$.

**10. A convex lens forms a virtual image $3$ times the size of an object. If the focal length of the lens is $15\text{ cm}$, find the object distance.**
- A. $5\text{ cm}$
- B. $10\text{ cm}$
- C. $20\text{ cm}$
- D. $30\text{ cm}$

**Answer: B.**
1. State the knowns: Convex lens $f = +15\text{ cm}$. Virtual image means $v$ is negative.
2. Formulate the relationship between $v$ and $u$: $m = 3 \implies v = -3u$.
3. Write the lens formula: $\frac{1}{f} = \frac{1}{u} + \frac{1}{v}$.
4. Substitute $f$ and $v$: $\frac{1}{15} = \frac{1}{u} - \frac{1}{3u}$.
5. Simplify the right side: $\frac{1}{15} = \frac{3}{3u} - \frac{1}{3u} = \frac{2}{3u}$.
6. Cross-multiply: $3u = 30\text{ cm}$.
7. Solve for $u$: $u = 10\text{ cm}$.
The most tempting wrong option is C ($20\text{ cm}$), which comes from the mistake of assuming the image is real ($v = +3u$), which would give $\frac{1}{15} = \frac{4}{3u} \implies 3u = 60 \implies u = 20\text{ cm}$.
