import cv2

from core.ClassTime import class_time, common_class_table

img1 = cv2.imread("resources/sample1.jpg", cv2.IMREAD_COLOR)
img2 = cv2.imread("resources/sample1.jpg", cv2.IMREAD_COLOR)

class_times = [class_time(img1), class_time(img2)]
gap_table = common_class_table(class_times)
gap_table.print()
