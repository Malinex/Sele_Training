from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://forum.attnauka.webd.pro/")
login = driver.find_element_by_id("username")
login.clear()
login.send_keys("lmalinowski")
ps = driver.find_element_by_id("password")
ps.send_keys("malin1")
driver.find_element_by_xpath("//input[@class='button2']").click()
assert driver.find_element_by_id("username_logged_in").text == "lmalinowski"