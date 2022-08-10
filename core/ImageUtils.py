import cv2
import numpy as np

HEIGHT = 1410
WIDTH = 1077


def image_read(path):
    return cv2.imread(path, cv2.IMREAD_COLOR)


def print_image(dst):
    cv2.imshow("img", dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def draw_point(img, position, size):
    cv2.line(img, position, position, (0, 0, 255), size)


def binary_image_from_string(img):
    nparr = np.fromstring(img, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return image_as_binary(img)


def image_from_string(str):
    nparr = np.fromstring(str, np.uint8)
    return cv2.imdecode(nparr, cv2.IMREAD_COLOR)


def image_as_binary(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(img, 240, 1000, cv2.THRESH_BINARY)

    line_min_width = 40
    kernel_h = np.ones((1, line_min_width), np.uint8)
    kernel_v = np.ones((line_min_width, 1), np.uint8)

    img_bin_h = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel_h)
    img_bin_v = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel_v)
    return img_bin_h | img_bin_v
