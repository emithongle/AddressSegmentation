__author__ = 'Thong_Le'

from libs.store import loadCSV, saveCSV
import datetime
from time import gmtime, strftime

# import csv
# with open('xyz.csv', newline='') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# data = loadCSV('abc')
# saveCSV(data, 'xyz')
# ==============================================
# t = datetime.datetime.now()
# print(str(t.date().strftime('%Y%m%d')) + '_' + str(t.time().strftime('%H%M%S')))
# ==============================================

import xlrd

book = xlrd.open_workbook('running_logs/logs.xlsx')

# get the first worksheet
first_sheet = book.sheet_by_index(0)

# read a row
for i in range(first_sheet.nrows):
    print(first_sheet.row_values(i))



# read a cell
cell = first_sheet.cell(0,0)
print(cell)
print(cell.value)

# read a row slice
print(first_sheet.row_slice(rowx=0,
                            start_colx=0,
                            end_colx=2)
      )
None