#Before you run this program. Please satisfy all the requirements and read all of the comments in the program as well.
#Please make sure that to whomsover you are going to send the message, that number is in your contact list. (it doesn't
#matter if you are in there contact list or not).
#Don't forget to change paths.
#Don't forget to choose proper selenium driver for your operating system and browser. https://www.selenium.dev/downloads/

from selenium import webdriver
from time import sleep
import pyautogui as gui
from selenium.webdriver.common.keys import Keys
import pandas as pdata
import random as random_num
from selenium.common.exceptions import NoSuchElementException

array_phone = []
array_notreached = []
string1 = str
string2 = str

#Below-mentioned path is for mac. You may change it accordingly for windows.
data_file = pdata.read_excel('/Users/user_name/phone_list.xls', 'Sheet1')

# this array can also be used in place of excel file
# numbers = {'+919999999999', '+919999999999', '+919999999999', '+919999999999'}

numbers = data_file['Phone']
names = data_file['Name']

#Don't forget to choose proper selenium driver for your operating system and browser. https://www.selenium.dev/downloads/
driver = webdriver.Chrome("/drivers/chrome")
driver.get('https://web.whatsapp.com/')

# give path of jpg file which needs to be sent
filepath = input('Enter your filepath (images/video): ')

#it will keep on waiting for your to press enter. Because sometimes scanning QR code takes time.
input('Enter anything after scanning QR code')

for i, n in zip(numbers, names):

    try:
        user = driver.find_element_by_class_name('_13NKt') #this class name changes after a few days by whatsapp so
        # I suggest you to please refer  the readme for getting value of it.
        user.send_keys(i)
        user.send_keys(Keys.RETURN)

        attachment_box = driver.find_element_by_xpath('//div[@title = "Attach"]')
        attachment_box.click()

        image_box = driver.find_element_by_xpath(
                    '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        image_box.send_keys(filepath)
        sleep(random_num.randint(5, 10))

        user2 = driver.find_element_by_class_name('_13NKt') #this class name changes after a few days by whatsapp so
        # I suggest you to please refer  the readme for getting value of it.
        user2.send_keys('Hello ' + n + ' Any Caption for the image')
        send_button = driver.find_element_by_xpath('//span[@data-icon="send"]')
        send_button.click()
        #I have added random sleep and refresh to stop your account from getting blocked and whatsapp should not
        # get to know about this automation.
        sleep(random_num.randint(10, 15))
        driver.refresh()
        sleep(random_num.randint(20, 45))

    except NoSuchElementException:
        array_phone.append(i)

        try:
            #In some cases there is a problem that the phone number is not in contact list of yours. Then the number
            # stays in search bar. So this option is to clear the occupied space.
            user = driver.find_element_by_class_name('_13NKt') #this class name changes after a few days by whatsapp so
        # I suggest you to please refer  the readme for getting value of it.
            user.clear()
            i = 0
            driver.refresh()
            continue
        except NoSuchElementException:
            array_notreached.append(i)

print("Numbers not on whatsapp")
for m in array_phone:
    print(m)


print("Numbers not reachable due to network issue")
for nr in array_notreached:
    print(nr)