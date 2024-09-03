from bs4 import BeautifulSoup
import re
import requests

url = "https://www.fantasypros.com/nfl/rankings/half-point-ppr-cheatsheets.php"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

elements = doc.find('div', class_ = "tooltip-left ecr-vs-adp-wrap")

page_text = elements

print(doc.prettify())

# Trying to learn more about WebScrapping, so im going to scrap for a lil and watch videos about it