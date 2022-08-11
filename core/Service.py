from core.ClassTime import class_table_of, common_class_table
from core.ImageFile import BinaryImage, image_read


def calculate_common_time(images):
    class_tables = []
    for i in range(len(images)):
        table = BinaryImage(images[i]).as_table()
        class_tables.append(class_table_of(table))
    return common_class_table(class_tables)


def sample_test(img):
    table = BinaryImage(img).as_table()
    return class_table_of(table)


# img = image_read("sample/sample1.jpg")
img = image_read("sample/sample-dark2.jpeg")
img = BinaryImage(img)
class_table_of(img.as_table()).print()
