# 🧠 AI Fitness Form Analyzer (Real-Time Computer Vision Trainer)

A real-time AI-powered fitness system that analyzes human body posture using a webcam and provides instant feedback on exercise form.

This project uses **computer vision (MediaPipe + OpenCV)** to detect body landmarks and track exercises like squats, pushups, and lunges.

---

## 🚀 Demo Overview

- Detects human pose in real time
- Tracks exercise movements
- Counts repetitions automatically
- Provides live feedback on form
- Logs workout history for progress tracking
- Visual dashboard for performance analytics

---

## 🏋️ Supported Exercises

- Squats
- Pushups
- Lunges

---

## 🧠 Key Features

### 🎯 Real-Time Pose Detection
Uses MediaPipe to detect 33 human body landmarks from webcam input.

### 🔢 Automatic Rep Counter
Detects movement cycles and counts completed reps accurately.

### 📊 Workout Tracking System
Stores workout data in CSV format for progress analysis.

### 📈 Performance Dashboard
Visualizes workout history using graphs for progress tracking.

### 🔧 Modular Architecture
Clean separation of logic:
- `main.py` → AI runtime system
- `utils.py` → mathematical logic (angles)
- `tracker.py` → workout logging system

---

## 🛠 Tech Stack

- Python
- OpenCV
- MediaPipe
- NumPy
- Pandas
- Matplotlib

---

## 📁 Project Structure
