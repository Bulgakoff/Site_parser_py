import xlsxwriter
from o_O import get_arr
import time

def writer(param_tuple):
    book = xlsxwriter.Workbook(r"C:\PPP_1\python_tricks-master\scraping\data2.xsls")
    page = book.add_worksheet("товар")

    row = 0
    column = 0

    page.set_column("A:A", 20)
    page.set_column("B:B", 20)
    page.set_column("C:C", 50)
    page.set_column("D:D", 50)

    for item in param_tuple():
        page.write(row, column, item[0])
        page.write(row, column + 1, item[1])
        page.write(row, column + 2, item[2])
        page.write(row, column + 3, item[3])
        row += 1

    book.close()

begin = time.time()
writer(get_arr)
after =time.time()
print(after-begin)