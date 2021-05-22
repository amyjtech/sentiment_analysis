# Importing packages
from selenium import webdriver
# This allows you to interact with webpage, type/enter text, etc.
from selenium.webdriver.common.keys import Keys
# Needed for using Chrome profile
from selenium.webdriver.chrome.options import Options

# from bs4 import BeautifulSoup
# from instascrape import Profile, scrape_posts
# !! Only grabbing 2 packages to increase load time while testing functionality
# Need to read posts, comments, hashtags

class WebScrape():
    '''
    This is the parent class for the webscraping application
    This holds all functionality for webscraping
    '''
    def __init__(self):
        pass
        
    # Setting up how we want Chrome to run
    def start():
        try:
            options = webdriver.ChromeOptions()
            options.add_argument("user-data-dir=C:\\Users\\AmySmith\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")
            # This prevents the browser from closing immediately after running
            options.add_experimental_option("detach", True)
            # Variable = path to the chromedriver
            PATH = "C:\Program Files (x86)\chromedriver.exe"
            # The driver is what navigates the page, I chose Chrome
            driver = webdriver.Chrome(PATH, options=options)

            # driver.get("webpage") will bring up any page you need
            driver.get("https://www.google.com")
            
        except Exception as e:
            print(e, "Chrome")

        
    # Make sure we exit/close chrome when we are done with scraping
    def end():
        print("... closing Chrome")
        driver.quit()
        
class Insta(WebScrape):
    '''
    Child class for scraping Instagram
    '''
    pass
    # A session ID is needed
    # # This allows you to scrape without being kicked out since cookies are saved
    ''' 
        Generating Session ID 
            1. Login into Instagram on web-browser
            2. Inspect page & select 'application' tab
            3 . Select 'cookies' and then double-click 'sessionid'
            4. Wait for the complete value to load, copy & past below
    '''
    '''
        session_id = "47863029330%3AhgNVPdS9MYlwmE%3A4"
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57",
            "cookie": "sessionid={session_id};"
            }
    '''
    # Load profile
    
    # Load posts
    
    # Read comments in posts
    
    # Search hastags containing phrase/brand/user
    
    # Search tags containing phrase/brand/user

class Fb(WebScrape):
    '''
    Child class for scraping Facebook
    '''
    pass
    # Load profile
    
    # Load posts
    
    # Read comments in posts
    
    # Search hashtags containing phrase/brand/user
    
    # Search tags containing phrase/brand/user
    
class Twit(WebScrape):
    '''
    Child class for scraping Twitter
    '''
    pass
    # Search for tweets containing phrase/brand/user
    
    # Search hashtags containing phrase/brand/user
    
    
    
'''
!!!
Testing code below
!!!
'''

WebScrape.start()