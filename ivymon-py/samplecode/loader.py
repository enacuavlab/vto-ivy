#!/usr/bin/env python3.4

# loading a file from a pickle save
import pickle
FILE = "demoienac.p"
memory = pickle.load(open(FILE, "rb"))
print(len(memory))
print(memory[0])

# loading and parsing a excel worksheet
# TODO: pip3 install xlrd
# import xlrd
def excelread():
    book = xlrd.open_workbook("book.xlsx")
    sheet1 = book.sheet_by_index(0)
    print(sheet1.row_values(0))
    print(sheet1.row_values(1))
    print(sheet1.cell(0,0))
