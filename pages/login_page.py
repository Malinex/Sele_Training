



class Login_Page:

    def __init__(self, app):

        self.app = app

    wd = self.app.wd
    username_box = wd.find_element_by_id("username")