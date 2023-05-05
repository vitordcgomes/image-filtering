import cv2
import numpy as np

kernelSharp = np.array([[0, -1,  0], #generic kernel - sharp filter
                       [-1,  5, -1],
                        [0, -1,  0]])

kernelEdge = np.array([[-1, -1, -1], #generic kernel - edge detection filter
                        [-1, 8, -1],
                        [-1, -1, -1]])

penguin_img = cv2.imread("penguin.jpg") #reads the image to filter
building_img = cv2.imread("building.jpg")

img_blur = cv2.GaussianBlur(penguin_img, (7,7), 0) #GaussianBlur filter kernel built-in function

img_sharp = cv2.filter2D(src=penguin_img, ddepth=-1, kernel=kernelSharp) #generic 2D filtering function
edge_image = cv2.filter2D(src=penguin_img, ddepth=-1, kernel=kernelEdge)

#penguin filtering
cv2.imshow('Original Peng', penguin_img) #shows the filtered image
cv2.imshow('Sharp Image', img_sharp) 
cv2.imshow('Blur Image', img_blur)
cv2.imshow('Edged Image', edge_image)

#building filtering
#cv2.imshow('Original Image', building_img)
#cv2.imshow('Edged Image', edge_image)


cv2.waitKey(0)