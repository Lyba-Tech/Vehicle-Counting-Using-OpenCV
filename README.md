![alt text](image.png)

### Vehicle Counting Using OpenCV

This project demonstrates a vehicle counting system using OpenCV and background subtraction techniques. The goal is to detect and count vehicles in a video stream by analyzing frame-by-frame changes. Here's a breakdown of the theory and methodology used:

#### **1. Overview**

The script processes a video to detect and count vehicles crossing a specified line. It leverages background subtraction and contour detection to identify moving objects and count them based on their position relative to a counting line.

#### **2. Key Concepts**

- **Background Subtraction**: This technique is used to isolate moving objects from the static background. The script utilizes OpenCV's `BackgroundSubtractorMOG2` to create a model of the static background and detect foreground objects.
  
- **Contour Detection**: After background subtraction, contours of the detected objects are found using OpenCV's `findContours` function. This helps in identifying and tracking the shapes of the moving vehicles.

- **Vehicle Detection and Counting**:
  - **Minimum Size Filtering**: Only objects (vehicles) with dimensions greater than a specified minimum width and height are considered. This helps in ignoring small noise or irrelevant objects.
  - **Center Calculation**: The center of each detected object is calculated to monitor its position.
  - **Counting Logic**: Vehicles are counted based on their vertical position relative to a specified line (`pos_linha`). When the center of a detected object crosses this line, it is counted as a detected vehicle.

#### **3. Code Flow**

1. **Initialization**: 
   - The video file is loaded.
   - A background subtractor is initialized to detect moving objects.

2. **Processing Each Frame**:
   - Convert the frame to grayscale and apply Gaussian blur to reduce noise.
   - Apply background subtraction to extract foreground objects.
   - Perform dilation and morphological operations to enhance object boundaries.
   - Find contours of the detected objects.

3. **Drawing and Counting**:
   - Draw a line on the frame to represent the counting line.
   - For each detected contour that meets the size criteria:
     - Draw a rectangle around the object.
     - Calculate the object's center and add it to the list of detected objects.
     - Check if the object's center crosses the counting line and update the vehicle count.

4. **Display Results**:
   - Display the frame with annotations, including vehicle count and detection visualization.
   - Provide real-time feedback by showing the processed video and detected objects.

5. **Termination**:
   - The script exits when the video ends or when the user presses the ESC key.
   - Clean up by releasing the video capture and destroying all OpenCV windows.

#### **4. Dependencies**

- **OpenCV**: For video processing, background subtraction, contour detection, and visualization.
- **NumPy**: For numerical operations and handling arrays.

#### **5. Usage**

- Place a video file named `video.mp4` in the working directory.
- Run the script to start processing the video and see the vehicle count in real-time.

This vehicle counting system provides a practical application of computer vision techniques for traffic monitoring and analysis.

