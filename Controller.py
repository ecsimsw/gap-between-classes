from fastapi import FastAPI, File, UploadFile
from typing import List

from core.ClassTime import class_time, common_class_table

app = FastAPI()


@app.get("/classTime")
def info():
    return {"ecsimsw": "2022.08.10"}


@app.post("/classTime")
async def read_item(files: List[UploadFile] = File(...)):
    file1 = await files[0].read()
    file2 = await files[1].read()

    class_times = [class_time(file1), class_time(file2)]
    print(type(class_times))
    common_table = common_class_table(class_times)
    return {"common_table": common_table}
