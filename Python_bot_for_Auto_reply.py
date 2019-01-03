from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")

input("Press anything after QR scan")
time.sleep(5)


names = ["Me"]

for name in names:

    person = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    person.click()

    for i in range(1,3):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    msg_got = driver.find_elements_by_css_selector("span.selectable-text.invisible-space.copyable-text")
    msg = [message.text for message in msg_got]

    if msg[-1] == "Happy New Year":
        reply = driver.find_element_by_class_name("_2S1VP.copyable-text.selectable-text")
        reply.clear()
        reply.send_keys("Same to you! :)")
        reply.send_keys(Keys.RETURN)
    else :
        reply = driver.find_element_by_class_name("_2S1VP.copyable-text.selectable-text")
        reply.clear()
        reply.send_keys("Happy New Year! :)")
        reply.send_keys(Keys.RETURN)
