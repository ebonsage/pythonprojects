#!/usr/bin/env python
#coding:utf-8
"""
  Author:  coreyjones --<>
  Purpose: examples xlsx
  Created: 12/10/2018
"""
import os, openpyxl, logging, pprint

workingFiles = 'C:\\pyworkfiles'
xslxfile = "example.xlsx"
pp = pprint.pprint

#logging.disable(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


os.chdir(workingFiles)
pwd = os.getcwd()
logging.info('The current directory is: %s' % (pwd))

logging.info('Opening workbook named: %s' % (xslxfile))
workbook = openpyxl.load_workbook('example.xlsx')
logging.info('Opened filetype: %s' % type(workbook))

sheet = workbook.get_sheet_by_name('Sheet1')

sheet_names = workbook.get_sheet_names()

for sheetNames in sheet_names:
    print("Sheet: %s" % (sheetNames))
    
    
#grab cell data
celldata = sheet['A1']
print(celldata) #returns cell object
print(celldata.value) #grab data from cell



cvalstr = str(celldata.value)
pprint.pprint(cvalstr)
cvalstr1 = str(sheet['B1'].value)
pprint.pprint(cvalstr1)


pprint.pprint(sheet['C1'].value)    
pprint.pprint(str(sheet['C1'].value))


pprint.pprint(sheet.cell(row=1, column=2))
pp(sheet['B1'])


for i in range(1, 8):
    print(i, sheet.cell(row=i, column=2).value)
    


#create and modify xlsx workbooks

wb = openpyxl.Workbook()

wb.get_sheet_names()
sheet = wb.get_sheet_by_name('Sheet')

pp(sheet)
sheet['A1'].value
sheet['A1'] = 42
sheet['A2'] = 'Hello'

if not os.path.exists("example1.xlsx"):
    pp('Delete the example1 file first to see effect')
    wb.save('example1.xlsx')
    






























#if __name__ == '__main__':
    #unittest.main()