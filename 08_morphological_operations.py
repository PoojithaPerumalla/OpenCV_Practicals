import cv2
import numpy as np

# Read the image
image = cv2.imread("images/input.png")

if image is None:
    print("Error: Could not load the image.")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create a morphological kernel
kernel = np.ones((15, 15), np.uint8)

# Apply Tophat
tophat = cv2.morphologyEx(
    gray,
    cv2.MORPH_TOPHAT,
    kernel
)

# Apply Blackhat
blackhat = cv2.morphologyEx(
    gray,
    cv2.MORPH_BLACKHAT,
    kernel
)

# Display results
cv2.imshow("Original Grayscale Image", gray)
cv2.imshow("Tophat", tophat)
cv2.imshow("Blackhat", blackhat)

# Save outputs
cv2.imwrite("outputs/tophat.png", tophat)
cv2.imwrite("outputs/blackhat.png", blackhat)

print("Tophat and Blackhat operations completed successfully.")

# Wait for key press
cv2.waitKey(0)

# Close windows
cv2.destroyAllWindows()