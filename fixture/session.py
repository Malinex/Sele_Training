import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import string
from random import *

from cfg_ATT import config


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get(config.base_url)

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

