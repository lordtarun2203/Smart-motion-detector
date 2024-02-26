import cv2
import pandas as pd
import threading
from datetime import datetime
import simpleaudio as sa
import numpy as np

# Replace 'path/to/beep.mp3' with the correct path to your beep sound file
beep_sound_path = 'path/to/beep.mp3'

def generate_sine_wave(frequency, duration, sample_rate=44100):
    t = np.arange(int(duration * sample_rate)) / sample_rate
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    return (wave * 32767).astype(np.int16)

def play_beep():
    frequency = 1000  # Adjust frequency as needed
    duration = 0.2    # Adjust duration as needed

    wave = generate_sine_wave(frequency, duration)
    play_obj = sa.play_buffer(wave, num_channels=1, bytes_per_sample=2, sample_rate=44100)
    play_obj.wait_done()

def motion_detection():
    static_back = None
    motion_list = [None, None]
    time = []
    df = pd.DataFrame(columns=["Start", "End"])

    video = cv2.VideoCapture(0)

    while True:
        check, frame = video.read()
        motion = 0

        # Resize the frame to a smaller size (adjust as needed)
        frame = cv2.resize(frame, (640, 480))

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)

        if static_back is None:
            static_back = gray
            continue

        diff_frame = cv2.absdiff(static_back, gray)
        thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
        thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

        cnts, _ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in cnts:
            if cv2.contourArea(contour) < 10000:
                continue
            motion = 1
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        motion_list.append(motion)
        motion_list = motion_list[-2:]

        if motion_list[-1] == 1 and motion_list[-2] == 0:
            time.append(datetime.now())
            threading.Thread(target=play_beep).start()
        if motion_list[-1] == 0 and motion_list[-2] == 1:
            time.append(datetime.now())
            threading.Thread(target=play_beep).start()

        cv2.imshow("Gray Frame", gray)
        cv2.imshow("Difference Frame", diff_frame)
        cv2.imshow("Threshold Frame", thresh_frame)
        cv2.imshow("Color Frame", frame)

        key = cv2.waitKey(1)
        if key == ord('q'):
            if motion == 1:
                time.append(datetime.now())
            break

    for i in range(0, len(time), 2):
        df = df.append({"Start": time[i], "End": time[i + 1]}, ignore_index=True)

    df.to_csv("Time_of_movements.csv")

    video.release()
    cv2.destroyAllWindows()

# Run the motion detection in a separate thread
threading.Thread(target=motion_detection).start()
