import pandas as pd

def excelParser(name, sheet):
    xls = pd.ExcelFile(name)
    df = pd.read_excel(xls, sheet)
    return df