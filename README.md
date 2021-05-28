# Sentiment Analysis Tool
## Analyzing Instagram, Facebook, and Twitter

**Open Source Used**
- Selenium Webdriver - Automates/imitates user controlling browser
- BeautifulSoup - Reads elements on the page
- facebook_scraper - Open source to scrape FB with no API
- sntwitter - Open source to scrape Twitter with no API
- Pandas
- TextBlob - Open source for sentiment analysis structured on NLTK (natural language toolkit)

### Webscraper
The first part of this tool is scraping Facebook, Twitter and Instagram for a specified user profile.  The comments underneath posts are collected and stored in .csv files for later use.

### Data Analysis
After the data is saved into .csv it is ready for analysis with Pandas and TextBlob.

Using TextBlob to analyze the polarity of user comment data.