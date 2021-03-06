__author__ = 'miserylab'

from selenium import webdriver
from python_training.fixture.session import SessionHelper
from python_training.fixture.group import GroupHelper
from python_training.fixture.contact import ContactHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        # добавление ожиданий актуально для страницы, которая обновляется динамически. т.е. страница уже загрузилась,
        # а элементы на ней всё ещё не появились (они подгружаются чуть позже)
        # self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

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
