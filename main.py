# Importing packages
from selenium.webdriver import Chrome 
from bs4 import BeautifulSoup
from instascrape import Profile, scrape_posts
# !! Only grabbing 2 packages to increase load time while testing functionality
# Need to read posts, comments, hashtags

class WebScrape():
    '''
    This is the parent class for the webscraping application
    This holds all functionality for webscraping
    '''
    def __init__(self, driver):
        self.driver = driver
        
    # Setting up how we want Chrome to run
    def start(self):
        # Rendering JavaScript with webdriver
        # This runs the Google Chrome browser using chromedriver
        webdriver = Chrome("chromedriver.exe")
        
        # By default, ChromeDriver will create a new temporary profile for each session.
        # You can use the user-data-dir Chrome command-line switch to tell Chrome which profile to use:
        options = webdriver.ChromeOptions()
        
       # A session ID is needed
       # # This allows you to scrape without being kicked out since cookies are saved
        ''' 
        Generating Session ID 
            1. Login into Instagram on web-browser
            2. Inspect page & select 'application' tab
            3 . Select 'cookies' and then double-click 'sessionid'
            4. Wait for the complete value to load, copy & past below
        '''
        
        session_id = 'SESSION ID GOES HERE'
        headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Mobile Safari/537.36 Edg/87.0.664.57",
            "cookie": "sessionid={session_id};"
            }
        
    # Make sure we exit/close chrome when we are done with scraping
    def end(self):
        pass
        
class Insta(WebScrape):
    '''
    Child class for scraping Instagram
    '''
    pass
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