import cv2
import numpy as np

# Create point matrix get coordinates of mouse click on image
point_matrix = np.zeros((2, 2), int)

counter = 0


def mousePoints(event, x, y, flags, params):
    global counter
    # Left button mouse click event opencv
    if event == cv2.EVENT_LBUTTONDOWN:
        point_matrix[counter] = x, y
        counter = counter + 1


# Read image
img = cv2.imread('C:/Users/6hs8de/Desktop/FramesV1P9/1.jpg')

while True:
    for x in range(0, 2):
        cv2.circle(img, (point_matrix[x][0], point_matrix[x][1]), 3, (0, 255, 0), cv2.FILLED)

    if counter == 2:
        S_x = point_matrix[0][0]
        S_y = point_matrix[0][1]

        E_x = point_matrix[1][0]
        E_y = point_matrix[1][1]
        # Draw rectangle for area of interest
        cv2.rectangle(img, (S_x, S_y), (E_x, E_y), (0, 255, 0), 1)

        # Cropping image
        img_cropped = img[S_y:E_y, S_x:E_x]
        cv2.imshow("ROI", img_cropped)
        np.save("C:/Users/6hs8de/Desktop/imgCrop", img_cropped)

    # Showing original image
    cv2.imshow("Original Image ", img)
    # Mouse click event on original image
    cv2.setMouseCallback("Original Image ", mousePoints)
    # Printing updated point matrix
    print(point_matrix)
    # Refreshing window all time
    cv2.waitKey(1)

