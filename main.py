import cv2
import numpy as np

src = cv2.imread("resources/sample1.jpg", cv2.IMREAD_COLOR)
img3 = cv2.imread("resources/sample3.jpg", cv2.IMREAD_COLOR)
dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
_, img = cv2.threshold(dst, 240, 1000, cv2.THRESH_BINARY)

contours, hier = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
dst = cv2.drawContours(img, contours, -1, (0, 255, 0), 4)

cv2.imshow("img", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

line_min_width = 15
kernal_h = np.ones((1, line_min_width), np.uint8)
kernal_v = np.ones((line_min_width, 1), np.uint8)

img_bin_h = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernal_h)
img_bin_v = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernal_v)
img_bin = img_bin_h | img_bin_v

cv2.imshow("img", img_bin)
cv2.waitKey(0)
cv2.destroyAllWindows()
