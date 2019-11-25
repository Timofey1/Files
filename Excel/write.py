import xlwt
book=xlwt.Workbook()
sheet=book.add_sheet('test')
sheet.write(0, 0, 100000)
book.save('fintest.xls')
print('book created')
