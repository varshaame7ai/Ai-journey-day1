import openpyxl

# Nayi Excel file banao
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "PriceList"

# Heading daalo
sheet['A1'] = "Product"
sheet['B1'] = "Price"

# Data daalo List se
products = ["Mouse", "Keyboard", "Monitor", "CPU", "Laptop"]
price = 750

row = 2
for product in products:
    sheet['A' + str(row)] = product
    sheet['B' + str(row)] = price
    row = row + 1

# File save kar do
wb.save("Client_PriceList.xlsx")
print("Excel file ban gayi! Phone ke storage mein check karo")
