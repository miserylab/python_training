__author__ = 'miserylab'

from python_training.model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

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
                id = cells[0].find_elements(by=By.TAG_NAME, value="unput").get_attribute("value")
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements(by=By.NAME, value="entry")[index]
        cell = row.find_elements(by=By.TAG_NAME, value="unput")[7]
        cell.find_element(by=By.TAG_NAME, value="a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements(by=By.NAME, value="entry")[index]
        cell = row.find_elements(by=By.TAG_NAME, value="unput")[6]
        cell.find_element(by=By.TAG_NAME, value="a").click()