__author__ = 'miserylab'

from python_training.model.contact import Contact


def test_add_contact(self):
    driver = self.driver
    driver.get("http://localhost/addressbook/")
    driver.find_element_by_name("user").clear()
    driver.find_element_by_name("user").send_keys("admin")
    driver.find_element_by_name("pass").click()
    driver.find_element_by_name("pass").clear()
    driver.find_element_by_name("pass").send_keys("secret")
    driver.find_element_by_xpath("//input[@value='Login']").click()
    driver.find_element_by_link_text("add new").click()
    driver.find_element_by_name("firstname").click()
    driver.find_element_by_name("firstname").clear()
    driver.find_element_by_name("firstname").send_keys("test")
    driver.find_element_by_name("middlename").click()
    driver.find_element_by_name("middlename").clear()
    driver.find_element_by_name("middlename").send_keys("test1")
    driver.find_element_by_name("lastname").click()
    driver.find_element_by_name("lastname").clear()
    driver.find_element_by_name("lastname").send_keys("test3")
    driver.find_element_by_name("nickname").click()
    driver.find_element_by_name("nickname").click()
    driver.find_element_by_name("nickname").clear()
    driver.find_element_by_name("nickname").send_keys("test4")
    driver.find_element_by_name("photo").click()
    driver.find_element_by_name("photo").clear()
    driver.find_element_by_name("photo").send_keys("C:\\fakepath\\20200226_141511924_iOS.heic")
    driver.find_element_by_name("title").click()
    driver.find_element_by_name("title").clear()
    driver.find_element_by_name("title").send_keys("test5")
    driver.find_element_by_name("company").click()
    driver.find_element_by_name("company").clear()
    driver.find_element_by_name("company").send_keys("test6")
    driver.find_element_by_name("address").click()
    driver.find_element_by_name("address").clear()
    driver.find_element_by_name("address").send_keys("test7")
    driver.find_element_by_name("home").click()
    driver.find_element_by_name("home").clear()
    driver.find_element_by_name("home").send_keys("43253534")
    driver.find_element_by_name("mobile").click()
    driver.find_element_by_name("mobile").clear()
    driver.find_element_by_name("mobile").send_keys("657575475")
    driver.find_element_by_name("work").click()
    driver.find_element_by_name("work").clear()
    driver.find_element_by_name("work").send_keys("423432432")
    driver.find_element_by_name("fax").click()
    driver.find_element_by_name("fax").clear()
    driver.find_element_by_name("fax").send_keys("56574745745")
    driver.find_element_by_name("email").click()
    driver.find_element_by_name("theform").click()
    driver.find_element_by_name("email").clear()
    driver.find_element_by_name("email").send_keys("test@test1.ru")
    driver.find_element_by_name("email2").click()
    driver.find_element_by_name("email2").click()
    driver.find_element_by_name("email2").clear()
    driver.find_element_by_name("email2").send_keys("test@test2.ru")
    driver.find_element_by_name("email3").click()
    driver.find_element_by_name("email3").click()
    driver.find_element_by_name("email3").click()
    driver.find_element_by_name("email3").clear()
    driver.find_element_by_name("email3").send_keys("test@test3.ru")
    driver.find_element_by_name("homepage").click()
    driver.find_element_by_name("theform").click()
    driver.find_element_by_name("homepage").clear()
    driver.find_element_by_name("homepage").send_keys("test1.ru")
    driver.find_element_by_name("bday").click()
    Select(driver.find_element_by_name("bday")).select_by_visible_text("4")
    driver.find_element_by_name("bmonth").click()
    Select(driver.find_element_by_name("bmonth")).select_by_visible_text("March")
    driver.find_element_by_name("byear").click()
    driver.find_element_by_name("byear").clear()
    driver.find_element_by_name("byear").send_keys("1987")
    driver.find_element_by_name("aday").click()
    Select(driver.find_element_by_name("aday")).select_by_visible_text("5")
    driver.find_element_by_name("amonth").click()
    Select(driver.find_element_by_name("amonth")).select_by_visible_text("July")
    driver.find_element_by_name("ayear").click()
    driver.find_element_by_name("ayear").clear()
    driver.find_element_by_name("ayear").send_keys("2020")
    driver.find_element_by_name("new_group").click()
    driver.find_element_by_name("theform").click()
    driver.find_element_by_name("address2").click()
    driver.find_element_by_name("address2").clear()
    driver.find_element_by_name("address2").send_keys("test8")
    driver.find_element_by_name("phone2").click()
    driver.find_element_by_name("phone2").clear()
    driver.find_element_by_name("phone2").send_keys("test9")
    driver.find_element_by_name("notes").click()
    driver.find_element_by_name("notes").clear()
    driver.find_element_by_name("notes").send_keys("test10")
    driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
    driver.find_element_by_link_text("Logout").click()
