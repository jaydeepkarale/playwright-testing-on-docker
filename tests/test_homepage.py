from playwright.sync_api import expect
from utilities.utilities import set_test_status
from pages.homepage import HomePage

def test_homepage_contains_search_button(browser, home_page):
    """
    Test to verify if search button exists on the home page
    """    
    home_page.navigate()
    home_page.search_button()
    browser.close()   
    
    
def test_homepage_contains_myaccount_link(browser, home_page):
    """
    Test to verify if my account link exists on the home page
    """        
    home_page.navigate()   
    home_page.myaccount_link()             
    browser.close()

