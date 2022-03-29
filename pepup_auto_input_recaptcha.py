#!/usr/bin/env python3

import time
import json
from selenium import webdriver
import datetime
import random
import argparse
from selenium.webdriver.chrome import service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

parser = argparse.ArgumentParser()
parser.add_argument('--user', type=str)
parser.add_argument('--password', type=str)
args = parser.parse_args()

CHROMEDRIVER = "/snap/bin/chromium.chromedriver"
EXTENSION_PATH = "/home/hattori/Buster_Captcha_1.3.1.0.crx"
chrome_service = service.Service(executable_path=CHROMEDRIVER)

options = webdriver.ChromeOptions()
options.add_argument(f'service={chrome_service}')
options.add_extension(EXTENSION_PATH)

# pass captcha and then login
driver = webdriver.Chrome(options=options)
driver.get('https://pepup.life/home')
time.sleep(random.randint(1,3))

driver.switch_to.frame(0)
time.sleep(random.randint(1,3))

driver.find_element(By.CSS_SELECTOR, ".recaptcha-checkbox-border").click()
time.sleep(random.randint(3,6))

driver.switch_to.default_content()
time.sleep(random.randint(1,3))

driver.switch_to.frame(2)
time.sleep(random.randint(1,3))

for _ in range(20):
  try:
    driver.find_element(By.CSS_SELECTOR, ".help-button-holder").click()
    time.sleep(random.randint(3,5))
  except Exception:
          pass

driver.switch_to.default_content()
user = driver.find_element_by_id("sender-email")
user.send_keys(args.user)
time.sleep(random.randint(1,3))

password = driver.find_element_by_id("user-pass")
password.send_keys(args.password)
time.sleep(random.randint(1,3))

commit = driver.find_element_by_name("commit")
commit.click()
time.sleep(random.randint(1,3))

# go to wakuwaku input page and submit today's data

d = datetime.datetime.now() 
date = d.strftime('%Y/X%m/X%d').replace('X0','X').replace('X','')
driver.get('https://pepup.life/scsk_mileage_campaigns/%s' % date)
time.sleep(random.randint(1,3))

# walking
random_step = random.randrange(10000,15000,100)
step_count = driver.find_element_by_css_selector("div:nth-child(1) > .sc-1mklvxx-5")
step_count.clear()
step_count.send_keys(random_step)
time.sleep(0.05)

# sleep time
sleep_time = driver.find_element_by_css_selector("div:nth-child(2) > .sc-1mklvxx-5")
sleep_time.clear()
sleep_time.send_keys("8")
time.sleep(0.05)

# sleep condition
#param3 = driver.find_element_by_css_selector("div:nth-child(3) > .sc-1mklvxx-6 .sc-1mklvxx-8")
param3 = driver.find_element_by_xpath("//label[contains(.,\'自分にとって良い睡眠習慣を実行する\')]")
if param3.is_selected():
    time.sleep(0.05)
else:
    param3.click()
    time.sleep(0.05)

# alcohol
#param4 = driver.find_element_by_css_selector("div:nth-child(4) > .sc-1mklvxx-6 > .sc-1mklvxx-7")
param4 = driver.find_element_by_xpath("//label[contains(.,\'アルコール摂取20ｇ以内（休肝日含む）\')]")
print(param4.is_selected())
print(param4.is_displayed())
if param4.is_selected():
    time.sleep(0.05)
else:
    param4.click()
    time.sleep(0.05)

# do not drink after dinner
#param5 = driver.find_element_by_css_selector("div:nth-child(5) > .sc-1mklvxx-6:nth-child(2) .sc-1mklvxx-8")
param5 = driver.find_element_by_xpath("//label[contains(.,\'夕食（飲酒）後の夜食（締め）を食べない\')]")
if param5.is_selected():
    time.sleep(0.05)
else:
    param5.click()
    time.sleep(0.05)

# calory
#param6 = driver.find_element_by_css_selector(".sc-1mklvxx-6:nth-child(3) .sc-1mklvxx-8")
param6 = driver.find_element_by_xpath("//label[contains(.,\'必要摂取カロリーを意識して1日の食事を組み立てる\')]")
if param6.is_selected():
    time.sleep(0.05)
else:
    param6.click()
    time.sleep(0.05)

# syusyoku, syusai, fukusai
#param7 = driver.find_element_by_css_selector(".sc-1mklvxx-6:nth-child(4) .sc-1mklvxx-8")
param7 = driver.find_element_by_xpath("//label[contains(.,\'「主食」「主菜」「副菜」をバランスよく摂る\')]")
if param7.is_selected():
    time.sleep(0.05)
else:
    param7.click()
    time.sleep(0.05)

# do not eat snack between meal
#param8 = driver.find_element_by_css_selector(".sc-1mklvxx-6:nth-child(5) .sc-1mklvxx-8")
param8 = driver.find_element_by_xpath("//label[contains(.,\'糖質を多く含む間食を控える\')]")
if param8.is_selected():
    time.sleep(0.05)
else:
    param8.click()
    time.sleep(0.05)

# eat breakfast
#param9 = driver.find_element_by_css_selector(".sc-1mklvxx-6:nth-child(6) .sc-1mklvxx-8")
param9 = driver.find_element_by_xpath("//label[contains(.,\'朝食を食べる\')]")
if param9.is_selected():
    time.sleep(0.05)
else:
    param9.click()
    time.sleep(0.05)

# submit
#submit = driver.find_element_by_css_selector(".sc-g7yrzm-7")
submit = driver.find_element_by_xpath("//button[contains(.,\'一括入力\')]")
submit.click()
time.sleep(1)

driver.quit()
