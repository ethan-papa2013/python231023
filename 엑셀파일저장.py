import openpyxl
import random

# 엑셀 파일 생성
workbook = openpyxl.Workbook()
worksheet = workbook.active

# 열 제목 추가
worksheet.append(["ID", "Name", "수량", "가격"])

# 전자제품 리스트 (예시)
products = [
    {"id": "P001", "name": "스마트폰", "수량": random.randint(1, 10), "가격": random.randint(100, 1000)},
    {"id": "P002", "name": "노트북", "수량": random.randint(1, 10), "가격": random.randint(500, 1500)},
    {"id": "P003", "name": "태블릿", "수량": random.randint(1, 10), "가격": random.randint(200, 800)},
    # 다른 제품들을 추가할 수 있습니다.
]

# 전자제품 리스트를 100개의 행으로 추가
for _ in range(100):
    product = random.choice(products)
    worksheet.append([product["id"], product["name"], product["수량"], product["가격"]])

# 엑셀 파일 저장
workbook.save("c:/work/sales.xlsx")
