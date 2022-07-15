import os
import shutil

source = "/Users/mohuasen/iCloud Drive (Archive)/Desktop/Armaan/"
Destination = "/Users/mohuasen/iCloud Drive (Archive)/Desktop/Armaan/PDFS"
Destination1 = "/Users/mohuasen/iCloud Drive (Archive)/Desktop/Armaan/CSVS"
Destination2 = "/Users/mohuasen/iCloud Drive (Archive)/Desktop/Armaan/EXCEL DOCS"
Destination3 = "/Users/mohuasen/iCloud Drive (Archive)/Desktop/Armaan/Zips"

allf = os.listdir(source)

for f in allf:
    if len(f) < 200:
        if f.endswith(".pdf"):
            shutil.move(source + f, Destination + f)
        elif f.endswith(".csv"):
            shutil.move(source + f, Destination1 + f)
        elif f.endswith(".xlsx"):
            shutil.move(source + f, Destination2 + f)
        elif f.endswith(".zip"):
            shutil.move(source + f, Destination3 + f)
        else:
            shutil.move(source + f, source + f)
    else:
        pass