DAYS = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
CLASS_TIMES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]


def common_class_table(class_tables):
    common_table = ClassTable()
    for time in range(len(CLASS_TIMES)):
        for day in range(len(DAYS)):
            for table in class_tables:
                if table.isFilled(time, day):
                    common_table.setFilled(time, day)
                    break
    return common_table


def class_table_of(table):
    class_table = ClassTable()
    for time in range(len(CLASS_TIMES)):
        for day in range(len(DAYS)):
            if len(table) <= time:
                continue
            if len(table[0]) <= day:
                continue
            if table[time][day] == 1:
                class_table.setFilled(time, day)
    return class_table


class ClassTable:

    def __init__(self):
        self.table = [[0 for _ in range(len(DAYS))] for _ in range(len(CLASS_TIMES))]

    def setFilled(self, time, day):
        self.table[time][day] = 1

    def isFilled(self, time, day):
        if len(self.table) <= time:
            return False
        if len(self.table[0]) <= day:
            return False
        return self.table[time][day] == 1

    def print(self):
        for i in self.table:
            for j in i:
                print(j, end=' ')
            print()
