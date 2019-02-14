from appium.webdriver.common.mobileby import By
from appium.webdriver.common.mobileby import MobileBy

class HomePageLocators(object):
    MENU = (MobileBy.ID, 'com.ebay.mobile:id/home')
    SEARCH = (MobileBy.ID, 'com.ebay.mobile:id/search_box')
    SEARCH_TEXT = (MobileBy.ID, 'com.ebay.mobile:id/search_src_text')

class SettingsPageLocators(object):
    SETTINGS = (MobileBy.ID, 'com.ebay.mobile:id/design_menu_item_text')
    COUNTRY = (MobileBy.ACCESSIBILITY_ID, 'Country/region button')
    AUTO_DETECT = (MobileBy.ID, 'android:id/switchWidget')
    SELECT_COUNTRY = (MobileBy.ID, 'android:id/title')
    SEARCH_COUNTRY = (MobileBy.ID, 'com.ebay.mobile:id/filter')
    SELECT_PARTICULAR_COUNTRY = (MobileBy.ID, 'com.ebay.mobile:id/check_country')

class ProductPageLocators(object):
    SELECT_PRODUCT = (MobileBy.ID, 'com.ebay.mobile:id/cell_collection_item')
    PRODUCT_NAME = (MobileBy.ID, 'com.ebay.mobile:id/textview_item_name')
    PRODUCT_PRICE = (MobileBy.ID, 'com.ebay.mobile:id/textview_item_price')
    ADD_TO_CART = (MobileBy.ID, 'com.ebay.mobile:id/button_add_to_cart')
    CHECK_OUT = (MobileBy.ID, 'com.ebay.mobile:id/action_view_icon')
class LoginPageLocators(object):
    LOGIN_USERNAME = (MobileBy.ID, 'com.ebay.mobile:id/edit_text_username')
    LOGIN_PASSWORD = (MobileBy.ID, 'com.ebay.mobile:id/edit_text_password')
    SIGN_IN = (MobileBy.ID, 'com.ebay.mobile:id/button_sign_in')
    DENY = (MobileBy.ID, 'com.ebay.mobile:id/button_google_deny')
class CheckOutPage(object):
    CHECK_OUT_ITEM = (MobileBy.ID, 'com.ebay.mobile:id/item_details')
