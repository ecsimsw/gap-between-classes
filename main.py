import cv2

src = cv2.imread("./sample.png", cv2.IMREAD_COLOR)
# cv2.imshow("src", src)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

dst = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
_, img = cv2.threshold(dst, 240, 225, cv2.THRESH_BINARY)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()




