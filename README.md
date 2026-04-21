# AI Fitness Form Analyzer

This is a real-time AI fitness tracking project that uses computer vision to detect and analyze human exercise movements using a webcam.

## Features
- Real-time pose detection using webcam
- Supports squats, pushups, and lunges
- Automatic rep counting
- Workout tracking saved to CSV file
- Simple dashboard to view progress

## Tech Stack
- Python
- OpenCV
- MediaPipe
- NumPy
- Pandas
- Matplotlib

## Project Structure
Fitness_Analyzer/
│
├── main.py
├── utils.py
├── tracker.py
├── dashboard.py
│
├── data/
│ └── workouts.csv

## How to Run

### Install dependencies

pip install opencv-python mediapipe numpy pandas matplotlib


### Run main program

python main.py


### Run dashboard

python dashboard.py


## Controls
- S → Start tracking
- P → Pause tracking
- Q → Quit
- 1 → Squats
- 2 → Pushups
- 3 → Lunges

## Goal
To build a simple AI system that can track fitness exercises and count repetitions using computer vision.
