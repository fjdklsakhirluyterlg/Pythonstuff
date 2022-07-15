import requests
import pwd
import os
import subprocess


url = "https://api.nasa.gov/planetary/apod?api_key=0Qndr4PLIh60y0TxWHDN0r4ZWiuMh7WGBbAsHAhy"
FILENAME = 'nasa_pic.png'


def get_filename():
    username = pwd.getpwuid(os.getuid()).pw_name
    directory = "/Users/mohuasen/Downloads"
        
    return os.path.join(directory, FILENAME)

  
def download_pic_of_day():
    r = requests.get(url)

    if r.status_code != 200:
        print('error')
        return
    
    picture_url = r.json()['url']
    if "jpg" not in picture_url:
        print("No image for today, must be something else")
    else:
        pic = requests.get(picture_url , allow_redirects=True)
        filename = get_filename()
        
        open(filename, 'wb').write(pic.content)
        
        print(f"saved picture of the day to {filename}!")

       

download_pic_of_day()
    
filename = get_filename()
    
cmd = "Automator /Users/mohuasen/Downloads/Desktop.workflow"

try:
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    print(output, error)
    print("changed picture")
    print(f"Run {cmd}")
except:
    print("Error")

