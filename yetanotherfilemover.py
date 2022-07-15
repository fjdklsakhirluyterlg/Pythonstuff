import os 
import shutil

source = "/Users/mohuasen/iCloud Drive (Archive)/Desktop/Powerpoint/"
source2 = "/Users/mohuasen/iCloud Drive (Archive)/Desktop/Word/"
dest = "/Users/mohuasen/iCloud Drive (Archive)/Desktop/Armaan/Powerpoints/"
dest2 = "/Users/mohuasen/iCloud Drive (Archive)/Desktop/Armaan/WordDocs/"

all = os.listdir(source)
for file in all:
    shutil.move(f"{source}{file}", dest)
    print("moving")

allf = os.listdir(source2)
for x in allf:
    try:
        shutil.move(f"{source2}{x}", dest2)
        print("moving2")
    except:
        continue