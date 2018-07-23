from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://forum.attnauka.webd.pro/")
login = driver.find_element_by_id("username")
login.clear()
a = open("att.cfg","r")
login.send_keys(a.read())
ps = driver.find_element_by_id("password")
b = open("att2.cfg","r")
ps.send_keys(b.read())
driver.find_element_by_xpath("//input[@class='button2']").click()
assert driver.find_element_by_xpath("//*[@id='username_logged_in']/div/a/span").text == "lmalinowski"