# 🍎 Bad Apple Particle Engine

### A High-Performance, Image-Driven Particle Video Renderer

> **The Ultimate Capstone Project**
> Transform a single static image into tens of thousands of animated particles that **reconstruct the iconic *****Bad Apple!!***** video in real time** — smoothly, efficiently, and beautifully.

---

## 🚀 Overview

**Bad Apple Particle Engine** is a real-time particle animation system built with **Python, Pygame, OpenCV, and Pillow**.
It converts a user-uploaded image into a dynamic particle pool and continuously morphs those particles to recreate frames from the *Bad Apple!!* video using **luminance-based matching** and **smooth interpolation**.

This project is designed as a **masterpiece-level build**, combining graphics, video processing, optimization, and animation into one cohesive system.

---

## ✨ Features

* 🎨 **Image-to-Particle Conversion**
  Converts every pixel of a user image into a colored particle with preserved spatial data.

* 🎞️ **Bad Apple Frame Extraction**
  Extracts and downsamples frames from the Bad Apple video using OpenCV for performance-friendly playback.

* 🧠 **Luminance-Based Matching**
  Particles are reassigned each frame by sorting both source and target pixels by brightness, creating visually coherent transitions.

* 🌀 **Smooth Particle Transitions**
  Particles glide between frames using interpolation, with configurable movement and hold durations.

* ⏯️ **Full Video Playback Loop**
  Cycles through all processed frames to recreate the full animation.

* ⚡ **Performance-Oriented Design**
  Optimized for real-time rendering with thousands of particles while maintaining smooth frame rates.

---

## 🛠️ Tech Stack

* **Python 3**
* **Pygame** – Rendering & animation loop
* **OpenCV (cv2)** – Video frame extraction
* **Pillow (PIL)** – Image processing
* **tqdm** – Progress visualization during frame extraction

---

## 📂 Project Structure

```
.
├── main.py              # Main Pygame loop and particle controller
├── particles.py         # Particle transition logic
├── data.py              # Image loading, pixel sorting, and frame management
├── extract_frames.py    # Bad Apple video frame extractor (OpenCV)
├── frames/              # Extracted and downsampled video frames
├── Test/
│   └── makima.jpg       # User image (particle source)
└── README.md
```

---

## ⚙️ How It Works

### 1️⃣ Image Ingestion

* A single colored image is loaded.
* Each pixel becomes a particle with:

  * Position `(x, y)`
  * RGB color
  * Luminance value

### 2️⃣ Frame Processing

* Bad Apple video frames are extracted and resized.
* Frames are converted to grayscale for luminance sorting.
* Only every **N-th frame** is used to reduce memory usage.

### 3️⃣ Particle Matching

* Both image particles and frame pixels are sorted by luminance.
* Each particle is assigned a new target position based on brightness similarity.

### 4️⃣ Animation Loop

* Particles smoothly interpolate toward their targets.
* Once all particles arrive, the frame is held briefly.
* The next frame is loaded and the cycle continues.

---

## 🧠 Optimization Strategy

* Only **every 10–20th video frame** is used
* Frames are **loaded on-demand**
* Interpolation-based motion avoids heavy physics calculations

---

## ▶️ How to Run

### 1. Install Dependencies

```bash
pip install pygame pillow opencv-python tqdm
```

### 2. Extract Video Frames

```bash
python extract_frames.py
```

Provide the path to your *Bad Apple!!* video when prompted.

### 3. Run the Engine

```bash
python main.py
```

---

## 🎯 Controls & Behavior

* Automatic playback through all frames
* Smooth transitions between frames
* Frame holding for visual clarity
* Loops seamlessly once complete

---

## 📈 What This Project Demonstrates

* Advanced particle systems
* Real-time animation pipelines
* Image & video processing
* Memory-conscious design
* Performance-first thinking
* Clean separation of logic and rendering

---

## 🏆 Why This Matters

This project is not just a demo —
it’s a **statement**.

It proves you can:

* Architect a full graphics system
* Handle real-time constraints
* Optimize large data flows
* Polish an idea into a finished experience

---

## 📜 License

Free to use, modify, and build upon.
Credit appreciated — greatness inspires greatness.

---

**Go build. Go optimize. Go render magic.** 🚀
**Bad Apple never looked this good.**
