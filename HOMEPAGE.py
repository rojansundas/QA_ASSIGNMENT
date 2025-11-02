from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class HomePage:
    def __init__(self,driver):
        self.driver=driver
        self.cart_badge=(By.XPATH,"//span[@class='shopping_cart_badge']")
        pass
    def count_badge(self):
        try:
            badge = self.driver.find_element(*self.cart_badge)
            return badge.text
        except NoSuchElementException:
            return 0