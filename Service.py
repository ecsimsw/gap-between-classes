import cv2
import numpy as np

from core.ImageUtils import image_read, print_image, draw_point


def find():
    img = image_read("sample/sample1.jpg")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(img, 240, 1000, cv2.THRESH_BINARY)

    line_min_width = 40
    kernel_h = np.ones((1, line_min_width), np.uint8)
    kernel_v = np.ones((line_min_width, 1), np.uint8)

    img_bin_h = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel_h)
    img_bin_v = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel_v)
    img_bin = img_bin_h | img_bin_v

    class_line_heights(img_bin)


def class_line_heights(img_bin):
    SEARCHING_START_HEIGHT = 10
    SEARCHING_END_HEIGHT = len(img_bin) - 10
    SEARCHING_WIDTH = 15
    MINIMUM_GAP_OF_CLASS_HEIGHT = 50

    line_heights = []
    for h in range(SEARCHING_START_HEIGHT, SEARCHING_END_HEIGHT):
        if img_bin.item(h, SEARCHING_WIDTH) == 0:
            if len(line_heights) > 0 and h - line_heights[len(line_heights) - 1] < MINIMUM_GAP_OF_CLASS_HEIGHT:
                continue
            line_heights.append(h)
    for h in line_heights:
        draw_point(img_bin, tuple([SEARCHING_WIDTH, h]), 10)
    return line_heights


find()
