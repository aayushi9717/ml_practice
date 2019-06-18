"""
Created on Thu May 30 15:03:36 2019

@author: pcc
"""
import urllib.request
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
page=urllib.request.urlopen(wiki)
from bs4 import BeautifulSoup
soup = BeautifulSoup(page)
print (soup.prettify())
print (soup.title)
all_tables=soup.find_all('table')

right_table=soup.find('table', class_='wikitable sortable plainrowheaders')
print(right_table)
