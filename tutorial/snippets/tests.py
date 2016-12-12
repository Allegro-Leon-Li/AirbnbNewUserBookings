from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


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
        selenium.get('http://127.0.0.1:8000/logout')
        selenium.get('http://127.0.0.1:8000/register')
        time.sleep(3)
        #find the form element
        username = selenium.find_element_by_id('login-username')
        age = selenium.find_element_by_id('login-age')
        psw = selenium.find_element_by_id('login-password')
        gender = selenium.find_element_by_id('login-gender')
        email = selenium.find_element_by_id('login-email')
        language = selenium.find_element_by_id('login-language')

        submit = selenium.find_element_by_id('btn-sub')

        #Fill the form with data
        username.send_keys('testusertestdjango2')
        age.send_keys('10')
        psw.send_keys('password')
        gender.send_keys('MALE')
        email.send_keys('yusuf@qawba.com')
        language.send_keys('German')

        #submitting the form
        submit.send_keys(Keys.RETURN)
        time.sleep(3)
        #check the returned result
        assert '<li class="filter">' in selenium.page_source

    def test_wrong_email(self):
        selenium = self.selenium
        # Opening the link we want to test

        selenium.get('http://127.0.0.1:8000/logout')
        selenium.get('http://127.0.0.1:8000/register')
        time.sleep(3)
        # find the form element
        username = selenium.find_element_by_id('login-username')
        age = selenium.find_element_by_id('login-age')
        psw = selenium.find_element_by_id('login-password')
        gender = selenium.find_element_by_id('login-gender')
        email = selenium.find_element_by_id('login-email')
        language = selenium.find_element_by_id('login-language')

        submit = selenium.find_element_by_id('btn-sub')

        # Fill the form with data
        username.send_keys('Yusufia2')
        age.send_keys('10')
        psw.send_keys('password')
        gender.send_keys('MALE')
        email.send_keys('yusuf')
        language.send_keys('German')

        # submitting the form
        submit.send_keys(Keys.RETURN)
        time.sleep(3)
        # check the returned result
        assert '<form name="registrationForm"' in selenium.page_source


    def test_bland_psw(self):
        selenium = self.selenium
        # Opening the link we want to test

        selenium.get('http://127.0.0.1:8000/logout')
        selenium.get('http://127.0.0.1:8000/register')
        time.sleep(3)
        # find the form element
        username = selenium.find_element_by_id('login-username')
        age = selenium.find_element_by_id('login-age')
        psw = selenium.find_element_by_id('login-password')
        gender = selenium.find_element_by_id('login-gender')
        email = selenium.find_element_by_id('login-email')
        language = selenium.find_element_by_id('login-language')

        submit = selenium.find_element_by_id('btn-sub')

        # Fill the form with data
        username.send_keys('Yusufia2')
        age.send_keys('10')
        psw.send_keys('')
        gender.send_keys('MALE')
        email.send_keys('yusuf@mail.com')
        language.send_keys('German')

        # submitting the form
        submit.send_keys(Keys.RETURN)
        try:
            WebDriverWait(webdriver.Chrome(), 3).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')

            alert = webdriver.switch_to_alert()
            alert.accept()
            print
            "alert accepted"
        except TimeoutException:
            print
            "no alert"
        time.sleep(3)
        # check the returned result
        assert '<form name="registrationForm"' in selenium.page_source


    def test_invalid_age(self):
        selenium = self.selenium
        # Opening the link we want to test

        selenium.get('http://127.0.0.1:8000/logout')
        selenium.get('http://127.0.0.1:8000/register')
        time.sleep(3)
        # find the form element
        username = selenium.find_element_by_id('login-username')
        age = selenium.find_element_by_id('login-age')
        psw = selenium.find_element_by_id('login-password')
        gender = selenium.find_element_by_id('login-gender')
        email = selenium.find_element_by_id('login-email')
        language = selenium.find_element_by_id('login-language')

        submit = selenium.find_element_by_id('btn-sub')

        # Fill the form with data
        username.send_keys('Yusufia2')
        age.send_keys('10a')
        psw.send_keys('password')
        gender.send_keys('MALE')
        email.send_keys('yusuf@mail.com')
        language.send_keys('German')

        # submitting the form
        submit.send_keys(Keys.RETURN)
        try:
            WebDriverWait(webdriver.Chrome(), 3).until(EC.alert_is_present(),
                                            'Timed out waiting for PA creation ' +
                                            'confirmation popup to appear.')

            alert = webdriver.switch_to_alert()
            alert.accept()
            print
            "alert accepted"
        except TimeoutException:
            print
            "no alert"
        time.sleep(3)
        # check the returned result
        assert '<form name="registrationForm"' in selenium.page_source

    def test_login(self):
        selenium = self.selenium
        # Opening the link we want to test

        selenium.get('http://127.0.0.1:8000/logout')
        selenium.get('http://127.0.0.1:8000/sign')
        time.sleep(3)
        # find the form element
        username = selenium.find_element_by_id('id_username')
        psw = selenium.find_element_by_id('id_password')

        submit = selenium.find_element_by_id('btn-sub')

        # Fill the form with data
        username.send_keys('testusertestdjango')
        psw.send_keys('password')

        # submitting the form
        submit.send_keys(Keys.RETURN)
        time.sleep(3)
        # check the returned result
        assert '<li class="filter">' in selenium.page_source
