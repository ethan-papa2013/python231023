import requests
from bs4 import BeautifulSoup

# 검색할 주소
url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%EB%A7%A5%EB%B6%81"

# HTTP GET 요청 보내고 페이지 내용 가져오기
response = requests.get(url)
#html = response.text

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(response, "html.parser")

# 검색 결과를 포함하는 부분 찾기
search_results = soup.find_all("li", class_="bx")

# 각 검색 결과에서 필요한 정보 추출
for result in search_results:
    # 블로그 이름 추출
    blog_name = result.find("a", class_="sub_thumb").text
    
    # 블로그 주소 추출
    blog_url = result.find("a", class_="sub_thumb")["href"]
    
    # 글의 제목 추출
    title = result.find("a", class_="sh_blog_title").text
    
    # 날짜 추출
    date = result.find("dd", class_="txt_inline").text
    
    # 결과 출력
    print("블로그 이름:", blog_name)
    print("블로그 주소:", blog_url)
    print("글의 제목:", title)
    print("날짜:", date)
    print("\n")
