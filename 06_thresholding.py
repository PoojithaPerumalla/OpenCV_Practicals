import cv2

# Read the image
image = cv2.imread("images/input.png")

if image is None:
    print("Error: Could not load the image.")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply binary threshold
threshold_value = 127

ret, binary = cv2.threshold(
    gray,
    threshold_value,
    255,
    cv2.THRESH_BINARY
)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Binary Threshold Image", binary)

# Save output
cv2.imwrite("outputs/binary_threshold.png", binary)

print("Binary thresholding completed successfully.")

# Wait for key press
cv2.waitKey(0)

# Close windows
cv2.destroyAllWindows()