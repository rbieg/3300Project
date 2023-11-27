from django.test import TestCase
from django.contrib.auth.models import User
from .models import Appliance
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import keys

chromedriver_path = 'C:\\Users\\saber\\git\\3300Project\\website\\cooking\\chromedriver.exe'

class ApplianceModelTest(TestCase):
    def setUp(self):
        self.appliance = Appliance.objects.create(name="testAppliance", description="", heat_setting=Appliance.heat_setting_choices[0])
    def test_appliance_str(self):
        self.assertEqual(str(self.appliance.name), 'testAppliance')
    def test_appliance_heat_setting(self):
        self.assertEqual(self.appliance.heat_setting,('low', 'Low'))

class LoginFormTest(LiveServerTestCase):
    def testform(self):
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/accounts/login/')  

        username = driver.find_element_by_name('username')
        password = driver.find_element_by_name('password')
        submit = driver.find_element_by_id('submit')

        username.send_keys('rbieg')
        password.send_keys('adminpass')

        submit.send_keys(keys.RETURN)

        assert 'rbieg' in driver.page_source



