import xml.etree.ElementTree as ET
import bs4 as soup
import requests
from lxml import etree

url = "https://v2.snsfeeder.app/ig/rss/7f074de9da34599777724d8d78550fe666977eecc4a92e02c897aa63ca840934"

url_link = requests.get(url)
file = soup.BeautifulSoup(url_link.text, features="xml")

find_content = file('content')[-1]

# print(file)
print(find_content)