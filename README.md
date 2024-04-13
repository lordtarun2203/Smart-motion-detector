# Smart Motion Detector

## Description
This project implements a Smart Motion Detector using Python and OpenCV, capable of detecting motion in real-time using a webcam. It employs computer vision techniques to analyze consecutive frames, identify changes, and trigger alerts when motion is detected. Additionally, it records the timestamps of detected motions in a CSV file for further analysis.

## Features
- Real-time motion detection using webcam feed
- Adjustable motion sensitivity threshold
- Beep alert upon detecting motion
- Records timestamps of detected motions
- User-friendly graphical interface

## Requirements
- Python 3.x
- OpenCV library
- pandas library
- simpleaudio library
- NumPy library

## Installation
1. Clone the repository to your local machine:

2. Install the required Python libraries:
  pip install opencv-python pandas simpleaudio numpy

## Usage
1. Navigate to the project directory:
  cd smart-motion-detector
2. Run the main Python script:
  python motion_detector.py
