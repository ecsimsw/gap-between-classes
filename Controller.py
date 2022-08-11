from typing import List

from fastapi import FastAPI, UploadFile
from multipart.multipart import File

from core.ImageFile import image_read

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
    dark = image_read("sample/sample-dark1.jpeg")

    # class_table = calculate_common_time([file1, file2, file3, file4, file5, file6])
    # class_table.print()

