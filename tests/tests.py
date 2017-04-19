from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time
# import re


class TestTodoApp(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(self):
        super(TestTodoApp, self).setUpClass()
        self.display = Display(visible=1, size=(1024, 768))
        self.display.start()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = self.live_server_url
        self.verificationErrors = []
        self.accept_next_alert = True
        self.task_title = "Заказать пиццу"

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        self.display.stop()
        super(TestTodoApp, self).tearDownClass()

    def Test_create_task(self):
        driver = self.driver
        driver.get(self.base_url + "/tasks/add/")
        driver.find_element_by_id("id_title").clear()
        driver.find_element_by_id("id_title").send_keys(self.task_title)
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        self.task_id = driver.find_element_by_link_text(self.task_title).get_attribute('id')
        driver.find_element_by_css_selector("tr[name='{}'] a[name='view-task']".format(self.task_id)).click()

    def Test_delete_task(self):
        driver = self.driver
        driver.get(self.base_url + "/tasks/")
        driver.find_element_by_css_selector("tr[name='{}'] a[name='delete-task']".format(self.task_id)).click()
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
        driver.get(self.base_url + "/tasks/")
        if driver.find_element_by_css_selector("tr[name='{}'] a[name='delete-task']".format(self.task_id)):
            raise ValueError('Cannot delete task with id:{}'.format(self.task_id))

    def test_create_then_delete(self):
        self.Test_create_task()
        self.Test_delete_task()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True
