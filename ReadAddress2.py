# This works!

import openpyxl, pprint
print ('Opening workbook ...')

wb = openpyxl.load_workbook('/Users/satishseshadri/001_Satish/Learn/Python/Sample Addresses.xlsx')

sheet = wb.get_sheet_by_name('Address')

AddresList={}

print ('Reading rows...')
for row in range(2, sheet.max_row+1):
	Name = sheet['A' + str(row)].value
	Email	 = sheet['B' + str(row)].value
	Street	 = sheet['C' + str(row)].value
	City	 = sheet['D' + str(row)].value
	State	 = sheet['E' + str(row)].value
	Zip = sheet['F' + str(row)].value

	#print (Name)
	#print (Email)
	#print (Street)
	#print (City)
	#print (State)
	#print (Zip)
	print (Name + ' ' + Email + ' ' + Street + ' ' + City + ' ' + State + ' ' + str(Zip))
        
