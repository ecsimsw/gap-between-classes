import cv2

src = cv2.imread("resources/sample1.jpg", cv2.IMREAD_COLOR)
img3 = cv2.imread("resources/sample3.jpg", cv2.IMREAD_COLOR)
dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
_, img = cv2.threshold(dst, 240, 1000, cv2.THRESH_BINARY)

contours, hier = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
dst = cv2.drawContours(img, contours, -1, (0, 255, 0), 4)

cv2.imshow("img", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
