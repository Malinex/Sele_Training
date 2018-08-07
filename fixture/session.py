import time
from selenium.webdriver.support.ui import WebDriverWait
import json


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        usernameBox = wd.find_element_by_id("username")
        usernameBox.click()
        usernameBox.clear()
        usernameBox.send_keys(username)
        passwordBox = wd.find_element_by_id("password")
        passwordBox.click()
        passwordBox.clear()
        passwordBox.send_keys(password)
        wd.find_element_by_class_name("button2").click()

    def logout(self):
        wd = self.app.wd

    def get_logged_user_name(self):
        wd = self.app.wd
        return wd.find_element_by_id("username_logged_in").text

    def open_subforum_page(self, subforum_title):
        wd = self.app.wd
        subforums = wd.find_elements_by_class_name("forumtitle")
        for e in subforums:
            if e.text == subforum_title:
                e.click()
                # wait until element is visible / presence -> by_class_name("forum-title")
                break
        #

    def open_subforum_by_nav_bar(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Łukasz").click()

    def create_new_topic(self, subject, message):
        wd = self.app.wd
        wd.find_element_by_link_text("New Topic").click()
        # ("//*[@id='xxx']") "button xxx"  //a == tagname ("a")  find_element_xxx.find_element_by_xpath("//")
        subjectBox = wd.find_element_by_id("subject")
        subjectBox.click()
        subjectBox.clear()
        subjectBox.send_keys(subject)
        messageBox = wd.find_element_by_id("message")
        messageBox.click()
        messageBox.clear()
        messageBox.send_keys(message)
        wd.find_element_by_name("post").click()

    def go_to_outbox(self):
        wd = self.app.wd
        self.go_to_private_messages(wd)
        wd.find_element_by_partial_link_text("Outbox").click()

    def go_to_private_messages(self, wd):
        wd.find_element_by_partial_link_text("Private messages").click()

    def create_new_priv_message(self, recipient, subject, message):
        wd = self.app.wd
        self.go_to_private_messages(wd)
        wd.find_element_by_link_text("New PM").click()
        recipientBox = wd.find_element_by_id("username_list")
        recipientBox.click()
        recipientBox.clear()
        recipientBox.send_keys(recipient)
        pmSubjectBox = wd.find_element_by_id("subject")
        pmSubjectBox.click()
        pmSubjectBox.clear()
        pmSubjectBox.send_keys(subject)
        pmMessageBox = wd.find_element_by_id("message")
        pmMessageBox.click()
        pmMessageBox.clear()
        pmMessageBox.send_keys(message)
        #
        submitMessage = wd.find_element_by_name("post")
        time.sleep(2)
        submitMessage.click()
        time.sleep(2)

        submitMessage.click()

    def get_subforum_name(self):
        wd = self.app.wd
        return wd.find_element_by_class_name("forum-title").text


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

