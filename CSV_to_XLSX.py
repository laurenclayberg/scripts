import sys
import csv
import xlsxwriter

wb = xlsxwriter.Workbook(sys.argv[1].replace(".csv", ".xlsx"))
ws = wb.add_worksheet("Sheet 1")

with open(sys.argv[1], 'r') as csvfile:
	table = csv.reader(csvfile)
	i = 0
	for row in table:
		ws.write_row(i, 0, row)
		i += 1
		
wb.close