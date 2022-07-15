import shutil
import os

source = "/Users/mohuasen/Armaan"
destination = "/Users/mohuasen/Armaan/CSVz"

files = os.listdir(source)

for file in files:
	if file.endswith(".csv"):
                new_path = shutil.move(f"{source}/{file}", destination)
                print(new_path)
