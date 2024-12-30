import cv2
import pytesseract
from PIL import Image
import streamlit as st

def main():
    st.title("Webcam Video Stream with OCR")

    # Access the webcam
    url = "http://192.168.219.70:8080/video"
    video_stream = cv2.VideoCapture(0)  # Use 0 for default webcam, change to 1 or other index for external cameras

    st.subheader("Live Webcam Feed")
    video_placeholder = st.empty()
    txt_html = st.empty()
    txt_write = st.empty()

    # Initialize the path to Tesseract
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    pytesseract.pytesseract.tesseract_cmd = path_to_tesseract
    image_path = "test1.jpg"

    while cv2.waitKey(400):
        # Read video frame
        ret, frame = video_stream.read()

        if not ret:
            st.warning("Unable to read from webcam. Please ensure the webcam is connected.")
            break

        # Convert BGR (OpenCV default) to RGB (Streamlit compatible)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the video frame in the Streamlit app
        video_placeholder.image(frame_rgb, channels="RGB",)

        # Convert frame to grayscale and perform OCR
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite('test1.jpg',cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
        text = pytesseract.image_to_string(Image.open(image_path))
        # text = pytesseract.image_to_string(gray)
        txt_html.html(f"<h1>{text}</h1></br>")
        # txt_write.write(text)

        # Print the extracted text in the console
        print(text)
        

        # Check for the 'q' key press to quit
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

    # Release the video stream
    video_stream.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
