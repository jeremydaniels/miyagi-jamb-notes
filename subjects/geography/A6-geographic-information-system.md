# JAMB Geography Notes: Geographic Information System (GIS)

## What JAMB expects

This topic is Part I, Topic F of the JAMB Geography syllabus: Geographic Information System (GIS).

By the end of these notes, you should be able to:
1. Understand GIS and its uses.
2. Understand the basic concepts and components.
3. Express locations through the use of latitudes, longitudes, zipcodes etc.
4. Understand land surveying, remote sensing, map digitizing, map scanning as sources of data.
5. Explain areas of use: Defense, Agriculture, Rural Development etc.
6. Identify problems with GIS in Nigeria.

## What is a Geographic Information System (GIS) and its uses?

**Objective i: understand GIS and its uses.**

A **Geographic Information System (GIS)** is a computer-based system designed to capture, store, manipulate, analyze, manage, and present geographic or spatial data. 

Unlike traditional paper maps, which are static (cannot be changed easily once printed), a GIS is dynamic. It links locations on the Earth's surface with detailed information about those locations. For example, while a paper map simply shows a dot for a school, a GIS can tell you the school's name, its number of students, its exam results, and how close it is to a major road.

**Uses of GIS:**
At a general level, GIS is used to:
- **Map where things are:** showing the locations of features like rivers, roads, and cities.
- **Map quantities:** finding areas with high or low populations, rainfall, or disease outbreaks.
- **Find what is nearby:** calculating how many houses are within 2 kilometres of a flooded river.
- **Track changes over time:** comparing satellite images from 2010 and 2024 to see how much of a forest in cross River State has been cut down.

## Basic concepts and components of GIS

**Objective ii: understand the basic concepts and components.**

### 1. Basic concepts of GIS

To understand how GIS works, you must understand a few core concepts:

**Spatial and Attribute Data**
Every feature in a GIS has two types of data attached to it:
- **Spatial data (The "Where"):** This represents the exact location and shape of a feature on the Earth's surface, using coordinates. 
- **Attribute data (The "What"):** This is the descriptive information or statistics about the feature. For example, if the spatial data is the location of a road, the attribute data might include the road's name (e.g., Lagos-Ibadan Expressway), its length, and its surface type (tarred).

**The Layer Concept (Thematic Layers)**
A GIS stores different types of information in separate layers (themes). For example, there might be one layer for roads, one for rivers, one for vegetation, and one for buildings. These layers can be stacked on top of one another on the computer screen. This allows users to analyze how different features relate to each other (for instance, checking if buildings are located too close to rivers).

[IMAGE: A 3D diagram showing the concept of GIS layers. At the bottom, a flat, real-world satellite image of a landscape. Above it, several transparent square layers hover, stacked one on top of the other, pulled apart vertically so each is visible. The bottom layer shows blue polygons representing lakes and rivers (Water). The next layer up shows green polygons for forests (Vegetation). The next shows red and grey blocks for houses and buildings (Structures). The top layer shows grey lines for roads (Transportation). A vertical dashed line passes through all layers to show how they align perfectly over the same geographic location. Clean flat textbook style, white background.]

**Data Models (How the computer draws features)**
GIS software represents the real world using two main data models:
- **Vector data model:** This uses precise geometry to represent features. It uses **points** (e.g., a single borehole or tree), **lines** (e.g., a road or river), and **polygons/areas** (e.g., a lake or a state boundary). It is excellent for showing distinct boundaries.
- **Raster data model:** This represents the world using a grid of square cells, called **pixels** (similar to a digital photograph). Each cell contains a value representing information, such as temperature, elevation, or land cover. It is best for continuous data that has no sharp boundaries, like a satellite image or rainfall map.

[IMAGE: A split diagram comparing raster and vector data models. On the left (Raster), a house, a river, and a tree are represented by a grid of small coloured squares (pixels). The curves are jagged because they are made of blocks. On the right (Vector), the same house is drawn with sharp geometric lines and points (polygons), the river is a smooth curving line, and the tree is a precise point. Labels to add later: "Raster Data Model (Grid of pixels)", "Vector Data Model (Points, lines, polygons)". Clean flat textbook style, white background.]

