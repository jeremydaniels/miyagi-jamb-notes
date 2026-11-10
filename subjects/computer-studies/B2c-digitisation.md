# JAMB Computer Studies Notes: Methods of Digitisation

## What JAMB expects

This topic is part of Section B, Topic 2 of the JAMB Computer Studies syllabus: Data and Information. It covers the third part of the topic. (The differences between data and information, and data representation/number bases, are covered in `B2a-data-and-information.md` and `B2b-data-representation-and-number-bases.md`).

This file covers the following content item:
* c. Methods of Digitisation

By the end of these notes, you should be able to:
1. Define digitization
2. Explain the process of digitalization(manual, heads-up, interactive tracing, automatic)
3. List different formats of digitized data (image, audio, video, motion, text, multimedia, etc.)

**Note on the syllabus wording:** The syllabus uses the spelling "digitization" in objective i, and "digitalization" in objective ii. In standard computer science and business, these two words mean different things. **Digitisation** (or digitization) is the technical process of converting physical or analog information into digital computer data (like scanning a paper). **Digitalisation** usually means using digital technology to change how a business or society works (like a bank moving from paper passbooks to mobile banking apps). However, because the syllabus lists technical conversion methods (manual, heads-up, etc.) under "digitalization", it uses both words to mean the exact same thing: the conversion process. We will explain the technical methods exactly as the syllabus requires.

## What is Digitisation?

**Objective i: Define digitization.**

**Digitisation** (spelled with an 's' or a 'z') is the process of converting analog information or physical objects into a **digital format**. 

A digital format means that the information is represented by a series of binary digits (1s and 0s) that a computer system can process, store, and transmit. 

Whenever you take a physical paper, a real-world sound, or a printed photograph and convert it into a file on your computer or phone, you are digitising it. 

Examples of digitisation include:
* Using a scanner to convert a printed WAEC certificate into a PDF document.
* Recording your voice singing a song and saving it as an MP3 file on your phone.
* Using a digital camera to take a picture of a landscape.
* Typing out a handwritten letter using a keyboard into a Microsoft Word document.

## Processes of Digitisation

**Objective ii: Explain the process of digitalization(manual, heads-up, interactive tracing, automatic).**

The specific methods listed in the syllabus—manual, heads-up, interactive tracing, and automatic—are technical terms used heavily in **Geographic Information Systems (GIS)** and **Computer-Aided Design (CAD)**. They describe how physical maps, engineering drawings, or printed pictures are converted into editable digital lines and shapes (vector graphics). 

Here is how each process works:

### 1. Manual Digitisation
In manual digitisation, a person physically traces the lines of a hardcopy (paper) map or drawing using a special piece of hardware called a **digitising tablet** (or digitizer) and a pointing device called a **puck** (which looks like a mouse with a crosshair).

**The process:**
1. The paper map is securely taped to the surface of the digitising tablet.
2. The tablet has an invisible electronic grid that tracks coordinates (X and Y positions).
3. The user holds the puck, places the crosshair exactly over a line or point on the paper map, and clicks a button.
4. Each click sends the exact coordinates to the computer, building a digital version of the map point by point and line by line.

**Characteristics:** It is slow, requires a lot of human effort, and its accuracy depends entirely on how steady the person's hand is. 

