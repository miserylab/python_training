__author__ = 'miserylab'

from selenium import webdriver
from selenium.webdriver.common.by import By
from python_training.fixture.session import SessionHelper
from python_training.fixture.group import GroupHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
