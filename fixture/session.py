import time
import json
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import string
from random import *

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://attnauka.webd.pro/forum/")

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        username_box = wd.find_element_by_id("username")
        username_box.click()
        username_box.clear()
        username_box.send_keys(username)
        password_box = wd.find_element_by_id("password")
        password_box.click()
        password_box.clear()
        password_box.send_keys(password)
        login_button = wd.find_element_by_class_name("button2")
        login_button.click()

    def wait(self):
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)
        return wait

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_id("username_logged_in").click()
        wd.find_element_by_xpath("//*[@title='Logout']").click()

    def get_logged_user_name(self):
        wd = self.app.wd
        return wd.find_element_by_id("username_logged_in").text

    def open_subforum_page(self, subforum_title):
        wd = self.app.wd
        subforums = wd.find_elements_by_class_name("forumtitle")
        for e in subforums:
            if e.text == subforum_title:
                e.click()
                break

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

    def check_subject_in_list_of_topics(self, subject):
        wd = self.app.wd
        list_of_topics = wd.find_elements_by_class_name("topictitle")
        for e in list_of_topics:
            if e.text == subject:
                return True
            else:
                return False

    def go_to_private_messages(self, wd):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@id='nav-main']/li[4]/a/span").click()

    def go_to_outbox(self):
        wd = self.app.wd
        self.go_to_private_messages(self)
        private_messages_menu = wd.find_elements_by_tag_name("span")
        for e in private_messages_menu:
            if e.text == "Outbox":
                e.click()
                break

    def create_new_priv_message(self, recipient, subject, message):
        wd = self.app.wd
        self.go_to_private_messages(self)
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
        WebDriverWait(wd, 10)
        time.sleep(2)
        submit_message = wd.find_element_by_name("post")
        submit_message.click()

    def get_subforum_name(self):
        wd = self.app.wd
        return wd.find_element_by_class_name("forum-title").text

    def random_chars(self, min_chars, max_chars):
        wd = self.app.wd
        allchars = " " + string.ascii_letters + " " + string.punctuation + " " + string.digits + " "
        return "".join(choice(allchars) for x in range(randint(min_chars, max_chars)))

    """
    nazwaForum <- wejście
    sprawdz gdzie na liscie forów jest takie o tej nazwie <- elementy -> for icz
    kliknij w to forum <- elements.forEach {if(it.text.equals("forum")){ it.click()}}
    sprawdz czy wszedłeś w dobre forum <- NIE SPRAWDZAJ LINKÓW, 
    find_element a find_elements
    
    Board > Łukasz > dupa
    //blalbla/bla/bla[3]/bla <-
    
    webdriver jak głupi buc nie programistyczny indeksuje od 1
    języki programowania indeksuja od 0
    
    
    get_forum_title():
        return blablabla bla bla bla
        
        
    czwarty zad a.k.a. czwarta dupa:
    nie bierzemy logiki paginacji -> czyli ze temat bedzie na 2 stronie, zakładamy ze jest ich tak mało ze beda na 1 stronie (page)
    
    """

