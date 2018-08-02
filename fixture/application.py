from selenium import webdriver
from fixture.session import SessionHelper

class Application:

    def __init__(self):
        self.wd = webdriver()
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://attnauka.webd.pro/forum/")

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

