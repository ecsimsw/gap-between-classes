from typing import List

from fastapi import FastAPI, UploadFile, File

from core.ImageFile import file_to_image
from core.Service import calculate_common_time

app = FastAPI()


@app.get("/classTime")
def info():
    return {"ecsimsw": "2022.08.10"}


@app.post("/classTime")
async def read_item(files: List[UploadFile] = File(...)):
    images = []
    for file in files:
        file = await file.read()
        images.append(file_to_image(file))
    common_time = calculate_common_time(images)
    return {"common_table": common_time}
