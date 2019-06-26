import random
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Instagram:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome("./chromedriver.exe")
        self.username = username
        self.password = password

    def signin(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        inputs = self.driver.find_elements_by_css_selector('form input')

        emailInput = inputs[0]
        passwordInput = inputs[1]
        emailInput.send_keys(self.username)

        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

        current_url = self.driver.current_url
        self.is_signin = current_url == "https://www.instagram.com/"

    def go_to_user(self, user):
        if not self.is_signin:
            print("User not signed in")
            return
        self.driver.get("https://www.instagram.com/" + user)

    def like_user_posts(self, user):
        self.go_to_user(user)
        links = set()
        for i in range(0, 7):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            links_holders = self.driver.find_elements_by_css_selector("a")
            newLinks = [link_holder.get_attribute("href") for link_holder in links_holders]
            newLinks = [link for link in newLinks if '.com/p/' in link]
            links.update(newLinks)

        for pic_href in links:
            self.driver.get(pic_href)
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))
                like_button = lambda: self.driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
                like_button().click()
                time.sleep(1)
            except Exception as e:
                print(e)
                time.sleep(2)

    ## Static functions
    @staticmethod
    def create_acc():
        # Still trying to figure out to create email and create new instagram account
        return
