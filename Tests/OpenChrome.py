from selenium import webdriver
import unittest
import time


class OpenChrome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:/Users/munnam/PycharmProjects/KBK/chromedriver')
        self.driver.maximize_window()
        self.driver.implicitly_wait(90)
        self.base_url = "http://server.kbk/cosmos/501/login"

    def test(self):
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(20)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
