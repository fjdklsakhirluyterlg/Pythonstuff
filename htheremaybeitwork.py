import csv
import shutil
import os

Source = "/Users/mohuasen/Downloads/"
Destination = "/Users/mohuasen/iCloud Drive (Archive)/Desktop/Armaan"
Destination1 = "/Users/mohuasen/iCloud Drive (Archive)/Desktop/Armaan/PDFS"
Destination2 = "/Users/mohuasen/iCloud Drive (Archive)/Desktop/Armaan/CSVS"
Destination3 = "/Users/mohuasen/iCloud Drive (Archive)/Desktop/Armaan/EXCEL DOCS"
Destination4 = "/Users/mohuasen/iCloud Drive (Archive)/Desktop/Armaan/Zips"

allfiles= os.listdir(Source)
print(allfiles)
for file in allfiles:
    if file.endswith(".pdf"):
        shutil.move(Source + file, Destination1 + file)
    elif file.endswith(".csv"):
        shutil.move(Source + file, Destination2 + file)
    elif file.endswith(".xlsx"):
        shutil.move(Source + file, Destination3 + file)
    elif file.endswith(".zip"):
        shutil.move(Source + file, Destination4 + file)
    else:
        shutil.move(Source + file, Destination + file)

