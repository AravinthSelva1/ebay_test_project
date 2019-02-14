import os
import unittest
import HtmlTestRunner
import logging
import subprocess
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from locators import *
from time import sleep

class ebayAndroidTests(unittest.TestCase):
    #starting adb logs
    subprocess.call("adb logcat > logs.txt &",shell=True)
    #logging error
    logging.basicConfig(filename='app.log', format='%(asctime)s - %(message)s', level=logging.INFO)
    @classmethod
    def setUpClass(self):
        #SETTING UP AN AUTOMATION SESSION
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = 'Android'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['appPackage'] = 'com.ebay.mobile'
        desired_caps['appActivity'] = 'com.ebay.mobile.activities.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    @classmethod
    def tearDownClass(self):
        #TEARING DOWN AN SESSION
        self.driver.quit()

    def test_1_prerequisite(self):
        try:
            sleep(2)
            #CICKING ON MENU ICON
            self.driver.find_element(*HomePageLocators.MENU).click()
            sleep(3)
            #SCROLL TO SETTINGS IN MENU
            self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("Settings").instance(0));')
            sleep(3)
            #CLICK ON SETTINGS
            element=self.driver.find_elements(*SettingsPageLocators.SETTINGS)
            element[10].click()
            sleep(3)
            #CLICK ON COUNTRY
            self.driver.find_element(*SettingsPageLocators.COUNTRY).click()
            sleep(3)
            #TURN OFF AUTO DETECT LOCATION
            self.driver.find_element(*SettingsPageLocators.AUTO_DETECT).click()
            sleep(3)
            #TAP ON COUNTRY/REGION
            element=self.driver.find_elements(*SettingsPageLocators.SELECT_COUNTRY)
            element[1].click()
            sleep(3)
            #SEARCH FOR AUSTRALIA
            self.driver.find_element(*SettingsPageLocators.SEARCH_COUNTRY).send_keys("australia")
            sleep(3)
            #SELECT AUSTRALIA
            element=self.driver.find_elements(*SettingsPageLocators.SELECT_PARTICULAR_COUNTRY)
            element[0].click()
            sleep(3)
            #BACK TO COUNTRY/REGION
            self.driver.back()
            sleep(3)
            #BACK TO HOMEPAGE
            self.driver.back()
            sleep(3)
            logging.info("Location changed")
        except:
            logging.info("coding error")

    def test_2_login_and_search_products(self):
        try:
            self.driver.find_element(*HomePageLocators.SEARCH).click()
            sleep(3)
            #SEARCH FOR AN PRODUCT
            self.driver.find_element(*HomePageLocators.SEARCH_TEXT).send_keys("65-inch TV")
            sleep(3)
            #CLICK GO
            self.driver.press_keycode(66)
            sleep(20)
            #CLICK ON THE PRODUCT
            element=self.driver.find_elements(*ProductPageLocators.SELECT_PRODUCT)
            element[1].click()
            sleep(20)
            #GET THE NAME OF THE PRODUCT
            product_name=self.driver.find_element(*ProductPageLocators.PRODUCT_NAME).get_attribute("text")
            sleep(3)
            #GET THE PRICE OF THE PRODUCT
            product_price=self.driver.find_element(*ProductPageLocators.PRODUCT_PRICE).get_attribute("text")
            sleep(3)
            #SCROLL TO ADD TO CART
            self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().resourceIdMatches("com.ebay.mobile:id/button_add_to_cart").instance(0));')
            sleep(3)
            #CLICK ON ADD TO CART
            self.driver.find_element(*ProductPageLocators.ADD_TO_CART).click()
            sleep(3)
            #ENTER LOGIN USERNAME
            self.driver.find_element(*LoginPageLocators.LOGIN_USERNAME).send_keys("aravinth.selva3@gmail.com")
            sleep(3)
            #ENTER LOGIN PASSWORD
            self.driver.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys("test@123")
            sleep(3)
            #CLICK ON SIGN IN
            self.driver.find_element(*LoginPageLocators.SIGN_IN).click()
            sleep(20)
            #CLICK ON DENY
            self.driver.find_element(*LoginPageLocators.DENY).click()
            sleep(3)
            #CHECKOUT THE PRODUCT
            self.driver.find_element(*ProductPageLocators.CHECK_OUT).click()
            sleep(3)
            #CLICK ON ITEM
            self.driver.find_element(*CheckOutPage.CHECK_OUT_ITEM).click()
            sleep(3)
            #VERIFY THE ITEM DETAILS WITH PRODUCT PAGE
            #GET THE NAME OF THE PRODUCT
            product_name_checkout=self.driver.find_element(*ProductPageLocators.PRODUCT_NAME).get_attribute("text")
            sleep(3)
            #GET THE PRICE OF THE PRODUCT
            product_price_checkout=self.driver.find_element(*ProductPageLocators.PRODUCT_PRICE).get_attribute("text")
            sleep(3)
            assert product_name == product_name_checkout, "product name doesn't match"
            assert product_price == product_price_checkout, "product price doesn't match"
            logging.info("product info matches")
        except AssertionError:
            logging.error("product info doesn't match")
            raise Exception("product info doesn't match")
        except:
            logging.info("Coding error")


if __name__ == '__main__':
    html_report_dir = './html_report' 
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=html_report_dir))
