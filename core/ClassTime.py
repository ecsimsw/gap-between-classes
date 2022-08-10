from core.ImageUtils import draw_point

DAYS = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
CLASS_TIMES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

START_POSITION = (165, 100)
PIXEL_GAP_OF_DAYS = 204
PIXEL_GAP_OF_CLASS_TIME = 67


def common_class_table(class_tables):
    common_table = ClassTable()
    for time in CLASS_TIMES:
        for day in DAYS:
            for table in class_tables:
                if table.isFilled(day, time):
                    common_table.setFilled(day, time)
                    break
    return common_table


def class_time(img_bin):
    class_table = ClassTable()
    pixel_y = START_POSITION[1]
    for time in CLASS_TIMES:
        pixel_x = START_POSITION[0]
        for day in DAYS:
            if img_bin.item(pixel_y, pixel_x) == 0:
                class_table.setFilled(day, time)
            pixel_x += PIXEL_GAP_OF_DAYS
        pixel_y += PIXEL_GAP_OF_CLASS_TIME
    return class_table


def draw_dot_on_class_time(img_bin):
    pixel_y = START_POSITION[1]
    for _ in CLASS_TIMES:
        pixel_x = START_POSITION[0]
        for _ in DAYS:
            # if img_bin.item(pixel_y, pixel_x) == 0:
            draw_point(img_bin, tuple([pixel_x, pixel_y]), 5)
            pixel_x += PIXEL_GAP_OF_DAYS
        pixel_y += PIXEL_GAP_OF_CLASS_TIME
    return img_bin


class ClassTable:

    def __init__(self):
        self.table = [[0 for _ in range(len(DAYS))] for _ in range(len(CLASS_TIMES))]

    def setFilled(self, day, time):
        self.table[CLASS_TIMES.index(time)][DAYS.index(day)] = 1

    def setFilledByIndex(self, day, time):
        self.table[time][day] = 1

    def setEmpty(self, day, time):
        self.table[CLASS_TIMES.index(time)][DAYS.index(day)] = 0

    def print(self):
        for i in self.table:
            for j in i:
                print(j, end=' ')
            print()

    def isFilled(self, day, time):
        return self.table[CLASS_TIMES.index(time)][DAYS.index(day)] == 1

    def isEmpty(self, day, time):
        return self.table[CLASS_TIMES.index(time)][DAYS.index(day)] == 0
