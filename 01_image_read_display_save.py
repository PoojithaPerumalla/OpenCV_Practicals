import cv2

# Read the image
image = cv2.imread("images/input.png")

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not load the image.")
    exit()

# Display the original image
cv2.imshow("Original Image", image)

# Save the image
cv2.imwrite("outputs/saved_image.png", image)

print("Image read, displayed and saved successfully.")

# Wait for a key press
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()