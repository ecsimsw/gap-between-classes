import cv2
import numpy as np


def print_image(dst):
    cv2.imshow("img", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def draw_point(img, position, size):
    cv2.line(img, position, position, (0, 0, 255), size)


img_bin = cv2.imread("resources/sample1.jpg", cv2.IMREAD_COLOR)
dst = cv2.cvtColor(img_bin, cv2.COLOR_BGR2GRAY)
_, img_bin = cv2.threshold(dst, 240, 1000, cv2.THRESH_BINARY)

line_min_width = 40
kernal_h = np.ones((1, line_min_width), np.uint8)
kernal_v = np.ones((line_min_width, 1), np.uint8)

img_bin_h = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernal_h)
img_bin_v = cv2.morphologyEx(img_bin, cv2.MORPH_OPEN, kernal_v)
img_bin = img_bin_h | img_bin_v

start_x = 165
start_y = 100
gap_of_days = 204
gap_of_half_hour = 67
days = ['MON', 'TUE', 'WED', 'THU', 'FRI']
class_times = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
               11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

now_y = start_y
for class_time in class_times:
    now_x = start_x
    for day in days:
        draw_point(img_bin, tuple([now_x, now_y]), 5)
        now_x += gap_of_days
    now_y += gap_of_half_hour

print_image(img_bin)

# cv2.imshow("img", img_bin)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
