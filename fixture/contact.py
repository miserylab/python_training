__author__ = 'miserylab'

from python_training.model.contact import Contact
from selenium.webdriver.common.by import By
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

    # def open_contact_page(self):
    #     wd = self.app.wd
    #     if not (wd.current_url.endswith("/group.php") and len(wd.find_elements(by=By.NAME, value="new")) > 0):
    #         wd.find_element(by=By.LINK_TEXT, value="groups").click()

    # def create(self, group):
    #     wd = self.app.wd
    #     self.open_contact_page()
    #     # init group creation
    #     wd.find_element(by=By.NAME, value="new").click()
    #     self.fill_contact_form(group)
    #     # submit group creation
    #     wd.find_element(by=By.NAME, value="submit").click()
    #     self.return_to_groups_page()
    #     # сброс кэша
    #     self.group_cache = None

    # def fill_contact_form(self, contact):
    #     wd = self.app.wd
    #     self.change_field_value("firstname", contact.firstname)
    #     self.change_field_value("lastname", contact.lastname)
    #     self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(by=By.NAME, value=field_name).click()
            wd.find_element(by=By.NAME, value=field_name).clear()
            wd.find_element(by=By.NAME, value=field_name).send_keys(text)

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements(by=By.NAME, value="entry"):
                cells = row.find_elements(by=By.TAG_NAME, value="td")
                firstname = cells[1].text
                lastname = cells[2].text
                id = cells[0].find_element(by=By.TAG_NAME, value="input").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements(by=By.NAME, value="entry")[index]
        cell = row.find_elements(by=By.TAG_NAME, value="td")[7]
        cell.find_element(by=By.TAG_NAME, value="a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements(by=By.NAME, value="entry")[index]
        cell = row.find_elements(by=By.TAG_NAME, value="td")[6]
        cell.find_element(by=By.TAG_NAME, value="a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element(by=By.NAME, value="firstname").get_attribute("value")
        lastname = wd.find_element(by=By.NAME, value="lastname").get_attribute("value")
        id = wd.find_element(by=By.NAME, value="id").get_attribute("value")
        homephone = wd.find_element(by=By.NAME, value="home").get_attribute("value")
        workphone = wd.find_element(by=By.NAME, value="work").get_attribute("value")
        mobilephone = wd.find_element(by=By.NAME, value="mobile").get_attribute("value")
        secondaryphone = wd.find_element(by=By.NAME, value="phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(by=By.ID, value="content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone)
