from fixture.session import SessionHelper
from selenium import webdriver
class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://attnauka.webd.pro/forum/")

    def destroy(self):
        self.wd.quit()