import os
import shutil

source = "/Users/mohuasen/iCloud Drive (Archive)/Desktop/"
dest1 = "/Users/mohuasen/iCloud Drive (Archive)/Desktop/Word/"
dest2 = "/Users/mohuasen/iCloud Drive (Archive)/Desktop/Powerpoint/"
dest3 = "/Users/mohuasen/iCloud Drive (Archive)/Desktop/Image/"
dest4 = "/Users/mohuasen/iCloud Drive (Archive)/Desktop/Randomwebsitesfromtheweb/"
all = os.listdir(source)
for file in all:
    if file.endswith(".docx") or file.endswith(".doc"):
        shutil.move(f"{source}{file}", dest1)
        print("moving")
    elif file.endswith(".pptx") or file.endswith(".ppt"):
        shutil.move(F"{source}{file}", dest2)
        print("moving2")
    elif file.endswith(".jpeg") or file.endswith(".png") or file.endswith(".HEIC") or file.endswith(".jpg") or file.endswith(".PNG") or file.endswith(".JPG"):
        shutil.move(f"{source}{file}", dest3)
        print("moving3")
    elif file.endswith(".html"):
        shutil.move(f"{source}{file}", dest4)
        print("moving4")
    

