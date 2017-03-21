# import xlrd
# import xlwt
#
# workbook = xlrd.open_workbook('C:\Games\hintest.xlsx', on_demand=True)
# sheet = workbook.sheet_by_index(0)
# book=xlwt.Workbook()
# sheet1=book.add_sheet('test')
# for i in range(sheet.nrows):
#     for j in range(sheet.ncols):
#         data = sheet.cell_value(i, j)
#         sheet1.write(i, j, data)
#
# book.save('fintest.xls')
# print('book created')
