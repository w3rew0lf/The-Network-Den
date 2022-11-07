import openpyxl
wb = openpyxl.Workbook() 
sheet = wb.active
def cellEntry(row, column, attribute ):
    new_cell = sheet.cell(row, column)
    new_cell.value = str(attribute)

cellEntry(1,1,"Localtime")
cellEntry(1,2,"Source IP")
cellEntry(1,3,"Source Port")
cellEntry(1,4,"Destination IP")
cellEntry(1,5,"Destination Port")
cellEntry(1,6,"Protocol")
wb.save("log.xlsx")