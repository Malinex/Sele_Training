from fixture.session import SessionHelper
from selenium import webdriver
from cfg_ATT import config

class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get(config.base_url)

    def destroy(self):
        self.wd.quit()

