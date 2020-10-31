#!/usr/bin/python3

# Import libs
from lxml import html
import requests

# Test

webpage = 'https://www.bestbuy.com/site/pny-geforce-rtx-3080-10gb-xlr8-gaming-epic-x-rgb-triple-fan-graphics-card/6432655.p?skuId=6432655'


class Scraper:

    # Init
    def __init__ (self, shortNames=[], webPages=[], keyWords=[]):
        
        # Initialize header for request
        self.__headers = headers = { 'User-Agent': 'My User 0.1.0' };

        # Set Vars
        self.__shortNames = shortNames;
        self.__webPages = webPages;
        self.__keyWords = keyWords;


    # Scrapes a single webpage and returns True if keyWords found on page
    def __scrape(self, webpage, keyWords=[]):

        # Default
        ret = False;

        # Get page content
        rawContent = requests.get(webpage, headers=self.__headers);
        content = html.fromstring(rawContent.content);

        # Iterate through loop and determine if match was found
        for keyWord in keyWords:

            # Get Counts
            count = len(content.xpath('//text()[normalize-space() = "{}"]'.format(keyWord)));

            # Set True if count greater than 0
            if (count > 0):
                ret = True;
        
        return ret;

    # Run scrape across registered webpages
    def run_scrape(self):

        results = dict();

        # Iterate over webpages and scrape with keywords
        for i, webpage in enumerate(self.__webPages):

            # Build Results
            results[self.__shortNames[i]] = self.__scrape(webpage, self.__keyWords);

        return results;
