import cv2
import numpy as np

from core.ClassTime import ClassTable
from core.ImageUtils import draw_point


def day_line_positions(img_bin):
    SEARCHING_START_WIDTH = 10
    SEARCHING_END_WIDTH = len(img_bin[0]) - 10
    SEARCHING_HEIGHT = 5
    MINIMUM_GAP_OF_CLASS_HEIGHT = 100

    positions = []
    for w in range(SEARCHING_START_WIDTH, SEARCHING_END_WIDTH):
        if img_bin.item(SEARCHING_HEIGHT, w) == 0:
            if len(positions) > 0 and w - positions[len(positions) - 1] < MINIMUM_GAP_OF_CLASS_HEIGHT:
                continue
            positions.append(w)
    return positions


def time_line_positions(img_bin):
    SEARCHING_START_HEIGHT = 10
    SEARCHING_END_HEIGHT = len(img_bin) - 10
    SEARCHING_WIDTH = 5
    MINIMUM_GAP_OF_CLASS_HEIGHT = 50

    positions = []
    for h in range(SEARCHING_START_HEIGHT, SEARCHING_END_HEIGHT):
        if img_bin.item(h, SEARCHING_WIDTH) == 0:
            if len(positions) > 0 and h - positions[len(positions) - 1] < MINIMUM_GAP_OF_CLASS_HEIGHT:
                continue
            positions.append(h)
    return positions


def class_time_positions(img_bin):
    days = day_line_positions(img_bin)
    times = time_line_positions(img_bin)

    DISTANCE = 10
    FIRST_HALF_DISTANCE = 10
    LAST_HALF_DISTANCE = int((times[1] - times[0]) / 2) + 10
    positions = []
    for day_index, day in enumerate(days):
        for time_index, time in enumerate(times):
            positions.append([day + DISTANCE, time + FIRST_HALF_DISTANCE])
            positions.append([day + DISTANCE, time + LAST_HALF_DISTANCE])
    return positions


def as_binary_image(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(img, 240, 1000, cv2.THRESH_BINARY)

    line_min_width = 35
    kernel_h = np.ones((1, line_min_width), np.uint8)
    kernel_v = np.ones((line_min_width, 1), np.uint8)

    img_bin_h = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel_h)
    img_bin_v = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel_v)
    return img_bin_h | img_bin_v


def draw_dot_on_class_time(img):
    img_bin = as_binary_image(img)
    positions = class_time_positions(img_bin)
    for position in positions:
        draw_point(img_bin, position, 5)
    return img_bin


def class_time(img):
    img_bin = as_binary_image(img)
    class_table = ClassTable()
    day_lines = day_line_positions(img_bin)
    time_lines = time_line_positions(img_bin)

    DISTANCE = 10
    FIRST_HALF_DISTANCE = 10
    LAST_HALF_DISTANCE = int((time_lines[1] - time_lines[0]) / 2) + 10

    for day_line in day_lines:
        for time_line in time_lines:
            day = day_lines.index(day_line)
            time = time_lines.index(time_line) * 2
            if img_bin.item(time_line + FIRST_HALF_DISTANCE, day_line + DISTANCE) == 0:
                class_table.setFilledByIndex(day, time)
            if img_bin.item(time_line + LAST_HALF_DISTANCE, day_line + DISTANCE) == 0:
                class_table.setFilledByIndex(day, time + 1)
    return class_table
