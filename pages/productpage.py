from playwright.sync_api import expect
from utilities.utilities import set_test_status
import re


class ProductPage:
    
    def __init__(self, page):
        self.page = page
        self.addtocart_button_locator = page.get_by_role(role="button", name=re.compile("add to cart", re.IGNORECASE))
        self.buynow_button_locator = page.get_by_role(role="button", name=re.compile("buy now", re.IGNORECASE))        
    
    def navigate(self):
        self.page.goto("https://ecommerce-playground.lambdatest.io/index.php?route=product/product&path=34&product_id=28")
    
    def add_to_cart(self):                
        try:
            expect(self.addtocart_button_locator).to_be_visible()
            set_test_status(self.page, "Passed", "Add To Cart button is visible")
        except Exception as ex:
            set_test_status(self.page, "Failed", "Add To Cart button is not visible")
    
    def buy_now(self):                
        try:
            expect(self.buynow_button_locator).to_be_visible()
            set_test_status(self.page, "Passed", "Buy Now button is visible")
        except Exception as ex:
            set_test_status(self.page, "Failed", "Buy Now button is visible")


    def checkout_product(self):                
        try:            
            # Add a product to cart first & click checkout
            self.page.goto("https://ecommerce-playground.lambdatest.io/")
            self.page.get_by_role("button", name="Shop by Category").click()
            self.page.get_by_role("link", name="MP3 Players").click()
            self.page.get_by_role("link", name="HTC Touch HD HTC Touch HD HTC Touch HD HTC Touch HD").click()
            self.page.get_by_role("button", name="Add to Cart").click()
            self.page.get_by_role("link", name="Checkout ").click()
            
            # Perform the test on the checkout
            coupon_code_locator = self.page.get_by_placeholder("Enter your coupon here")
            expect(coupon_code_locator).to_be_visible()
            set_test_status(self.page, "Passed", "Use Coupon Code option is visible")
        except Exception as ex:
            set_test_status(self.page, "Failed", "Use Coupon Code option is visible")                       
