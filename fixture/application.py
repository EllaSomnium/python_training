from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def go_to_homepage(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def destroy(self):
        self.wd.quit()
