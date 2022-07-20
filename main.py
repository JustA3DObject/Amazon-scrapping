from openpyxl.workbook import Workbook
from openpyxl import load_workbook

asin_list = []
wb = load_workbook("Amazon Scraping.xlsx")
ws = wb.active
col_asin = ws["C"]
col_country = ws["D"]

for index, item in enumerate(col_asin):
    asin_list.insert(index, item.value)

for index, item in enumerate(asin_list):
    if type(item) == float:
        asin_list[index] = int(item)

print(asin_list)
