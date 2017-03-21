from openpyxl import load_workbook
import warnings
warnings.simplefilter("ignore")
book=load_workbook('export.xlsx')
sheet=book.active


