# Moodle Login

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
print("type 1 for CSD1113  (Web Technology 01)")
print("type 2 for CSD1133  (Problem Solving)")
print("type 3 for CSD1194  (Business application)")
print("type 4 for CSD1233  (Python Programming)")
print("type 5 for CSD2206  (Database SQl)")
choice = int(input("Enter your choice: "))
driver = webdriver.Chrome()
driver.get("https://moodle.queenscollege.ca/moodle")

login = driver.find_element_by_xpath("//*[@id='page-site-index']/nav/ul[3]/li[2]/div/a")
action = ActionChains(driver)
action.click(on_element = login)
action.perform()
time.sleep(2)
username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
remember = driver.find_element_by_id("rememberusername")
login_btn = driver.find_element_by_id("loginbtn")
username.send_keys(" Your Username ") # Add your Moodle Username Here
password.send_keys(" Your Password ") # Add your Moodle Password Here
action = ActionChains(driver)
action.click(on_element = remember)
action.perform()
action = ActionChains(driver)
action.click(on_element = login_btn)
action.perform()
time.sleep(2)
driver.get("https://moodle.queenscollege.ca/moodle/course/index.php?mycourses=1")
#CSD1113 = driver.find_element_by_xpath('//*[@id="yui_3_17_2_1_1618836842447_37"]/div[1]/div/div[2]/div/h4/a')
#CSD1133 = driver.find_element_by_xpath("//*[@id='yui_3_17_2_1_1618833774571_37']/div[2]/div/div[2]/div/h4/a")
#CDS1194 = driver.find_element_by_xpath("//*[@id='yui_3_17_2_1_1618833774571_37']/div[3]/div/div[2]/div/h4/a")
#CSD1233 = driver.find_element_by_xpath("//*[@id='yui_3_17_2_1_1618833774571_37']/div[4]/div/div[2]/div/h4/a")
#CSD2206 = driver.find_element_by_xpath("//*[@id='yui_3_17_2_1_1618833774571_37']/div[5]/div/div[2]/div/h4/a")

if(choice==1):
    driver.get("https://moodle.queenscollege.ca/moodle/course/view.php?id=4494")
elif(choice==2):
    driver.get("https://moodle.queenscollege.ca/moodle/course/view.php?id=4456")
elif(choice==3):
    driver.get("https://moodle.queenscollege.ca/moodle/course/view.php?id=4669")
elif(choice==4):
    driver.get("https://moodle.queenscollege.ca/moodle/course/view.php?id=4633")
elif(choice==5):
    driver.get("https://moodle.queenscollege.ca/moodle/course/view.php?id=4613")
else:
    driver.close()
    print("Invalid input")