import os

cmd = "cd /Users/mohuasen && touch test.txt"
os.system(cmd)
with open("test.txt", "w+") as file:
    file.write("hi")
    file.write(" \n")
    file.write("bye")
    file.close()