import cv2

# Open the input video
cap = cv2.VideoCapture("videos/input.mp4")

if not cap.isOpened():
    print("Error: Could not open the video.")
    exit()

# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Create video writer
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

out = cv2.VideoWriter(
    "outputs/output_video.mp4",
    fourcc,
    fps,
    (width, height)
)

print("Playing video... Press Q to stop.")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Display frame
    cv2.imshow("Input Video", frame)

    # Write frame to output video
    out.write(frame)

    # Press Q to stop
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print("Video reading and writing completed successfully.")