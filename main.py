from openpyxl.workbook import Workbook
from openpyxl import load_workbook

asin_list = []
country_list = []
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

url_list = []
i = 0
for asin, country in (zip(asin_list, country_list)):
    url_list.insert(i, f"https://www.amazon.{country}/dp/{asin}")
    i = i+1

print(url_list)
