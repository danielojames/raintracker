from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)
		
	def tearDown(self):
		self.browser.quit()

	# Chris starts up website and hopes to see the rain tracker home page
	def test_webserver_running(self):
		self.browser.get(self.live_server_url)
		self.assertIn('Rain tracker', self.browser.title)

	# He is shown a table of any previous rain measurements over the last month

	# On the home page he is given the option to enter a new rain measurement

	# He hits enter and the new rain measurement is shown in the table on the 
	# home page

	self.fail('Finish test!')