import os
from openpyxl import Workbook

# Path to the folder containing the files
folder_path = "D:\karanqrcode\karanqrcode"

# Create a new Excel workbook
workbook = Workbook()
sheet = workbook.active

# Iterate through the files in the folder
for filename in os.listdir(folder_path):
    # Write the file name to the Excel sheet
    sheet.append([filename])

# Save the workbook
workbook.save("file_names.xlsx")
