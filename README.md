# AngelHack
Automatic Behavior and Anomaly Detection
# Automatic Anolamous Behavior Detection



This project aims to automatically detect criminal and abnormal activities in different areas and notify the concerned authorities for the immediate actions to be taken with minimal communication delay.
It recognizes the behaviour captured in surveillance videos for the applications of standard behaviour recognition and anomaly detection.


### Problem Statement

To prevent abnormal activity in
real time to solve the problem of delayed manual check of
surveillance footage of the unwanted events that have already
happened.


### Tech Stack

  - Python
  - Machine Learning
- Deep Neural Network 
        1. SSD_MobileNet Object Detection Model
        2. LSTM for classification
- Html
- CSS
- Javascript
- PHP


### Approach

Live footage from the CCTV is first pre-processed to extract
foreground, and removed features are fed into an LSTM Network
which is used to classify the behaviour as usual or not.
First we process the live input video frame by frame and we extract all the bottle neck features.
The we use those bottle neck feature as an input for our next deep neural network model.
