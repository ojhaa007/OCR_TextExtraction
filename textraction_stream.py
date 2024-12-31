import streamlit as st
import cv2
import pytesseract
from PIL import Image
import numpy as np

# Set Tesseract executable path (Assuming Tesseract is installed in the default location on Linux)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Streamlit app title
st.title("Live Webcam Text Extraction")

# Function to capture video from webcam
def capture_video():
    cap = cv2.VideoCapture(0)
    stframe = st.empty()
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to capture frame.")
            break
        
        # Convert frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Perform OCR
        text = pytesseract.image_to_string(gray_frame)

        # Display the frame with extracted text
        stframe.image(frame, channels="BGR", caption=f"Extracted Text: {text}")
    
    cap.release()

# Button to start video capture
if st.button("Start Camera"):
    capture_video()
