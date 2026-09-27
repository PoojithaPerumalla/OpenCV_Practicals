import cv2

# Read the image
image = cv2.imread("images/input.png")

if image is None:
    print("Error: Could not load the image.")
    exit()

# Resize the image
resized = cv2.resize(image, (400, 300))

# Horizontal flip
horizontal_flip = cv2.flip(image, 1)

# Vertical flip
vertical_flip = cv2.flip(image, 0)

# Both horizontal and vertical flip
both_flip = cv2.flip(image, -1)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Resized Image", resized)
cv2.imshow("Horizontal Flip", horizontal_flip)
cv2.imshow("Vertical Flip", vertical_flip)
cv2.imshow("Both Flips", both_flip)

# Save outputs
cv2.imwrite("outputs/resized.png", resized)
cv2.imwrite("outputs/horizontal_flip.png", horizontal_flip)
cv2.imwrite("outputs/vertical_flip.png", vertical_flip)
cv2.imwrite("outputs/both_flip.png", both_flip)

print("Resize and flip operations completed successfully.")

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()