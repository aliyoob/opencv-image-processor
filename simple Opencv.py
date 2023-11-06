import cv2

image = cv2.imread("Main.jpeg")
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Result",image)
cv2.imshow("Gray Res",grayscale)

# cv2.imwrite("Gray.jpg", grayscale)

cv2.waitKey(0)