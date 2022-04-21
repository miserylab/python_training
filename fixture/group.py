__author__ = 'miserylab'

from selenium.webdriver.common.by import By
from python_training.model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        # для test_del_group добавлена проверка на случай, когда нет записей для удаления и мы добавляем её через
        # сreate. Чтобы два раза не было перехода на страницу с группами. Если на странице с url, оканчивающимся на
        # /group.php есть кнопка "New group" и пр.
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements(by=By.NAME, value="new")) > 0):
            wd.find_element(by=By.LINK_TEXT, value="groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element(by=By.NAME, value="new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element(by=By.NAME, value="submit").click()
        self.return_to_groups_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(by=By.NAME, value=field_name).click()
            wd.find_element(by=By.NAME, value=field_name).clear()
            wd.find_element(by=By.NAME, value=field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # submit_deletion
        wd.find_element(by=By.NAME, value="delete").click()
        self.return_to_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element(by=By.NAME, value="selected[]").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # open modification form
        wd.find_element(by=By.NAME, value="edit").click()
        # fill group from
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element(by=By.NAME, value="update").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element(by=By.LINK_TEXT, value="group page").click()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements(by=By.NAME, value="selected[]"))

    def get_group_list(self):
        wd = self.app.wd
        self.open_groups_page()
        groups = []
        for element in wd.find_elements(by=By.CSS_SELECTOR, value="span.group"):
            text = element.text
            id = element.find_element(by=By.NAME, value="selected[]").get_attribute("value")
            groups.append(Group(name=text, id=id))
        return groups

