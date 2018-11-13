import pandas as pd

file = 'NBS-e-NEBS-em-excel.xlsx'

xl = pd.ExcelFile(file)

print(xl.sheet_names)
