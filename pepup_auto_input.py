#!/usr/bin/env python3

import time
import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import datetime
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--user', type=str)
parser.add_argument('--password', type=str)
args = parser.parse_args()

driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)

# login
driver.get('https://pepup.life/home')

user = driver.find_element_by_id("sender-email")
user.send_keys(args.user)

password = driver.find_element_by_id("user-pass")
password.send_keys(args.password)

commit = driver.find_element_by_name("commit")
commit.click()
time.sleep(3)

# go to wakuwaku input page and submit today's data

d = datetime.datetime.now() 
date = d.strftime('%Y/X%m/X%d').replace('X0','X').replace('X','')
driver.get('https://pepup.life/scsk_mileage_campaigns/%s' % date)
time.sleep(3)

# walking
random_step = random.randrange(10000,15000,500)
step_count = driver.find_element_by_css_selector("div:nth-child(1) > .sc-ycydyz-5")
step_count.send_keys(random_step)
time.sleep(3)

# sleep time
sleep_time = driver.find_element_by_css_selector("div:nth-child(2) > .sc-ycydyz-5")
sleep_time.send_keys("8")
time.sleep(3)

# sleep condition
param3 = driver.find_element_by_css_selector("div:nth-child(3) > .sc-ycydyz-6 .sc-ycydyz-8")
param3.click()
time.sleep(3)

# alcohol
param4 = driver.find_element_by_css_selector("div:nth-child(4) > .sc-ycydyz-6 .sc-ycydyz-8")
param4.click()
time.sleep(3)

# do not drink after dinner
param5 = driver.find_element_by_css_selector("div:nth-child(5) > .sc-ycydyz-6:nth-child(2) .sc-ycydyz-8")
param5.click()
time.sleep(3)

# calory
param6 = driver.find_element_by_css_selector(".sc-ycydyz-6:nth-child(3) .sc-ycydyz-8")
param6.click()
time.sleep(3)

# syusyoku, syusai, fukusai
param7 = driver.find_element_by_css_selector(".sc-ycydyz-6:nth-child(4) .sc-ycydyz-8")
param7.click()
time.sleep(3)

# do not eat snack between meal
param8 = driver.find_element_by_css_selector(".sc-ycydyz-6:nth-child(5) .sc-ycydyz-8")
param8.click()
time.sleep(3)

# eat breakfast
param9 = driver.find_element_by_css_selector(".sc-ycydyz-6:nth-child(6) .sc-ycydyz-8")
param9.click()
time.sleep(3)

# submit
submit = driver.find_element_by_css_selector(".sc-afzobm-7")
submit.click()
time.sleep(5)

driver.quit()