### 2. The Five Components of GIS

For a GIS to function properly, it requires five essential components working together:

1. **Hardware:** The physical computer equipment used to process, store, and display data. This includes computer processors, monitors, scanners, digitizers, plotters (large printers), and GPS devices.
2. **Software:** The computer programs that provide the tools to store, analyze, and display geographic information. Popular GIS software includes ArcGIS, QGIS (which is free), and MapInfo.
3. **Data:** This is the most important and expensive component. It includes the spatial coordinates and the attribute tables (the information).
4. **People:** A GIS is useless without humans. This ranges from the technical experts (GIS analysts and programmers) who manage the system, to the decision-makers and everyday citizens who use the maps.
5. **Methods (Procedures):** The rules, guidelines, and specific business practices used to manage the system. A well-designed plan is needed to ensure the data is collected accurately and updated regularly.

## Expressing locations in GIS

**Objective iii: express locations through the use of latitudes, longitudes, zipcodes etc.**

In GIS, **location referencing** (or georeferencing) is the method used to tell the computer exactly where something is located on the Earth. There are several ways to express location:

### 1. Latitudes and Longitudes (Coordinates)
This is the most precise and universal way to express a location in GIS. It uses the global grid system of imaginary lines. 
- **Latitude** measures how far North or South a place is from the Equator.
- **Longitude** measures how far East or West a place is from the Greenwich Meridian.
- In GIS, coordinates are usually stored as mathematical X (longitude) and Y (latitude) values. For example, the precise location of Abuja can be expressed in GIS as approximately **9.07° N, 7.40° E**. Because it relies on mathematics, it allows the computer to measure distances and areas perfectly.

### 2. Zipcodes (Postal Codes)
A zipcode is a series of numbers or letters used by postal services to identify specific geographic areas for mail delivery. 
- In Nigeria, the Nigerian Postal Service (NIPOST) uses a 6-digit **postal code** (for example, the code for Garki in Abuja is 900241, while the syllabus uses the American term "zipcode"). 
- In GIS, a zipcode represents an **area (polygon)** rather than a specific point. It is highly useful for mapping demographic attribute data, such as showing the average income, population density, or the number of malaria cases within a specific postal code area.

### 3. Street Addresses and Geocoding
Humans use street addresses (e.g., "10 Broad Street, Lagos") to find places every day. However, a computer cannot put an address on a map until it has coordinates. 
- **Geocoding** is the step-by-step process GIS uses to translate a descriptive location (like a street address or a zipcode) into exact latitude and longitude coordinates. 
- Once geocoded, the address appears as a precise point on the digital map.

## Sources of GIS data

**Objective iv: understand land surveying, remote sensing, map digitizing, map scanning as sources of data.**

Geographic data does not appear in a computer magically; it must be collected. The four main sources of GIS data are:

### 1. Land Surveying
This is the traditional method of capturing spatial data. Surveyors go into the field using instruments like theodolites, total stations, and Global Positioning System (GPS) receivers to physically measure exact distances, angles, and elevations on the ground.
- **Advantage:** It provides the highest level of accuracy for boundaries, property lines, and engineering projects.
- **Disadvantage:** It is very slow, labour-intensive, and expensive over large areas.

### 2. Remote Sensing
Remote sensing is the science of obtaining information about the Earth's surface from a distance, without making physical contact. This is done using sensors attached to aircraft (aerial photography) or satellites in space.
- In Nigeria, the National Space Research and Development Agency (NASRDA) manages satellites like **NigeriaSat-1** and **NigeriaSat-2**, which capture images of the country from space. 
- These satellite images provide excellent **raster data** for GIS, allowing scientists to track large-scale environmental changes, such as the shrinking of Lake Chad or the spread of urbanization in Lagos.

