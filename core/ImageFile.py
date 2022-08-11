import cv2
import numpy as np


def image_read(path):
    return cv2.imread(path, cv2.IMREAD_COLOR)


def is_dark_mode(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img.item(5, 5) < 100


class BinaryImage:

    def __init__(self, img):
        if is_dark_mode(img):
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = 255 - img
            _, img = cv2.threshold(img, 230, 1000, cv2.THRESH_BINARY)
            self.img = img
            return

        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, img = cv2.threshold(img, 240, 1000, cv2.THRESH_BINARY)
        line_min_width = 35
        kernel_h = np.ones((1, line_min_width), np.uint8)
        kernel_v = np.ones((line_min_width, 1), np.uint8)

        img_bin_h = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel_h)
        img_bin_v = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel_v)
        self.img = img_bin_h | img_bin_v

    def day_line_positions(self):
        SEARCHING_START_WIDTH = 10
        SEARCHING_END_WIDTH = len(self.img[0]) - 10
        SEARCHING_HEIGHT = 5
        MINIMUM_GAP_OF_CLASS_HEIGHT = 100

        positions = []
        for w in range(SEARCHING_START_WIDTH, SEARCHING_END_WIDTH):
            if self.img.item(SEARCHING_HEIGHT, w) == 0:
                if len(positions) > 0 and w - positions[len(positions) - 1] < MINIMUM_GAP_OF_CLASS_HEIGHT:
                    continue
                positions.append(w)
        return positions

    def time_line_positions(self):
        SEARCHING_START_HEIGHT = 10
        SEARCHING_END_HEIGHT = len(self.img) - 10
        SEARCHING_WIDTH = 5
        MINIMUM_GAP_OF_CLASS_HEIGHT = 50

        positions = []
        for h in range(SEARCHING_START_HEIGHT, SEARCHING_END_HEIGHT):
            if self.img.item(h, SEARCHING_WIDTH) == 0:
                if len(positions) > 0 and h - positions[len(positions) - 1] < MINIMUM_GAP_OF_CLASS_HEIGHT:
                    continue
                positions.append(h)
        return positions

    def as_table(self):
        day_lines = self.day_line_positions()
        time_lines = self.time_line_positions()

        DISTANCE = 10
        FIRST_HALF_DISTANCE = 10
        LAST_HALF_DISTANCE = int((time_lines[1] - time_lines[0]) / 2) + 10

        table = [[0 for _ in range(len(day_lines))] for _ in range(len(time_lines) * 2)]
        for day_line in day_lines:
            for time_line in time_lines:
                day = day_lines.index(day_line)
                period = time_lines.index(time_line) * 2
                if self.img.item(time_line + FIRST_HALF_DISTANCE, day_line + DISTANCE) == 0:
                    table[period][day] = 1
                if self.img.item(time_line + LAST_HALF_DISTANCE, day_line + DISTANCE) == 0:
                    table[period + 1][day] = 1
        return table

    def draw_point(self, position, size):
        cv2.line(self.img, position, position, (0, 0, 255), size)

    def print(self):
        cv2.imshow("img", self.img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
