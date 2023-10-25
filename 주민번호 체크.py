import random
import re

def generate_random_korean_resident_number():
    # 연월일 부분을 랜덤으로 생성
    year = random.randint(0, 99)
    month = random.randint(1, 12)
    day = random.randint(1, 31)

    # 검증부분을 랜덤으로 생성 (1 또는 2)
    check_digit = random.randint(1, 2)

    # 주민등록번호 형식으로 조합
    resident_number = f"{year:02d}{month:02d}{day:02d}-{check_digit}{random.randint(100000, 999999)}"

    return resident_number

def is_valid_korean_resident_number(resident_number):
    # 주민등록번호 형식을 정규식으로 검사
    pattern = re.compile(r'^\d{6}-[1-2]\d{6}$')
    
    if not pattern.match(resident_number):
        return False

    # 주민등록번호를 '-'를 기준으로 나누어 연월일 부분과 검증부분을 분리
    parts = resident_number.split('-')
    birth_date = parts[0]
    check_digit = parts[1]

    # 연월일 부분 검사
    year = int(birth_date[:2])
    month = int(birth_date[2:4])
    day = int(birth_date[4:6])

    if year < 0 or year > 99 or month < 1 or month > 12 or day < 1 or day > 31:
        return False

    # # 검증부분 검사
    # check_gen = list(check_digit)
    # if check_gen[0] != 1 or 2:
    #     return False

    # return True

# 10개의 랜덤 주민등록번호 생성 및 유효성 검사
for _ in range(10):
    random_resident_number = generate_random_korean_resident_number()
    if is_valid_korean_resident_number(random_resident_number):
        print(f"{random_resident_number}는 유효한 주민등록번호입니다.")
    else:
        print(f"{random_resident_number}는 유효하지 않은 주민등록번호입니다.")
