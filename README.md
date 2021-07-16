# Sentiment Analysis Tool
## Analyzing Instagram, Facebook, and Twitter

## Checklist
[ ] Create virtual environment
[ ] Download Packages
    - Selenium
    - facebook_scraper
    - sntwitter (?)
    - Pandas
    - BeautifulSoup4
[ ] Fix errors in scraping code
[ ] Save comments per parameters
[ ] Process with TextBlob or another NLP/machine learning

**Open Source Used**
- Selenium Webdriver - Automates/imitates user controlling browser
- BeautifulSoup - Reads elements on the page
- facebook_scraper - Open source to scrape FB with no API
- sntwitter - Open source to scrape Twitter with no API
- Pandas
- TextBlob - Open source for sentiment analysis structured on NLTK (natural language toolkit)

## Downloads Required
- Selenium [link]
- BeautifulSoup4 [https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup]
- facebook_scraper [https://pypi.org/project/facebook-scraper/]
- sntwitter [link]
- TextBlob [link] -- may not use
- Pandas [link]

### Webscraper
The first part of this tool is scraping Facebook, Twitter and Instagram for a specified user profile.  The comments underneath posts are collected and stored in .csv files for later use.

### Data Analysis
After the data is saved into .csv it is ready for analysis with Pandas and TextBlob.

Using TextBlob to analyze the polarity of user comment data.