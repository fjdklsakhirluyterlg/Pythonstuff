import os
import shutil
import time

#change these for your own file system, on windows it would be C:\path\
source = "/Users/mohuasen/prev/all/Armaan"            
dest1 = "/Users/mohusen/prev/all/Armaan/EXCEL DOCS/"
dest2 = "/Users/mohusen/prev/all/Armaan/Zips/"
dest3 = "/Users/mohusen/prev/all/Armaan/CSVS/"
dest4 = "/Users/mohusen/prev/all/Armaan/WordDocs"
dest5 = "/Users/mohusen/prev/all/Armaan/Images"
dest6 = "/Users/mohusen/prev/all/Armaan/PDFS"
dest7 = "/Users/mohusen/prev/all/Armaan/Websites"
dest8 = "/Users/mohusen/prev/all/Armaan/Powerpoints"

    
def move_flies():
    all = os.listdir(source)
    for file in all:
        if file.endswith(".xlsx"):
            shutil.move(f"{source}{file}", dest1)
            print("moving")
        elif file.endswith(".xls"):
            shutil.move(f"{source}{file}", dest1)
            print("moving")
        elif file.endswith(".zip"):
            shutil.move(f"{source}{file}", dest2)
            print("moving2")
        elif file.endswith(".csv"):
            shutil.move(f"{source}{file}", dest3)
            print("moving3")
        elif file.endswith(".docx"):
            shutil.move(f"{source}{file}", dest4)
            print("moving4")
        elif file.endswith(".png"):
            shutil.move(f"{source}{file}", dest5)
            print("moving5")
        elif file.endswith(".ods"):
            shutil.move(f"{source}{file}", dest1)
            print("moving")
        elif file.endswith(".html"):
            shutil.move(f"{source}{file}", dest7)
            print("moving7")
        elif file.endswith(".webarchive"):
            shutil.move(f"{source}{file}", dest7)
            print("moving7")
        elif file.endswith(".pptx"):
            shutil.move(f"{source}{file}", dest8)
            print("moving8")
        elif file.endswith(".pdf"):
            shutil.move(f"{source}{file}", dest6)
            print("moving6")
        elif file.endswith(".doc"):
            shutil.move(f"{source}{file}", dest4)
            print("moving4")
        elif file.endswith(".jpeg"):
            shutil.move(f"{source}{file}", dest5)
            print("moving5")
        elif file.endswith(".jpg"):
            shutil.move(f"{source}{file}", dest5) #moves the file from one place to another
            print("moving5")

move_flies()