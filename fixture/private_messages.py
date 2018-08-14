import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import string
from random import *
from cfg_ATT import config


class private_messages_helper:

    def __init__(self, app):
        self.app = app

    def go_to_private_messages(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@id='nav-main']/li[4]/a/span").click()

    def check_if_user_in_private_masseges(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//*[@id='tabs']/ul/li[4]/a").text == "Private messages"

    def go_to_outbox_by_private_messages(self):
        wd = self.app.wd
        wait = WebDriverWait(wd, 5)
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "span")))
        private_messages_menu = wd.find_elements_by_tag_name("span")
        for e in private_messages_menu:
            if e.text[0:6] == 'Outbox':
                e.click()
                break

    def go_to_outbox_after_sending_a_message(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(text(),'Return to your “Outbox” folder')]").click()

    def create_new_priv_message(self, recipient, subject, message):
        wd = self.app.wd
        self.go_to_private_messages()
        wd.find_element_by_xpath("//a[@class='button']").click()
        recipient_box = wd.find_element_by_id("username_list")
        recipient_box.click()
        recipient_box.clear()
        recipient_box.send_keys(recipient)
        add_ecipient_button = wd.find_element_by_name("add_to")
        add_ecipient_button.click()
        pm_subject_box = wd.find_element_by_id("subject")
        pm_subject_box.click()
        pm_subject_box.clear()
        pm_subject_box.send_keys(subject)
        pm_message_box = wd.find_element_by_id("message")
        pm_message_box.click()
        pm_message_box.clear()
        pm_message_box.send_keys(message)
        submit_message = WebDriverWait(wd, 50).until(EC.presence_of_element_located((By.NAME, "post")))
        submit_message.click()

    def check_message_in_outbox(self, subject):
        wd = self.app.wd
        messages_in_outbox = wd.find_elements_by_class_name("topictitle")
        for e in messages_in_outbox:
            if e.text == subject:
                return True