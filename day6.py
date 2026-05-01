import openpyxl

# Nayi Excel file banao
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "Real_PriceList"

# Heading daalo
sheet['A1'] = "Product"
sheet['B1'] = "Price"

# 2 Lists: Products aur unke Price
products = ["Mouse", "Keyboard", "Monitor", "CPU", "Laptop"]
prices = [500, 1200, 5000, 15000, 45000]

# Loop chalao - dono list saath mein
row = 2
for i in range(5): # 0 se 4 tak = 5 items
    sheet['A' + str(row)] = products[i] # i = 0,1,2,3,4
    sheet['B' + str(row)] = prices[i]
    row = row + 1

# File save kar do
wb.save("Varsha_Real_Prices.xlsx")
print("Real price wali Excel ban gayi! Check karo")
