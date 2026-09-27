import cv2

# Read the image
image = cv2.imread("images/input.png")

if image is None:
    print("Error: Could not load the image.")
    exit()

# Get image dimensions
height, width = image.shape[:2]

# Find the center of the image
center = (width // 2, height // 2)

# Define rotation angle and scale
angle = 45
scale = 1.0

# Create rotation matrix
rotation_matrix = cv2.getRotationMatrix2D(
    center,
    angle,
    scale
)

# Apply rotation using warpAffine
rotated = cv2.warpAffine(
    image,
    rotation_matrix,
    (width, height)
)

# Display original and rotated images
cv2.imshow("Original Image", image)
cv2.imshow("Rotated Image", rotated)

# Save rotated image
cv2.imwrite("outputs/rotated.png", rotated)

print("Image rotation completed successfully.")

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()