### 3. Map Scanning
Map scanning is the process of passing a physical paper map through an optical electronic scanner (similar to a photocopier). 
- **The process:** The scanner takes a "picture" of the map and converts it into a digital image file on the computer. 
- **The result:** The output is **raster data** (a grid of pixels). The computer only sees it as a flat picture; it does not recognize individual roads or rivers as separate features until further processing is done. It is a very fast way to get an old map into a computer.

### 4. Map Digitizing
Map digitizing is the process of converting features from a physical paper map into digital **vector data** (points, lines, and polygons).
- **The process:** The paper map is taped to a specialized electronic board called a **digitizing tablet**. A human operator uses a mouse-like device with a crosshair, called a **puck**, to carefully trace the outline of rivers, roads, and boundaries by clicking along their paths.
- **The result:** The computer records these clicks as exact coordinates, creating editable vector lines and polygons. It is slower than scanning but makes the data ready for immediate GIS analysis.

**Comparison of Scanning and Digitizing**

| Feature | Map Scanning | Map Digitizing |
| --- | --- | --- |
| **Output Data Model** | Raster data (a grid of pixels / flat image) | Vector data (editable points, lines, polygons) |
| **Equipment Used** | Optical scanner | Digitizing tablet and puck |
| **Speed** | Very fast | Slow and labour-intensive |
| **Computer Understanding** | The computer sees a single picture; it cannot distinguish a road from a river | The computer recognizes distinct features; a road can be selected and edited |

