# Keyboardless-Handwriting-Input
# ✍️ Keyboardless Handwriting Input

> An inclusive, real-time handwriting-to-text system — no keyboard required.

---

## 🧠 Problem Statement

Typing isn’t designed for everyone. People with motor disabilities or limited hand mobility often struggle with keyboards. This project introduces a natural, accessible way to communicate: through handwriting input instead of traditional typing.

---

## 💡 Solution Overview

Keyboardless Handwriting Input allows users to “write” in the air, on a touchscreen, or with a stylus — and see their handwriting instantly translated into text.

- ✍️ Converts natural handwriting gestures into typed text
- 🎯 Tracks finger or stylus movements using **computer vision**
- ⚡ Recognizes and translates handwriting into text **in real time**

---

## 🚀 Why This Matters

Unlike standard typing tools, this project is:

- **Accessible**: Designed for users with motor impairments
- **Versatile**: Works on phones, tablets, smartwatches, and even in AR/VR
- **Natural**: Mimics real handwriting for faster, more comfortable text input

---

## 🌟 Unique Features

- No physical keyboard needed
- Write on touchscreens or “in the air”
- Real-time handwriting recognition powered by machine learning
- Works across diverse scripts and input styles

---

## 🎯 Target Audience

**Who Benefits**:
- Individuals with accessibility needs
- Students and professionals in hands-busy environments
- Creatives and multilingual users who prefer pen-like input

**Use Cases**:
- Note-taking, form-filling, creative expression, and accessible communication
- Input in multiple languages or non-Latin scripts with ease

---

## 🛠️ Tech Stack

### 📥 Input and Finger Tracking
- **MediaPipe Hands**: Real-time hand landmark detection (via webcam)
- **HTML5 Video**: Webcam streaming in the browser
- **JavaScript + TensorFlow.js**: Extracts finger positions client-side

### 🧠 ML & Preprocessing
- **OpenCV (Python)**: Image preprocessing (grayscale, resize)
- **TensorFlow / PyTorch**: Character recognition using MNIST/EMNIST

### 🧪 Backend
- **Flask (Python)**: Handles API calls and model inference
- **REST API**: Connects frontend input to backend prediction logic

### 🖥️ Frontend
- **React.js** or **Vanilla JS**
- **Canvas API**: Visualizes the user's handwriting path in real time

---

## 🧪 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/anunjinb/Keyboardless-Handwriting-Input.git
cd Keyboardless-Handwriting-Input
