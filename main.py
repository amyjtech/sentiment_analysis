# Importing packages
from selenium.webdriver import Chrome 
from bs4 import BeautifulSoup
from instascrape import *
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