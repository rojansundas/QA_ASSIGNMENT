from selenium import webdriver
from selenium.webdriver.common.by import By

class AddToCart:
    def __init__(self, driver):
        self.driver=driver
        self.item1=(By.ID,"add-to-cart-sauce-labs-backpack")
        self.item2=(By.ID,"add-to-cart-sauce-labs-bike-light")
        self.cart=(By.CLASS_NAME,"shopping_cart_link")
    def add_to_cart(self):
        self.driver.find_element(*self.item1).click()
        self.driver.find_element(*self.item2).click()
    def click_cart(self):
        self.driver.find_element(*self.cart).click()