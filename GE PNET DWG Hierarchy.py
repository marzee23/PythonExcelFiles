import os
import easygui as eg
import xlsxwriter

workbook = xlsxwriter.Workbook("GE_PNET_DWG_Hierarchy.xlsx")
filepath = eg.enterbox("Enter directory name with files to search")

if os.path.exists(filepath):

	bold=workbook.add_format({'bold':True})
	worksheet = workbook.add_worksheet("GE_PNET_DWG_Hierarchy")
	worksheet.write('A1','File_Pathway', bold)
	row = 0
	#restart new row + column
	col = 0
	for root, dirs, files in os.walk(filepath):
		for file in files:
			if file.endswith(".dwg"):
				row += 1
				worksheet.write(row, col, os.path.join(root, file))
	
	workbook.close()
	print("All Done!")

else:
	workbook.close()
	
	print("The pathway:", filepath, "is no good.")