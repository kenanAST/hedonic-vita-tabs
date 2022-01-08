import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

f = open("cleandb.txt", "r")

names = f.read()
names = names.split(",")

sleep = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
sleepDistribution = [0, 0.008, 0.00825, 0.025, 0.09, 0.18, 0.2, 0.14, 0.09, 0.05, 0.01, 0.005]

work = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
workDistribution = [0, 0.008, 0.00825, 0.025, 0.09, 0.18, 0.2, 0.14, 0.09, 0.05, 0.01, 0.005]

age = [13,14,15,16,17,18,19,20,21,22,23,24]
ageDistribution = [0.0025, 0.008, 0.0085, 0.05, 0.17, 0.16, 0.12, 0.12, 0.09, 0.05, 0.01, 0.005]

buy = [1, 0]
buyDistribution = [0.92, 0.08]


# print(names[random.randint(0,999)])



for i in range(160):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://forms.gle/dzbwBkHNGfaVVAJ88')


    nameXpath = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
    sleepXpath = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
    workXpath = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'
    ageXpath = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input'
    yesXpath = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input'
    # noXpath = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div/div'
    submitXpath = '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span'
    time.sleep(1)
    namez = driver.find_element(By.XPATH, nameXpath)
    namez.click()
    namez.send_keys(names[random.randint(0,999)])

    sleepz = driver.find_element(By.XPATH, sleepXpath)
    sleepz.click()
    sleepz.send_keys(random.choices(sleep,sleepDistribution)[0])

    workz = driver.find_element(By.XPATH, workXpath)
    workz.click()
    workz.send_keys(random.choices(work,workDistribution)[0])


    agez = driver.find_element(By.XPATH, ageXpath)
    agez.click()
    agez.send_keys(random.choices(age,ageDistribution)[0])

    Buy = random.choices(buy,buyDistribution)[0]
    yes = driver.find_element(By.XPATH, yesXpath)
    if(Buy == 1):
        yes.send_keys("Yes")
    else:
        yes.send_keys("No")

    submit = driver.find_element(By.XPATH, submitXpath)
    submit.click()
    time.sleep(1)
    driver.close()












# for i in range(100):
    # print( str(i + 1) + ". " + names[random.randint(0,999)] + "\tSleep: " + str(random.choices(sleep, sleepDistribution)[0]) + "\tWork: " + str(random.choices(work, workDistribution)[0]) + "\tAge: " + str(random.choices(age, ageDistribution)[0]) )

