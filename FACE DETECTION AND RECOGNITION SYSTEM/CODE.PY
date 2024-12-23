import cv2

# Path to the Haarcascade XML file
harcascade = "C:/Users/Admin/Downloads/haarcascade_frontalface_default.xml"

def detect_faces_image(image_path):
    """
    Detects faces in an image and saves the output.
    :param image_path: Path to the input image.
    """
    img = cv2.imread(image_path)  # Load the image
    if img is None:
        print(f"Error: Could not load image at {image_path}")
        return

    facecascade = cv2.CascadeClassifier(harcascade)  # Load the Haarcascade model
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    faces = facecascade.detectMultiScale(img_gray, 1.1, 4)  # Detect faces

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw rectangles around faces

    resized_img = cv2.resize(img, (800, 600))  # Resize for better visualization
    output_path = "detected_faces_output.png"  # Output file path
    cv2.imwrite(output_path, resized_img)  # Save the processed image
    print(f"Processed image saved as: {output_path}")


def detect_faces_video():
    """
    Detects faces in real-time from a webcam feed.
    Press 'q' to quit.
    """
    cap = cv2.VideoCapture(0)  # Initialize webcam
    cap.set(3, 640)  # Set width
    cap.set(4, 480)  # Set height

    if not cap.isOpened():
        print("Error: Could not access the webcam.")
        return

    facecascade = cv2.CascadeClassifier(harcascade)  # Load the Haarcascade model

    while True:
        success, img = cap.read()  # Capture a frame
        if not success:
            print("Error: Could not read frame from webcam.")
            break

        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
        faces = facecascade.detectMultiScale(img_gray, 1.1, 4)  # Detect faces

        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Draw rectangles around faces

        cv2.imshow("Face Detection", img)  # Display the frame with detections

        # Break the loop on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()  # Release the webcam
    cv2.destroyAllWindows()  # Close all OpenCV windows


# Example usage:
# Detect faces in an image
detect_faces_image("D:/CODSOFT-main/ALL Tasks/FACE DETECTION AND RECOGNITION SYSTEM/Screenshot 2024-03-15 224104.png")

# Detect faces in real-time from the webcam
# Uncomment the line below to enable webcam detection
# detect_faces_video()