[IMAGE: A user performing manual digitisation. A large flat digitising tablet is on a desk with a paper map taped to it. The user's hand is holding a digitising puck (a mouse-like device with a clear plastic extension showing a crosshair) over a line on the map. A computer monitor nearby shows the digital lines being created. Clean flat textbook illustration, white background.]

### 2. Heads-up Digitisation (On-screen Digitisation)
"Heads-up" gets its name because the user keeps their head up, looking at the computer monitor, instead of looking down at a digitising tablet. 

**The process:**
1. The paper map or drawing is first converted into a digital picture (a raster image) using an electronic **scanner**.
2. This scanned image is opened on a computer screen using specialised software.
3. The user uses a standard computer mouse to click and trace over the lines, roads, or boundaries visible on the scanned image on the screen.

**Characteristics:** It is more comfortable than manual digitising. The user can zoom in on the screen to see small details clearly, which makes it very accurate. It is currently the most popular method for digitising maps.

### 3. Interactive Tracing (Semi-automatic Digitisation)
Interactive tracing is a combination of human effort and smart software. It is a step up from heads-up digitising because the computer does part of the tracing for you.

**The process:**
1. Just like heads-up digitising, the paper map is scanned and displayed on the screen.
2. Instead of tracing every single tiny curve manually, the user clicks at the start of a line.
3. The software's algorithm looks at the scanned image, detects the edge of the line based on colour or contrast, and automatically traces the rest of the line until it gets confused (for example, if lines cross).
4. If the software stops, the user clicks again to guide it, and the software continues.

**Characteristics:** It is much faster than manual or pure heads-up digitising but still requires a human to monitor the process and guide the software when it makes a mistake.

### 4. Automatic Digitisation
Automatic digitisation relies entirely on the computer software to convert an entire scanned image into digital data with almost no human tracing.

**The process:**
1. A physical document is scanned into the computer.
2. Special software analyses the whole image at once.
3. For maps or drawings, **raster-to-vector conversion software** automatically finds all the lines, circles, and text, turning them into digital shapes immediately.
4. For text documents, **Optical Character Recognition (OCR)** software scans the shapes of the letters and automatically converts them into editable text (so you can edit it in Microsoft Word, instead of it just being a flat picture).

**Characteristics:** It is extremely fast and great for clean, high-quality original documents. However, if the original paper is dirty, faded, or has very complex overlapping lines, the software will make mistakes, and a human will have to spend time fixing the errors.

### Summary Comparison of the Processes

| Feature | Manual | Heads-up | Interactive Tracing | Automatic |
| :--- | :--- | :--- | :--- | :--- |
| **Input Hardware** | Digitising tablet and puck | Scanner and computer mouse | Scanner and computer mouse | Scanner |
| **User's Focus** | Looking down at the paper | Looking up at the screen | Looking up at the screen | Minimal (starts the software) |
| **Speed** | Very slow | Moderate | Fast | Very fast |
| **Human Effort** | Very high (traces everything) | High (traces everything) | Medium (guides the software) | Very low (software does the work) |

## Formats of Digitized Data

**Objective iii: List different formats of digitized data (image, audio, video, motion, text, multimedia, etc.).**

When data is digitised, it must be saved in a specific **file format** so the computer knows how to open and read it. Different types of data have different standard formats. 

### 1. Image Formats
These formats store digital pictures, such as scanned photographs, digital art, or camera snapshots.
*   **JPEG / JPG (Joint Photographic Experts Group):** Very common for photographs; creates small file sizes by losing a tiny bit of quality.
*   **PNG (Portable Network Graphics):** Great for web graphics because it supports transparent backgrounds.
*   **GIF (Graphics Interchange Format):** Often used for simple graphics on the web; supports basic animation.
*   **BMP (Bitmap):** An older format that saves high-quality images but takes up a lot of storage space.

### 2. Audio Formats
These formats store sound, such as recorded voice, music, or sound effects.
*   **MP3 (MPEG-1 Audio Layer III):** The most popular format for music; compresses the audio so the file size is small but the sound is still good.
*   **WAV (Waveform Audio File Format):** Uncompressed, high-quality sound used by professionals in studios. The files are very large.
*   **AAC (Advanced Audio Coding):** Similar to MP3 but offers slightly better sound quality; often used by Apple (iTunes) and YouTube.

### 3. Video Formats
These formats store moving pictures combined with sound, such as movies or recorded phone clips.
*   **MP4 (MPEG-4 Part 14):** The most common video format today. Used for YouTube, phones, and sharing online.
*   **AVI (Audio Video Interleave):** An older format developed by Microsoft; files are usually larger than MP4.
*   **MKV (Matroska):** Often used for high-definition movies because it can hold multiple audio tracks (like different languages) and subtitles in one file.

### 4. Motion / Animation Formats
These formats specifically handle movement, often without heavy audio or video data. They are used for computer animations or motion capture.
*   **GIF:** As mentioned, animated GIFs show a short, repeating, silent loop of images.
*   **SWF (Small Web Format):** An older format used by Adobe Flash for web animations (though largely discontinued today).
*   **BVH (Biovision Hierarchy):** A specialised format used to store motion-capture data (for example, recording a real actor's movements to animate a 3D video game character).

### 5. Text Formats
These formats store typed words, numbers, and symbols.
*   **TXT (Plain Text):** Stores only basic text with no formatting (no bold, no colours, no images). 
*   **DOCX (Microsoft Word Document):** Stores text along with formatting, tables, and images.
*   **PDF (Portable Document Format):** Created by Adobe; it locks the layout so the document looks exactly the same on any computer or phone.
*   **RTF (Rich Text Format):** A universal format that supports basic text formatting (like bold and italics) and can be opened by almost any word processor.

### 6. Multimedia Formats
Multimedia means combining multiple types of media (text, image, audio, video) into a single interactive package.
*   **HTML (Hypertext Markup Language):** The format for web pages. A single web page can contain text, images, videos, and clickable links.
*   **PPTX (Microsoft PowerPoint):** A presentation file that can hold text, images, audio, video, and slide animations.

[IMAGE: A graphic showing six folders labelled Image, Audio, Video, Motion, Text, and Multimedia. Inside each folder are smaller icons showing common file extensions. Image: JPG, PNG. Audio: MP3, WAV. Video: MP4, AVI. Motion: GIF, BVH. Text: PDF, DOCX, TXT. Multimedia: HTML, PPTX. Clean flat textbook illustration, white background.]

## Key terms

| Term | Meaning |
| :--- | :--- |
| **Digitisation** | The process of converting physical or analog data into a digital (binary) format for computer processing. |
| **Digitising tablet** | A physical electronic board used with a puck to manually trace maps and drawings into a computer. |
| **Puck** | A mouse-like pointing device with a crosshair, used on a digitising tablet for high accuracy. |
| **Heads-up digitising** | Tracing over a scanned image on a computer monitor using a mouse. |
| **Interactive tracing** | A digitising method where the user clicks a starting point and the software automatically traces the line. |
| **Automatic digitisation** | Converting a scanned document to digital vectors or text entirely using software algorithms (like OCR). |
| **OCR** | Optical Character Recognition; software that automatically reads printed text in a scanned image and converts it to editable text. |
| **JPEG / PNG** | Common formats used for digitised images. |
| **MP3 / WAV** | Common formats used for digitised audio. |
| **MP4 / AVI** | Common formats used for digitised video. |

## Exam tips and common mistakes

*   **Heads-up vs Manual:** The most common exam mistake is confusing manual digitising with heads-up digitising. Remember: **Manual** uses a physical *digitising tablet* and you look down. **Heads-up** uses a *scanner and computer screen* and you look up at the monitor.
*   **Automatic digitising needs a scanner:** You cannot do automatic digitising directly from a physical paper without first scanning it to get a raster image. 
*   **File format categories:** Be prepared to classify file extensions. If a question asks for a video format, look for MP4 or AVI, not MP3 (which is audio) or JPEG (which is an image).
*   **Digitization vs Digitalization:** If JAMB asks for the meaning of "digitalization" in the context of data formats, treat it as the technical conversion of analog to digital (because that is how the syllabus groups it), even though modern textbooks might define it as a broader business transformation.

## Quick summary

1. Digitisation is the conversion of physical or analog information into a digital format consisting of binary digits (1s and 0s).
2. Manual digitisation requires tracing a physical paper document on a digitising tablet using a puck.
3. Heads-up (on-screen) digitisation involves scanning a document first and then tracing it on the computer monitor using a mouse.
4. Interactive tracing is a semi-automatic process where a user guides software to trace lines on a scanned image.
5. Automatic digitisation relies heavily on software (such as OCR or vectorisation tools) to convert scanned images with minimal human effort.
6. Digitised image formats include JPEG, PNG, GIF, and BMP.
7. Digitised audio formats include MP3, WAV, and AAC, while video formats include MP4, AVI, and MKV.
8. Text documents can be saved in formats like TXT, DOCX, RTF, and PDF.

## Practice questions

**1. The process of converting physical or analog information into a binary format that a computer can process is known as:**
- A. Formatting
- B. Digitisation
- C. Downloading
- D. Networking

**Answer: B.** Digitisation (or digitization) is defined as converting analog information into a digital format.

**2. Which method of digitisation involves tracing a paper map taped to an electronic board using a device called a puck?**
- A. Automatic digitisation
- B. Interactive tracing
- C. Heads-up digitisation
- D. Manual digitisation

**Answer: D.** Manual digitisation is done physically by tracing a hardcopy document on a digitising tablet with a puck.

**3. Why is "heads-up" digitisation given its name?**
- A. Because the user must wear a headset while working.
- B. Because the user keeps their head up to look at a computer screen instead of looking down at a tablet.
- C. Because the software automatically brings the image to the top of the screen.
- D. Because it requires a special camera mounted above the user's head.

**Answer: B.** The user traces over a scanned image displayed on a computer monitor, meaning they keep their head up to look at the screen.

**4. A method of digitisation where the user clicks the start of a line and software automatically detects and traces the rest of the edge is called:**
- A. Manual digitisation
- B. Heads-up digitisation
- C. Interactive tracing
- D. Complete automation

**Answer: C.** Interactive tracing (or semi-automatic digitisation) relies on user clicks to guide software algorithms that do the actual line tracing.

**5. Which of the following software technologies is a common example of automatic digitisation for typed documents?**
- A. Optical Character Recognition (OCR)
- B. Computer-Aided Design (CAD)
- C. Word Processing Software
- D. Antivirus Software

**Answer: A.** OCR software analyses a scanned image of text and automatically converts the letters into editable digital text without a human having to trace or re-type them.

**6. Which of the following lists contains ONLY digitised audio formats?**
- A. MP3, WAV, AAC
- B. JPEG, PNG, BMP
- C. MP4, AVI, MKV
- D. PDF, DOCX, TXT

**Answer: A.** MP3, WAV, and AAC are audio formats. Option B contains image formats, C contains video formats, and D contains text formats.

**7. A student scans a photograph and saves it to a flash drive. Which of the following file extensions is most likely applied to the file?**
- A. .mp3
- B. .jpeg
- C. .txt
- D. .avi

**Answer: B.** JPEG (.jpeg) is a standard image format for photographs. MP3 is for audio, TXT is for plain text, and AVI is for video.

**8. Which digitisation process generally requires the LEAST amount of human tracing effort?**
- A. Manual digitisation
- B. Heads-up digitisation
- C. Interactive tracing
- D. Automatic digitisation

**Answer: D.** Automatic digitisation uses software to interpret the entire scanned image, requiring minimal human tracing compared to manual, heads-up, or interactive tracing.

**9. The primary advantage of heads-up digitisation over manual digitisation is that:**
- A. It does not require a computer to process the data.
- B. It uses a digitising tablet, which is cheaper than a scanner.
- C. The user can zoom in on the scanned image on the screen to improve accuracy.
- D. The computer does 100% of the tracing automatically.

**Answer: C.** Heads-up digitising allows the user to zoom in on the screen to trace details very accurately. Option D describes automatic digitisation, not heads-up. Option B is incorrect because heads-up uses a scanner, not a tablet.

**10. An interactive web page combining text, images, sound, and video is best classified as which format type?**
- A. Plain text format
- B. Motion format
- C. Audio format
- D. Multimedia format

**Answer: D.** Multimedia refers to the integration of multiple forms of media (text, audio, images, video) into a single presentation or interface, such as an HTML web page.
