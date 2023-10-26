#web2.py
#웹서버에 요청
import requests
#크롤링
from bs4 import BeautifulSoup

url = "https://www.daangn.com/fleamarket/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

#<dev class속성 딕셔너리>
#파일에 저장
f = open("c:\\work\\daangn.txt", "wt", encoding="utf-8")
posts = soup.find_all("div", attrs={"class":"card-desc"})

for post in posts:
    title = post.find("h2", attrs={"class","card-title"})
    price = post.find("div", attrs={"class","card-price"})
    addr = post.find("div", attrs={"class","card-region-name"})
    #메서드체인(함수체인)
    title = title.text.strip().replace("\n", "")
    price = price.text.strip().replace("\n", "")
    addr = addr.text.strip().replace("\n", "")
    print("{0}, {1}, {2}".format(title, price, addr))
    #f를 붙이고 변수명 넘기기
    f.write(f"{title}, {price}, {addr}\n")

f.close()

# <div class="card-photo ">
#         <img alt="다이슨청소기" src="https://dnvefa72aowie.cloudfront.net/origin/article/202310/513e07b899ac80b837b31927be6a6aca1489ea374970e7758f2ddc48ebba35aa_0.webp?q=82&amp;s=300x300&amp;t=crop&amp;f=webp">
#     </div>


