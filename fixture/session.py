




class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_id("username").click()
        wd.find_element_by_id("username").clear()
        wd.find_element_by_id("username").send_keys(username)
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys(password)
        wd.find_element_by_xpath("//input[@class='button2']").click()

    def logout(self):
        wd = self.app.wd

    def create_new_topic(self):
        pass

    def open_subforum_page(self):
        wd = self.app.wd
        wd.get("http://www.attnauka.webd.pro/forum/viewforum.php?f=4&sid=65b6408fb2f044eedeaf59640e41c9ee")