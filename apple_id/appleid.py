# selenium cheatsheet <https://gist.github.com/huangzhichong/3284966>
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome("/Users/otavio/Dropbox (Personal)/GrubHub/grubs/chromedriver")

browser.get('https://appleid.apple.com/account#!&page=create')

# 1. Sign Up 
email = browser.find_element_by_type("email");
email.send_keys("hell yes")

email=browser.find_element_by_xpath("//input[@placeholder='name@example.com']")
email.send_keys("doug.hu.work+7@gmail.com")

pw = browser.find_element_by_id("password");
pw.send_keys("Poiu0987!")

conf_pw=browser.find_element_by_xpath("//input[@placeholder='confirm password']")
conf_pw.send_keys("Poiu0987!")

first=browser.find_element_by_xpath("//input[@placeholder='first name']")
first.send_keys("Doug")

last=browser.find_element_by_xpath("//input[@placeholder='last name']")
last.send_keys("Hu")

birthday=browser.find_element_by_xpath("//input[@placeholder='birthday']")
birthday.send_keys("02/20/1988")

answer=browser.find_element_by_xpath("//input[@placeholder='answer']")
answer.send_keys("333")

# Doesn't work:
select = browser.find_element_by_class_name("security-question130");
select.selectByVisibleText("What is the first name of your best friend in high school?");


# 2. Adding payment

card = browser.find_element_by_xpath("//button[@class='button button-link button-large add-card acdn-btn-edit']")
card.click()

number=browser.find_element_by_xpath("//input[@placeholder='credit card number']")
number.send_keys("5403 0203 5310 7550")

exp=browser.find_element_by_xpath("//input[@placeholder='mm/yyyy']")
exp.send_keys("032017")

cvv=browser.find_element_by_xpath("//input[@placeholder='security code']")
cvv.send_keys("958")

street=browser.find_element_by_xpath("//input[@placeholder='street address']")
street.send_keys("587 N 6th St")

city=browser.find_element_by_xpath("//input[@placeholder='city']")
city.send_keys("san jose")

zipc=browser.find_element_by_xpath("//input[@placeholder='zip code']")
zipc.send_keys("95112")

phone=browser.find_element_by_xpath("//input[@placeholder='phone number']")
phone.send_keys("4082783674")

elem = browser.find_element_by_class_name("email-input email-input-wrapper")
elem.send_keys("hell yes")
elem.submit()

# end

elem = browser.find_element_by_class_name("email-input email-input-wrapper")

try:
    email = browser.find_element_by_class_name("email-input email-input-wrapper")
except:
    print('Was not able to find an element with that name.')

browser.get("https://google.com")
elem = browser.find_element_by_name("q")
elem.send_keys("hell yes")
elem.submit()

try:
    email = browser.findElement(By.id("email-input email-input-wrapper"));
except:
    print('Was not able to find an element with that name.')





email.send_keys("doug.hu.work+7@gmail.com")
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

# binary = FirefoxBinary('Applications/Firefox.app')
# browser = webdriver.Firefox(firefox_binary=binary)

# browser = webdriver.Firefox()

