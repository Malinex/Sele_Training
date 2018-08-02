




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

    def create_new_topic(self):
        pass

    def open_subforum_page(self):
        wd = self.app.wd


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

    def get_logged_user_name(self):
        wd = self.app.wd
        return wd.find_element_by_id("username_logged_in").text