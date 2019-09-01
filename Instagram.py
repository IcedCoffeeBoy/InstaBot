import random
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from CSVwriter import CSVwriter


class Instagram:
    def __init__(self, username, password, headless=False):
        if headless:
            options = Options()
            options.add_argument('--headless')
            self.driver = webdriver.Chrome("./chromedriver.exe", chrome_options=options)
        else:
            self.driver = webdriver.Chrome("./chromedriver.exe")

        self.username = username
        self.password = password

    def signin(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        time.sleep(2)

        inputs = self.driver.find_elements_by_css_selector('form input')

        emailInput = inputs[0]
        passwordInput = inputs[1]
        emailInput.send_keys(self.username)

        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

        current_url = self.driver.current_url
        self.is_signin = self.checkUrl(current_url)
        if not self.is_signin:
            print("user not signed in")
        else:
            print("Log in success!")

    def go_tag_posts(self, tag):
        if not self.is_signin:
            print("User not signed in")
            return
        self.driver.get("https://www.instagram.com/explore/tags/" + tag)

    def like_tag_posts(self, tag):
        self.go_tag_posts(tag)
        links = set()
        likes = 0

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
                print("liked " + pic_href)
                time.sleep(1)
                likes += 1
            except Exception as e:
                print(e)
                time.sleep(2)

        print("Total number of likes: %i" % likes)
        return

    def go_to_user(self, user):
        if not self.is_signin:
            print("User not signed in")
            return
        self.driver.get("https://www.instagram.com/" + user)

    def like_user_posts(self, user):
        self.go_to_user(user)
        links = set()
        likes = 0

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
                print("Liked")
                time.sleep(1 + pic_href)
                likes += 1
            except Exception as e:
                print(e)
                time.sleep(2)

        print("Total number of likes: %i" % likes)
        return

    def get_user_post(self, user):
        self.go_to_user(user)
        links = set()
        csvwriter = CSVwriter("posts_{}.csv".format(user))

        for i in range(0, 1):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            links_holders = self.driver.find_elements_by_css_selector("a")
            newLinks = [link_holder.get_attribute("href") for link_holder in links_holders]
            newLinks = [link for link in newLinks if '.com/p/' in link]
            links.update(newLinks)

        # for link in links:
        #     self.driver.get(link)
        #     time.sleep(1)
        #     input("Paused")
        link = list(links)[0]
        self.driver.get(link)
        time.sleep(1)
        spans = self.driver.find_elements_by_css_selector("span")
        texts = [span.text for span in spans]
        print(texts)
        csvwriter.many_insert(texts)

    def close_driver(self):
        self.driver.close()

    def checkUrl(self, string):
        items = string.split('.com')
        print(items)
        if (len(items) == 1):
            return True
        if (items[1] == '/'):
            return True
        return False

    ## Static functions
    @staticmethod
    def create_acc():
        # Still trying to figure out to create email and create new instagram account
        return
