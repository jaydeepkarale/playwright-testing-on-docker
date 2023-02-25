from playwright.sync_api import expect
from utilities.utilities import set_test_status
from pages.accountpage import AccountPage

def test_myaccount_page_contains_registration_link(browser, account_page):
    """
    Test to verify if new customer registration link exists on account page
    """
    account_page.navigate()
    account_page.new_registration()
    browser.close()   
    
    
def test_myaccount_page_contains_login_form_with_email_and_password(browser, account_page):
    """
    Test to verify if customer login form exists on account page and contains email and password fields
    """       
    account_page.navigate()   
    account_page.login_form()             
    browser.close()

def test_myaccount_page_contains_forgotten_password_link(browser, account_page):
    """
    Test to verify if forgotten password link exists on account login page
    """       
    account_page.navigate()   
    account_page.forgotten_password()             
    browser.close()

