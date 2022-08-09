from core.ClassTime import class_times
import cv2

img1 = cv2.imread("resources/sample1.jpg", cv2.IMREAD_COLOR)
img2 = cv2.imread("resources/sample1.jpg", cv2.IMREAD_COLOR)

times = class_times(img1)
times.print()
