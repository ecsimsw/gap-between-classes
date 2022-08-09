import cv2
import numpy as np


def print_image(dst):
    cv2.imshow("img", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def draw_point(img, position, size):
    cv2.line(img, position, position, (0, 0, 255), size)


def image_as_binary(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(img, 240, 1000, cv2.THRESH_BINARY)

    line_min_width = 40
    kernel_h = np.ones((1, line_min_width), np.uint8)
    kernel_v = np.ones((line_min_width, 1), np.uint8)

    img_bin_h = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel_h)
    img_bin_v = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel_v)
    return img_bin_h | img_bin_v
