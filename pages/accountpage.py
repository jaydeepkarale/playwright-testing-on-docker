from playwright.sync_api import expect
from utilities.utilities import set_test_status


class AccountPage:
    
    def __init__(self, page):
        self.page = page
        self.new_registration_link_locator =  page.get_by_role(role="link", name="Continue")
        self.email_field_locator = page.get_by_placeholder("E-Mail Address")
        self.password_field_locator =  page.get_by_placeholder("Password")
        self.forgotten_password_link_locator = page.get_by_role(role="link", name="Forgotten Password", exact=True)
    
    def navigate(self):
        self.page.goto("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")
    
    def new_registration(self):                
        try:
             expect(self.new_registration_link_locator).to_have_attribute("href", "https://ecommerce-playground.lambdatest.io/index.php?route=account/register")
             set_test_status(self.page, "Passed", "Registration link is visible")
        except Exception as ex:
            set_test_status(self.page, "Failed", "Registration link is not visible")
    
    def login_form(self):                
        try:
            expect(self.email_field_locator).to_be_visible()
            expect(self.password_field_locator).to_be_visible()
            set_test_status(self.page, "Passed", "Login form contains email & password fields")
        except Exception as ex:
            set_test_status(self.page, "Failed", "Login form does not contains email & password fields") 


    def forgotten_password(self):                
        try:
            expect(self.forgotten_password_link_locator).to_have_attribute("href","https://ecommerce-playground.lambdatest.io/index.php?route=account/forgotten")    
            set_test_status(self.page, "Passed", "Forgotten Password link is visible")
        except Exception as ex:
            set_test_status(self.page, "Passed", "Forgotten Password link is not visible")
                    
            

                

        