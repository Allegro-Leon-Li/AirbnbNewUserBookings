from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome()
        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/login')
        time.sleep(3)
        #find the form element
        username = selenium.find_element_by_id('login-username')
        age = selenium.find_element_by_id('login-age')
        gender = selenium.find_element_by_id('login-gender')
        email = selenium.find_element_by_id('login-email')
        language = selenium.find_element_by_id('login-language')

        submit = selenium.find_element_by_id('btn-sub')

        #Fill the form with data
        username.send_keys('Yusufia')
        age.send_keys('10')
        gender.send_keys('MALE')
        email.send_keys('yusuf@qawba.com')
        language.send_keys('German')

        #submitting the form
        submit.send_keys(Keys.RETURN)
        time.sleep(3)
        #check the returned result
        assert '<li class="filter">' in selenium.page_source