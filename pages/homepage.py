from playwright.sync_api import expect
from utilities.utilities import set_test_status


class HomePage:   
    
    def __init__(self, page):
        self.page = page
        self.search_button_locator = page.get_by_role(role="button", name="Search")
        self.myaccount_link_locator = page.get_by_role(role="link", name="My Account")
    
    def navigate(self):
        self.page.goto("https://ecommerce-playground.lambdatest.io/")
    
    def search_button(self):                
        try:
            expect(self.search_button_locator).to_be_visible()
            set_test_status(self.page, "Passed", "Search button is visible")
        except Exception as ex:
            set_test_status(self.page, "Failed", "Search button is not visible")
    
    def myaccount_link(self):        
        try:
            expect(self.myaccount_link_locator).to_have_attribute("href", "https://ecommerce-playground.lambdatest.io/index.php?route=account/account")
            set_test_status(self.page, "Passed", "My account link is visible")
        except Exception as ex:
            set_test_status(self.page, "Failed", "My account link is not visible")                    
                    
            

                

        