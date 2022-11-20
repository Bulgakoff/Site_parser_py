import xlsxwriter
from o_O1 import get_arr
import time


def writer(param_tuple):
    book = xlsxwriter. \
        Workbook(r"C:\PPP_1\python_tricks-master\scraping\data1.xsls")
    page = book.add_worksheet("tags")

    row = 0
    column = 0

    page.set_column("A:A", 20)
    page.set_column("B:B", 100)

    for item in param_tuple():
        page.write(row, column, item[0])
        page.write(row, column + 1, item[1])
        row += 1

    book.close()


begin = time.time()
writer(get_arr())
after = time.time()
print(after - begin)
