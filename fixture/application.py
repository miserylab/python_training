__author__ = 'miserylab'

from selenium import webdriver
from selenium.webdriver.common.by import By


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)

    def logout(self):
        wd = self.wd
        wd.find_element(by=By.LINK_TEXT, value="Logout").click()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element(by=By.LINK_TEXT, value="group page").click()

    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        # init group creation
        wd.find_element(by=By.NAME, value="new").click()
        # fill group form
        wd.find_element(by=By.NAME, value="group_name").click()
        wd.find_element(by=By.NAME, value="group_name").clear()
        wd.find_element(by=By.NAME, value="group_name").send_keys(group.name)
        wd.find_element(by=By.NAME, value="group_header").click()
        wd.find_element(by=By.NAME, value="group_header").clear()
        wd.find_element(by=By.NAME, value="group_header").send_keys(group.header)
        wd.find_element(by=By.NAME, value="group_footer").click()
        wd.find_element(by=By.NAME, value="group_footer").clear()
        wd.find_element(by=By.NAME, value="group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element(by=By.NAME, value="submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element(by=By.LINK_TEXT, value="groups").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element(by=By.NAME, value="user").clear()
        wd.find_element(by=By.NAME, value="user").send_keys(username)
        wd.find_element(by=By.ID, value="LoginForm").click()
        wd.find_element(by=By.NAME, value="pass").click()
        wd.find_element(by=By.NAME, value="pass").clear()
        wd.find_element(by=By.NAME, value="pass").send_keys(password)
        wd.find_element(by=By.XPATH, value="//input[@value='Login']").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
