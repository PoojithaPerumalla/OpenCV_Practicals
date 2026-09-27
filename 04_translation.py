import cv2
import numpy as np

# Read the image
image = cv2.imread("images/input.png")

if image is None:
    print("Error: Could not load the image.")
    exit()

# Get image dimensions
height, width = image.shape[:2]

# Define translation values
tx = 100
ty = 50

# Create translation matrix
translation_matrix = np.float32([
    [1, 0, tx],
    [0, 1, ty]
])

# Apply translation using warpAffine
translated = cv2.warpAffine(
    image,
    translation_matrix,
    (width, height)
)

# Display original and translated images
cv2.imshow("Original Image", image)
cv2.imshow("Translated Image", translated)

# Save the translated image
cv2.imwrite("outputs/translated.png", translated)

print("Image translation completed successfully.")

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()