# gap-between-classes 

시간표 이미지로 공통 공강 확인하기

1. 다수의 대학교 시간표 이미지 업로드 

<img width="400" alt="image" src="https://user-images.githubusercontent.com/46060746/215980251-ec72b2cb-2431-47c6-a270-fb80201db826.png">

2. 기기별 상이한 전체 이미지 크기에 따라 각 교시의 좌표 계산

<img width="378" alt="image" src="https://user-images.githubusercontent.com/46060746/215980691-ad588da9-af5e-4cd0-bb60-5301ca8c1d8a.png">

3. Opencv 흑백 전환

<img width="397" alt="image" src="https://user-images.githubusercontent.com/46060746/215981015-3c13d27b-27e7-418c-af79-c259a1c2495e.png">

4. 이진화, 공강 여부 배열 생성

![스크린샷 2022-08-10 오전 8 11 18](https://user-images.githubusercontent.com/46060746/215981562-2cbf470e-8c6c-412b-9b4e-39e11d4705cd.png)

5. 각 이미지 파일의 공통 공강 시간을 이진 배열로 바꿔 응답

``` python
@app.post("/classTime")
async def read_item(files: List[UploadFile] = File(...)):
  images = []
  for file in files:
      file = await file.read()
      images.append(file_to_image(file))
  common_time = calculate_common_time(images)
  return {"common_table": common_time}
```
