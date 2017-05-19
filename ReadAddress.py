import xlrd
workbook = xlrd.open_workbook('my_file_name.xls')


#workbook = xlrd.open_workbook('my_file_name.xls', encoding='cp1252')
workbook = xlrd.open_workbook('E:\001_Satish\Learn\Python\Sample Addresses.xlsx')
#workbook = xlrd.open_workbook('my_file_name.xls', on_demand = True)

worksheet = workbook.sheet_by_name('Address')
#If you are not sure of the name of the sheet, you can open the first worksheet by its index:
#worksheet = workbook.sheet_by_index(0)
#workbook.nsheets wants to know the number of sheets. workbook.sheet_names() gives you a list of the names of the sheets present in the file, 
#which helps you iterate over the sheets.

#Getting data from cells
#Once you have selected the worksheet, you can extract the value of a particular data cell as follows.

# Value of 1st row and 1st column
for 
Address.cell(0, 0).value

You can iterate it over a loop to extract data in the whole sheet.

You can detect an empty cell by using empty_cell in xlrd.

if sheet.cell(0, 0).value == xlrd.empty_cell.value:
    # Do something
Creating spreadsheets
The workflow for creating worksheets is similar to that of the previous section.

Import the module xlwt
Create a blank spreadsheet file (or workbook)
Create a sheet within the file
Put desired values in particular data cells
Save the workbook
Create a new file
