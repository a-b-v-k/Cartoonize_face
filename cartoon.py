import cv2

img = cv2.imread('sample1.jpg')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 13, 9)

color = cv2.bilateralFilter(img, 9, 490, 400)
cartoon = cv2.bitwise_and(color, color, mask = edges)

cartoon = cv2.resize(cartoon, (800, 600))

#cv2.imshow("Image", img)
#cv2.imshow("gray", gray)
#cv2.imshow("edges", edges)
cv2.imshow("cartoon", cartoon)

cv2.waitKey(0)

cv2.destroyAllWindows()