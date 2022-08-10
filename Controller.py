from typing import List

from fastapi import FastAPI, File, UploadFile

from Service import draw_dot_on_class_time, class_time_positions, as_binary_image, class_time
from core.ImageUtils import image_as_binary, image_read, print_image, binary_image_from_string
import cv2

app = FastAPI()


@app.get("/classTime")
def info():
    return {"ecsimsw": "2022.08.10"}


# @app.post("/classTime")
# async def read_item(files: List[UploadFile] = File(...)):
#     file1 = await files[0].read()
#     file1 = binary_image_from_string(file1)
#
#     file2 = await files[1].read()
#     file2 = binary_image_from_string(file2)
#
#     class_times = [class_time(file1), class_time(file2)]
#     common_table = common_class_table(class_times)
#     return {"common_table": common_table}


def sampleTest():
    file1 = image_read("sample/sample1.jpg")
    file2 = image_read("sample/sample2.jpg")
    file3 = image_read("sample/sample3.jpg")
    file4 = image_read("sample/sample4.jpeg")
    file5 = image_read("sample/sample5.jpeg")
    file6 = image_read("sample/sample6.jpeg")

    table1 = class_time(file1)
    table1.print()
    # table2 = draw_dot_on_class_time(file2)
    # table3 = draw_dot_on_class_time(file3)
    # table4 = draw_dot_on_class_time(file4)
    # table5 = draw_dot_on_class_time(file5)
    # table6 = draw_dot_on_class_time(file6)

    # file1 = as_binary_image(file1)
    # class_table = class_time_positions(file1)
    # print_image(class_table)

    # print_image(table1)
    # print_image(table2)
    # print_image(table3)
    # print_image(table4)
    # print_image(table5)
    # print_image(table6)


sampleTest()
