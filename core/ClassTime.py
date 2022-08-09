from core.ImageUtils import image_as_binary

DAYS = ['MON', 'TUE', 'WED', 'THU', 'FRI']
CLASS_TIMES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

START_POSITION = (165, 100)
PIXEL_GAP_OF_DAYS = 204
PIXEL_GAP_OF_CLASS_TIME = 67


def class_times(class_image):
    img_bin = image_as_binary(class_image)
    class_table = ClassTable()

    pixel_y = START_POSITION[1]
    for time in CLASS_TIMES:
        pixel_x = START_POSITION[0]
        for day in DAYS:
            if img_bin.item(pixel_y, pixel_x) == 0:
                class_table.fill(day, time)
            pixel_x += PIXEL_GAP_OF_DAYS
        pixel_y += PIXEL_GAP_OF_CLASS_TIME
    return class_table


class ClassTable:

    def __init__(self):
        self.table = [[0 for _ in range(len(DAYS))] for _ in range(len(CLASS_TIMES))]

    def fill(self, day, time):
        day_index = DAYS.index(day)
        time_index = CLASS_TIMES.index(time)
        self.table[time_index][day_index] = 1

    def print(self):
        for i in self.table:
            for j in i:
                print(j, end=' ')
            print()