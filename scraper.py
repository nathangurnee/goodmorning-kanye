# Web scraper to access quotes
import requests
from bs4 import BeautifulSoup

# URLs for different quote website pages
pg1 = requests.get('https://www.brainyquote.com/authors/kanye-west-quotes')
pg2 = requests.get('https://www.brainyquote.com/authors/kanye-west-quotes_2')
pg3 = requests.get('https://quotefancy.com/kanye-west-quotes')

# Loads a list with quotes from page
soup = BeautifulSoup(pg1.content, 'html.parser')
quote_blocks_pg1 = soup.find_all('div', class_='grid-item qb clearfix bqQt')
quotes_pg1 = [ block.find('div', attrs={'style': 'display: flex;justify-content: space-between'}).text.strip() for block in quote_blocks_pg1 ]

soup = BeautifulSoup(pg2.content, 'html.parser')
quote_blocks_pg2 = soup.find_all('div', class_='grid-item qb clearfix bqQt')
quotes_pg2 = [ block.find('div', attrs={'style': 'display: flex;justify-content: space-between'}).text.strip() for block in quote_blocks_pg2 ]

soup = BeautifulSoup(pg3.content, 'html.parser')
quote_blocks_pg3 = soup.find_all('div', class_='q-container')
quotes_pg3 = [ block.find('a', class_='quote-a').text for block in quote_blocks_pg3 ]

# All quotes
quotes = quotes_pg1 + quotes_pg2 + quotes_pg3