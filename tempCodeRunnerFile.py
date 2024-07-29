import tempfile
import os

# Vehicle counting code
vehicle_counting_code = """
import cv2
import numpy as np
from time import sleep

# Configuration
largura_min = 80  # Minimum width of the rectangle
altura_min = 80   # Minimum height of the rectangle
offset = 6  # Permissible error in pixels
pos_linha = 550  # Position of the counting line
delay = 60  # FPS of the video

# Initialize variables
detec = []
carros = 0

def pega_centro(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy

# Load video
cap = cv2.VideoCapture('video.mp4')
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Background subtractor
subtracao = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame1 = cap.read()
    if not ret:
        break
    tempo = float(1 / delay)
    sleep(tempo)
    
    # Preprocess the frame
    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey, (3, 3), 5)
    img_sub = subtracao.apply(blur)
    dilat = cv2.dilate(img_sub, np.ones((5, 5), np.uint8))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilatada = cv2.morphologyEx(dilat, cv2.MORPH_CLOSE, kernel)
    dilatada = cv2.morphologyEx(dilatada, cv2.MORPH_CLOSE, kernel)
    
    # Find contours
    contorno, _ = cv2.findContours(dilatada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the counting line
    cv2.line(frame1, (25, pos_linha), (1200, pos_linha), (255, 127, 0), 3)
    
    for (i, c) in enumerate(contorno):
        (x, y, w, h) = cv2.boundingRect(c)
        validar_contorno = (w >= largura_min) and (h >= altura_min)
        if not validar_contorno:
            continue

        # Draw rectangle around detected object
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        centro = pega_centro(x, y, w, h)
        detec.append(centro)
        cv2.circle(frame1, centro, 4, (0, 0, 255), -1)

        # Count vehicles
        for (x, y) in detec:
            if y < (pos_linha + offset) and y > (pos_linha - offset):
                carros += 1
                cv2.line(frame1, (25, pos_linha), (1200, pos_linha), (0, 127, 255), 3)
                detec.remove((x, y))
                print("car is detected: " + str(carros))

    # Display vehicle count
    cv2.putText(frame1, "VEHICLE COUNT: " + str(carros), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)
    
    # Show the video frames
    cv2.imshow("Video Original", frame1)
    cv2.imshow("Detectar", dilatada)

    # Break the loop if the window is closed
    if cv2.getWindowProperty("Video Original", cv2.WND_PROP_VISIBLE) < 1:
        break

    # Exit on ESC key
    if cv2.waitKey(1) == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
"""

# Create a temporary file and write the code to it
with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as temp_file:
    temp_file.write(vehicle_counting_code.encode())
    temp_filename = temp_file.name

print(f"Temporary file created: {temp_filename}")

# Optionally, you can execute the temporary file here
# Uncomment the following lines to execute the script
# import subprocess
# subprocess.run(["python", temp_filename])

# Clean up
# os.remove(temp_filename)
