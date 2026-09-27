import cv2
import numpy as np

# Read the image
image = cv2.imread("images/input.png")

if image is None:
    print("Error: Could not load the image.")
    exit()

# Create a copy for drawing
output = image.copy()

# Draw a line
cv2.line(output, (50, 50), (350, 50), (0, 255, 0), 3)

# Define polygon points
points = np.array([
    [100, 100],
    [300, 100],
    [350, 250],
    [200, 300],
    [50, 250]
], np.int32)

# Reshape points
points = points.reshape((-1, 1, 2))

# Draw polygon
cv2.polylines(output, [points], True, (255, 0, 0), 3)

# Add text
cv2.putText(
    output,
    "OpenCV Practical",
    (50, 350),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 0, 255),
    2
)

# Display the result
cv2.imshow("Shapes and Text", output)

# Save the output
cv2.imwrite("outputs/shapes_text.png", output)

print("Line, polygon and text added successfully.")

# Wait for key press
cv2.waitKey(0)

# Close window
cv2.destroyAllWindows()