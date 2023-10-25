import re

# 정규 표현식 패턴
#r(raw string notation)
email_pattern = r'^[\w\.-]+@[\w\.-]+\.[a-z|A-Z]+$'

# 이메일 주소를 포함한 텍스트
text = """이메일 주소 목록:
john.doe@example.com
jane.doe@subdomain.example.co.uk
test_email@email.co
invalid.email@.com
missing_at_symbol.com
email_with_special_chars@example_123.com
"""

# 정규 표현식을 사용하여 이메일 주소 검사
matches = re.findall(email_pattern, text)

if matches:
    print("검출된 이메일 주소:")
    for email in matches:
        print(email)
else:
    print("이메일 주소를 찾을 수 없습니다.")
