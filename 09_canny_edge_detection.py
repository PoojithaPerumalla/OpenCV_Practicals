import cv2

# Read the image
image = cv2.imread("images/input.png")

if image is None:
    print("Error: Could not load the image.")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray, 100, 200)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Canny Edges", edges)

# Save edge image
cv2.imwrite("outputs/canny_edges.png", edges)

print("Canny edge detection completed successfully.")

# Wait for key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()