[IMAGE: Two-panel illustration of GIS data capture. Left panel (Map Scanning): a physical paper map of a coastline is sliding through a wide, flat electronic scanner, coming out on a computer screen as a single flat image file. Right panel (Map Digitizing): a person's hand holds a mouse-like device with a crosshair (a puck) and traces the outline of a river on a paper map attached to a large flat electronic board (digitizing tablet). On the connected computer screen, a sharp red vector line appears exactly matching the traced river. Labels to add later: "Map Scanning", "Raster image output", "Map Digitizing", "Digitizing tablet and puck", "Vector line output". Clean flat textbook style, white background.]

## Applications and areas of use of GIS

**Objective v: explain areas of use: Defense, Agriculture, Rural Development etc.**

GIS is used across almost every sector of the economy. Below are the key areas of application:

### 1. Defense and Military
The military relies heavily on GIS for intelligence and logistics.
- **Terrain analysis:** Mapping the physical landscape to plan safe routes for moving troops and equipment.
- **Intelligence gathering:** Using satellite imagery to locate enemy bases, hideouts, or terrorist camps.
- **Targeting:** Guiding precision missiles and drones to specific coordinates (latitudes and longitudes) with high accuracy.

### 2. Agriculture
GIS has revolutionized farming, creating a system known as **precision agriculture**.
- **Soil mapping:** Mapping different soil types on a farm so that fertilizers are only applied exactly where they are needed, saving money and the environment.
- **Crop health monitoring:** Using remote sensing images from drones or satellites to detect diseased or water-stressed crops before the human eye can see the damage.
- **Yield prediction:** Analyzing weather data and soil moisture to predict how much harvest a region will produce.

### 3. Rural Development
Governments and NGOs use GIS to plan infrastructure in underdeveloped areas to ensure resources are shared evenly.
- **Locating facilities:** Determining the best central location for a new primary healthcare centre or school so that no village is more than a 5 km walk away.
- **Resource management:** Mapping the location of underground water to determine the best places to drill community boreholes.
- **Infrastructure routing:** Planning the most cost-effective routes for rural electrification lines and feeder roads to connect remote villages to markets.

### 4. Other Important Areas of Use
- **Disaster Management:** Agencies like the National Emergency Management Agency (NEMA) use GIS to map flood-prone areas (such as communities along the River Niger and Benue) to plan evacuation routes and distribute relief materials.
- **Urban Planning:** City planners map out zones for residential, commercial, and industrial use, and track illegal structures.
- **Transportation:** Routing delivery trucks, tracking public transit systems, and providing navigation (like Google Maps).
- **Health:** Mapping disease outbreaks (like cholera or malaria) to find the source of the infection and direct medical teams to the worst-hit areas.

## Problems with GIS in Nigeria

**Objective vi: identify problems with GIS in Nigeria.**

Despite its immense benefits, the implementation and use of GIS in Nigeria face several major challenges:

1. **Inadequate Power Supply:** GIS relies entirely on computers, servers, and data centers. The erratic and poor electricity supply from the national grid means organizations must spend heavily on generators and diesel, increasing the cost of operations.
2. **High Cost of Implementation:** Setting up a GIS is very expensive. The hardware (workstations, plotters, servers), the software licenses (which are usually priced in foreign currency), and high-resolution satellite imagery cost millions of Naira.
3. **Dearth of Skilled Personnel:** There is a shortage of well-trained GIS analysts, cartographers, and spatial data scientists in Nigeria. Many universities lack the modern equipment needed to train students practically.
4. **Poor Internet and Communication Infrastructure:** GIS often requires downloading and sharing massive data files (like heavy satellite images). Slow and unreliable internet networks in many parts of the country make this very difficult.
5. **Lack of Data Availability and Sharing:** Government ministries and agencies in Nigeria often operate in silos. They are reluctant to share geographic data with each other or the public. Consequently, different agencies waste money capturing the same data twice.
6. **Obsolete Base Maps:** Many of the official topographical base maps of Nigeria were created in the 1960s and have not been updated. Using outdated maps leads to inaccurate GIS analysis.
7. **Poor Maintenance Culture:** When expensive GIS hardware (like scanners or digitizers) breaks down, there is often a lack of maintenance contracts or local experts to repair them, leaving the equipment abandoned.

## Key terms

| Term | Meaning |
| --- | --- |
| Geographic Information System (GIS) | A computer system used for capturing, storing, analyzing, and displaying spatial data. |
| Spatial data | Data that provides the exact geographic location and shape of a feature (the "Where"). |
| Attribute data | Descriptive information or statistics about a geographic feature (the "What"). |
| Vector data model | A method of representing features using precise points, lines, and polygons. |
| Raster data model | A method of representing features using a grid of square cells or pixels (like an image). |
| Remote sensing | Obtaining information about the Earth from a distance using satellites or aircraft. |
| Map digitizing | Tracing features from a paper map using a tablet and puck to create digital vector data. |
| Map scanning | Passing a paper map through an optical scanner to create a digital raster image. |
| Geocoding | The computer process of converting a descriptive location (like a street address) into exact geographic coordinates. |
| Zipcode / Postal code | A sequence of letters or numbers representing a specific geographic area for mail delivery. |

## Exam tips and common mistakes

- **Do not confuse raster and vector:** Remember that **raster** is a grid of pixels (like a digital photo), while **vector** uses geometric points, lines, and polygons.
- **Digitizing vs Scanning:** Scanning a map just takes a picture of it (raster). Digitizing means manually tracing the lines to create editable features (vector). This is a very common exam trap.
- **Spatial vs Attribute:** If a question mentions coordinates or location, it is spatial data. If it mentions names, population, or road types, it is attribute data.
- **The components of GIS:** Students often remember hardware, software, and data, but forget that **People** and **Methods** are also official components of a GIS.
- **Geocoding:** Remember that geocoding is the specific process that changes a street address into a latitude and longitude on the map.

## Quick summary

1. GIS is a computer-based system that captures, stores, analyzes, and displays geographic (spatial) data and its related descriptive (attribute) data.
2. GIS organizes information into stackable thematic layers (e.g., a road layer on top of a vegetation layer).
3. The five components of GIS are hardware, software, data, people, and methods.
4. Locations in GIS can be expressed precisely using latitudes and longitudes, or by areas using zipcodes/postal codes, and by street addresses (using a process called geocoding).
5. GIS data is sourced from land surveying, remote sensing (satellites like NigeriaSat-1), map scanning (creating raster images), and map digitizing (creating vector data).
6. GIS is used heavily in defense (terrain analysis, targeting), agriculture (precision farming, soil mapping), and rural development (locating facilities, routing roads).
7. Major problems hindering GIS in Nigeria include inadequate power supply, high costs, a lack of skilled personnel, and outdated base maps.

## Practice questions

**1. Which of the following best defines a Geographic Information System (GIS)?**
- A. A manual cartography tool for drawing topographic maps
- B. A computer-based system for capturing, storing, analyzing, and displaying spatial data
- C. A satellite placed in orbit to monitor weather patterns
- D. A traditional method of measuring land boundaries using a theodolite

**Answer: B.** GIS is entirely computer-based and is defined by its ability to manage, analyze, and display both spatial and attribute data.

**2. The component of GIS that includes the physical equipment such as computers, scanners, and plotters is known as**
- A. Software
- B. Methods
- C. Hardware
- D. People

**Answer: C.** Hardware refers to all the physical, tangible electronic equipment used in the system.

**3. In GIS, information that describes the characteristics of a feature, such as the name of a school or the population of a town, is called**
- A. Spatial data
- B. Raster data
- C. Coordinate data
- D. Attribute data

**Answer: D.** Attribute data provides the descriptive details (the "what"), while spatial data provides the physical location (the "where").

**4. The process of passing a physical paper map through an optical electronic device to create a grid of digital pixels is known as**
- A. Map digitizing
- B. Geocoding
- C. Map scanning
- D. Remote sensing

**Answer: C.** Map scanning creates a raster image (pixels). The most tempting wrong option is A, but digitizing involves manually tracing features to create vector data, not simply passing it through an optical device.

**5. Which of the following represents geographic features using a grid of square cells, where each cell contains a value?**
- A. Vector data model
- B. Raster data model
- C. Attribute table
- D. Polygon data

**Answer: B.** The raster model uses a grid of cells/pixels (like a satellite image). The vector model uses points, lines, and polygons.

**6. Using GIS to assign exact mathematical coordinates to a descriptive location like "10 Broad Street, Lagos" is known as**
- A. Map scanning
- B. Layering
- C. Remote sensing
- D. Geocoding

**Answer: D.** Geocoding is the specific GIS process of translating a street address or zipcode into exact latitudes and longitudes. 

**7. Obtaining spatial data about a large, inaccessible forest reserve using cameras attached to an aircraft or satellite is an example of**
- A. Remote sensing
- B. Land surveying
- C. Map digitizing
- D. Precision agriculture

**Answer: A.** Remote sensing gathers data from a distance without physical contact. Land surveying requires physical presence on the ground.

**8. Which of the following is a major problem hindering the effective use of GIS in Nigeria?**
- A. Free and open access to all government maps
- B. Uninterrupted power supply across the nation
- C. High cost of computer hardware and software licenses
- D. An overabundance of trained spatial data scientists

**Answer: C.** Setting up a GIS is highly capital-intensive. Options A, B, and D are incorrect because they state the exact opposite of the realities in Nigeria, where data is hoarded, power is erratic, and experts are scarce.

**9. In agriculture, GIS is most likely to be used for which of the following activities?**
- A. Guiding military drones to enemy targets
- B. Monitoring crop health and mapping soil types
- C. Planning the layout of a new urban shopping mall
- D. Tracking the movement of public transit buses

**Answer: B.** Mapping soil types and monitoring crop health are core applications of GIS in precision agriculture. The other options describe uses in defense, urban planning, and transportation.

**10. Which method of location referencing provides the most precise, mathematical point on the Earth's surface for GIS analysis?**
- A. Zipcodes
- B. State names
- C. Street addresses
- D. Latitudes and longitudes

**Answer: D.** Latitudes and longitudes provide precise X and Y coordinates. A zipcode or state name represents a large area rather than an exact point.
<!-- COVERAGE
obj i | What is a Geographic Information System (GIS) and its uses?
obj ii | Basic concepts and components of GIS
obj iii | Expressing locations in GIS
obj iv | Sources of GIS data
obj v | Applications and areas of use of GIS
obj vi | Problems with GIS in Nigeria
-->
