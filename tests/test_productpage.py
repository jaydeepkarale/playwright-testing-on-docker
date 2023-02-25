from playwright.sync_api import expect
from utilities.utilities import set_test_status
from pages.productpage import ProductPage

def test_product_page_contains_addtocart_button(browser, product_page):
    """
    Test to verify if product page has `add to cart` button
    """    
    product_page.navigate()
    product_page.add_to_cart()
    browser.close()   
    
    
def test_product_page_contains_buynow_button(browser, product_page):
    """
    Test to verify if product page has `buy now` button
    """     
    product_page.navigate()   
    product_page.buy_now()             
    browser.close()

def test_checkout_page_contains_use_couponcode_option(browser, product_page):
    """
    Test to verify if product page has `use coupon code` option is available on checkout page
    """    
    product_page.checkout_product()             
    browser.close()

