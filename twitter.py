import sys
import csv

from selenium import webdriver
# This allows you to interact with webpage, type/enter text, etc.
from selenium.webdriver.common.keys import Keys
# Needed for using Chrome profile
from selenium.webdriver.chrome.options import Options

from selenium.common import exceptions

# Used for Explicit Waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup as bs

# Used for FB scraper
from facebook_scraper import get_posts

# Used for Twitter scraper
import snscrape.modules.twitter as sntwitter

# Used for sleep
import time

options = webdriver.ChromeOptions()
# Was getting an encoding error.  Passing r"" creates a raw string preventing errors when locating the file
options.add_argument("user-data-dir=C:\\Users\\AmySmith\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")
# Prevents windows error
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# This prevents the browser from closing immediately after running
options.add_experimental_option("detach", True)
# Variable = path to the chromedriver
PATH = "C:\Program Files (x86)\chromedriver.exe"

# The driver is what navigates the page, I chose Chrome
driver = webdriver.Chrome(PATH, options=options)

'''
TWITTER SCRAPER
x Scrape tweets by keyword/user
? Scrapes all tweets
x Save data in an easy to manage way
? Scrape indefinitely

x Scrape specific time/dates
o Scrapes replies/threads
o Identify tweets scraped so they are not scraped again
'''
def save_tweets():
    print("Starting Twitter Scrape")
    try:
        # Setting variables to be used below
        maxTweets = 500

        # Creating list to append tweet data to
        tweets_list = []

        # Appending the tweets to file
        save_twitter = open("tweets.txt", "a", encoding="utf-8")
        tweet_file = "tweets.csv"
        
        with open(tweet_file, 'a+',encoding='utf-8',newline='') as csvfile:
                
            tweet_csv = csv.writer(csvfile,delimiter='|')
                
            twitter_header = ['tweet_name','tweet_text','tweet_time']
                
            if 'tweet|' in tweet_file:
                pass
            else:
                tweet_csv.writerow(twitter_header)
            # Using TwitterSearchScraper to scrape data and append tweets to list
            # since:2020-06-01 until:2021-05-20 <-- specify timeframe
            for i,tweet in enumerate(sntwitter.TwitterSearchScraper('rideclutch').get_items()):
               
                if i>maxTweets:
                    break
                
                tweet_user = tweet.user.username
                tweet_text = tweet.content
                tweet_time = tweet.date
    
                tweets = [tweet_user, tweet_text.replace('\n',' '), str(tweet_time)]
                # Keeps track of number of tweets
                tweets_list.append(tweet_user)
                # Writes tweets list to CSV
                tweet_csv.writerow(tweets)
                
        print(f"{len(tweets_list)} Tweets saved to file")
        print("Twitter Scrape successful")
        driver.quit()
    except:
        # Print error
        print(sys.exc_info())
        # Let user know scrape was incomplete
        print("Twitter Scrape Incomplete\n")
        driver.quit()
        
save_tweets()