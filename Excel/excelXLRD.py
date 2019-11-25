import xlrd
import xlwt

fio = 'Богдан Дарья Александровна'
month = 'сентябрь'
date = 10

workbook = xlrd.open_workbook('C:\Games\export.xls', on_demand=True)
sheet = workbook.sheet_by_index(0)

book = xlwt.Workbook()
sheet1 = book.add_sheet("test")

for i in range(sheet.nrows):
    data = sheet.cell_value(i, 0)
    if data == fio:
        currow = i
        break
for i in range(sheet.ncols):
    data = sheet.cell_value(0, i)
    if data == month:
        curcol = i
        break
for i in range(curcol, sheet.ncols - curcol):
    data = sheet.cell_value(1, i)
    if data == date:
        curcol = i
        break

print(currow, curcol)
res = "X"
sheet1.write(currow, curcol, res)

for i in range(sheet.nrows):
    for j in range(sheet.ncols):
        if i == currow and j == curcol:
            continue
        data = sheet.cell_value(i, j)
        sheet1.write(i, j, data)

book.save('fintest.xls')
print('book created')
