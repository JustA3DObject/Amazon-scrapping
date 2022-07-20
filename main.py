import csv
import requests
from bs4 import BeautifulSoup
from openpyxl.workbook import Workbook
from openpyxl import load_workbook

asin_list = []
country_list = []
url_list = []
wb = load_workbook("Amazon Scraping.xlsx")
ws = wb.active
col_asin = ws["C"]
col_country = ws["D"]


def make_asin_list():
    for index, item in enumerate(col_asin):
        asin_list.insert(index, item.value)

    for index, item in enumerate(asin_list):
        if type(item) == float:
            asin_list[index] = int(item)

    asin_list.pop(0)


def make_country_list():
    for index, item in enumerate(col_country):
        country_list.insert(index, item.value)

    country_list.pop(0)


make_asin_list()
make_country_list()


def make_url_list():
    i = 0
    for asin, country in (zip(asin_list, country_list)):
        url_list.insert(i, f"https://www.amazon.{country}/dp/{asin}")
        i = i+1


make_url_list()
# print(url_list)

j = 100
while(j < 200):

    try:
        URL = url_list[j]
        j = j+1
        # headers from https://httpbin.org/get

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36",
                   "X-Amzn-Trace-Id": "Root=1-62d8036d-2b173c1f2e4e7a416cc9e554", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                   "Accept-Encoding": "gzip, deflate, br", }
        page = requests.get(URL, headers=headers)
        soup1 = BeautifulSoup(page.content, "html.parser")
        soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
        title = soup2.find(id="productTitle").get_text()
        price = soup2.find(class_="a-offscreen").get_text()
        about = soup2.find(
            class_="a-unordered-list a-vertical a-spacing-mini").get_text()
        img_url = soup2.find(id="landingImage")

        title = title.strip()
        price = price.strip()
        about = about.strip()
        img_url = img_url['src'].strip()

    except AttributeError:
        print("404 ERROR!")
        title = "404 ERROR!"

        header = ["Product"]
        data = [title]
        with open("AmazonScraperData.csv", 'a+', newline='', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(data)

    else:
        header = ["Product", "Price", "Details", "Image URL"]
        data = [title, price, about, img_url]
        with open("AmazonScraperData.csv", 'a+', newline='', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(data)
