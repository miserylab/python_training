__author__ = 'miserylab'

from selenium import webdriver
from python_training.fixture.session import SessionHelper
from python_training.fixture.group import GroupHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def is_valid(self):
        try:
            # опрос у браузера какой текущий url у страницы. если url возвращается, то фикстура валидна
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
