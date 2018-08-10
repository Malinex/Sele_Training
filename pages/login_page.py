



class Login_Page:
    wd = self.app.wd
    username_box = wd.find_element_by_id("username")


    def __init__(self, app):

        self.app = app

        username_box = wd.find_element_by_id("username")
    def objects(self):
        wd = self.app.wd
        username_box = wd.find_element_by_id("username")


    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        pages.login_page.username_box.click()
        username_box.clear()
        username_box.send_keys(username)
        password_box = wd.find_element_by_id("password")
        password_box.click()
        password_box.clear()
        password_box.send_keys(password)
        login_button = wd.find_element_by_class_name("button2")
        login_button.click()