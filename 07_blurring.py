import cv2

# Read the image
image = cv2.imread("images/input.png")

if image is None:
    print("Error: Could not load the image.")
    exit()

# Apply Gaussian Blur
gaussian_blur = cv2.GaussianBlur(image, (15, 15), 0)

# Apply Median Blur
median_blur = cv2.medianBlur(image, 15)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Gaussian Blur", gaussian_blur)
cv2.imshow("Median Blur", median_blur)

# Save outputs
cv2.imwrite("outputs/gaussian_blur.png", gaussian_blur)
cv2.imwrite("outputs/median_blur.png", median_blur)

print("Gaussian Blur and Median Blur completed successfully.")

# Wait for key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()