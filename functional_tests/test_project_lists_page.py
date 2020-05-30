# from selenium import webdriver
# #from budget.models import Project
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from django.urls import reverse
# import time
# from . import *



# class TestProjectListPage(StaticLiveServerTestCase):

# 	def setUp(self):
# 		self.browser = webdriver.Chrome('functional_tests/chromedriver')
# 		self.browser.maximize_window()

# 		#self.browser.get("http://127.0.0.1:8000/")
	
# 	def tearDown(self):
# 		self.browser.close()


# 	def test_program(self):
# 		time.sleep(3)
# 		self.browser.get(self.live_server_url)
# 		time.sleep(5)
# 		self.browser.find_element_by_id('testAlgo').click()
# 		time.sleep(5)
# 		self.browser.find_element_by_id('insertBt').click()
# 		time.sleep(5)
# 		self.browser.find_element_by_id('closebtn').click()
# 		time.sleep(3)
# 		self.browser.find_element_by_id('rBtn').click()
# 		time.sleep(2)
# 		self.browser.find_element_by_id('fname').send_keys('vidhaan')
# 		time.sleep(1)
# 		self.browser.find_element_by_id('lname').send_keys('mishra')
# 		time.sleep(1)
# 		self.browser.find_element_by_id('mail').send_keys('abc@def.com')
# 		time.sleep(1)
# 		self.browser.find_element_by_id('usrName').send_keys('vidhaan')
# 		time.sleep(1)
# 		self.browser.find_element_by_id('pswd').send_keys('123')
# 		time.sleep(1)
# 		self.browser.find_element_by_id('pswd1').send_keys('123')
# 		time.sleep(1)
# 		self.browser.find_element_by_id('regBtn').click()
# 		time.sleep(2)
# 		self.browser.find_element_by_id('usrName').send_keys('vidhaan')
# 		time.sleep(2)
# 		self.browser.find_element_by_id('pswd').send_keys('123')
# 		time.sleep(2)
# 		self.browser.find_element_by_id('btnLogin').click()
# 		time.sleep(5)
# 		self.browser.find_element_by_id('testAlgo').click()
# 		time.sleep(4)
# 		self.browser.find_element_by_id('sortAlgo').click()
# 		time.sleep(5)
# 		self.browser.find_element_by_id('btInser').click()
# 		time.sleep(10)
# 		self.browser.find_element_by_id('btReset').click()
# 		time.sleep(5)
# 		self.browser.find_element_by_id('btHeap').click()
# 		time.sleep(10)
# 		self.browser.find_element_by_id('close1btn').click()
# 		time.sleep(3)
# 		self.browser.execute_script("window.scrollTo(5000, 5001)")
# 		time.sleep(5)
# 		self.browser.find_element_by_id('gitHub').click()
# 		time.sleep(6)
# 		self.browser.back()
# 		time.sleep(5)
# 		self.browser.execute_script("window.scrollTo(0, 0)")
# 		time.sleep(5)
# 		self.browser.find_element_by_id('btnOut').click()
# 		time.sleep(10)


