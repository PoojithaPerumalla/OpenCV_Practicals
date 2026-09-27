import cv2

# Open the default webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Webcam started.")
print("Press Q to quit.")

while True:
    # Capture frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    # Display webcam frame
    cv2.imshow("Live Webcam", frame)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release webcam
cap.release()

# Close all OpenCV windows
cv2.destroyAllWindows()

print("Webcam capture completed successfully.")