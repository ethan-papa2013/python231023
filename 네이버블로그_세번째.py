import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# Create an Excel workbook
workbook = Workbook()
sheet = workbook.active
sheet.title = "Naver Blog Data"

# Function to scrape and extract data from a Naver search page
def scrape_naver_blog_page(url, sheet):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        blog_entries = soup.find_all("li", class_="bx")
        for entry in blog_entries:
            blog_name = entry.find("a", class_="sub_text")
            blog_address = entry.find("a", class_="sub_thumb")
            post_title = entry.find("a", class_="sh_blog_title")
            date = entry.find("span", class_="sub_time")
            if blog_name and blog_address and post_title and date:
                sheet.append([
                    blog_name.get_text(),
                    blog_address["href"],
                    post_title["title"],
                    date.get_text()
                ])
    else:
        print("Failed to retrieve the page. Status code:", response.status_code)

# Iterate through pages 1 to 100
for page in range(1, 101):
    url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%EB%A7%A5%EB%B6%81&start={page * 10}"
    print(f"Scraping page {page}...")
    scrape_naver_blog_page(url, sheet)

# Save the data to an Excel file
workbook.save("c:/work/result.xlsx")
