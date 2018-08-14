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

    def open_subforum_page(self, subforum_title):
        wd = self.app.wd
        subforums = wd.find_elements_by_class_name("forumtitle")
        for e in subforums:
            if e.text == subforum_title:
                e.click()
                break

    def check_subject_in_list_of_topics(self, subject):
        wd = self.app.wd
        list_of_topics = wd.find_elements_by_class_name("topictitle")
        for e in list_of_topics:
            if e.text == subject:
                return True

    def get_subforum_name(self):
        wd = self.app.wd
        return wd.find_element_by_class_name("forum-title").text

    def return_to_topics_list(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("a.left-box.arrow-left").click()