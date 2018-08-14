import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import string
from random import *
from cfg_ATT import config


class forum_helper:

    def __init__(self, app):
        self.app = app



def create_new_topic(self, subject, message):
    wd = self.app.wd
    wd.find_element_by_xpath("//a[@class='button']").click()
    subject_box = wd.find_element_by_id("subject")
    subject_box.click()
    subject_box.clear()
    subject_box.send_keys(subject)
    message_box = wd.find_element_by_id("message")
    message_box.click()
    message_box.clear()
    message_box.send_keys(message)
    new_topic_button = wd.find_element_by_name("post")
    new_topic_button.click()