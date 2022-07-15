from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
 
# Replace below path with the absolute path
# to chromedriver in your computer
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=/Users/mohuasen/Library/Application Support/Google/Chrome/Default")
driver = webdriver.Chrome(executable_path=r'/Users/mohuasen/chromedriver', options=options)
 
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 900)
 
# Replace 'Friend's Name' with the name of your friend
# or the name of a group
target = '"Phillip"'
 
# Replace the below string with your own message
string = "Message sent using Python test, sorry you were the first person to randomly choose"
x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((
    By.XPATH, x_arg)))
group_title.click()
inp_xpath = '//div[@class="_13NKt copyable-text selectable-text"][@data-tab="9"]'
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
for i in range(100):
    input_box.send_keys(string + Keys.ENTER)
    time.sleep(1)