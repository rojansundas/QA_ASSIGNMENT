from selenium import webdriver
from selenium.webdriver.common.by import By
from LOGINPAGE import LoginPage
from ADDTOCART import AddToCart
from HOMEPAGE import HomePage
import time



driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")


loginpage=LoginPage(driver)
loginpage.enter_username("standard_user")
loginpage.enter_password("secret_sauce")
loginpage.click_button()
time.sleep(3)



addtocart=AddToCart(driver)
addtocart.add_to_cart()
addtocart.click_cart()

homepage = HomePage(driver)
NumberOfBadge = homepage.count_badge()
ActualCount=int(NumberOfBadge)


assert ActualCount == 2, f"ExpeActed 2 items, but got {NumberOfBadge}"

print("Cart badge shows 2 items successfully.")

time.sleep(3)
driver.quit()