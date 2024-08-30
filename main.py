from bs4 import BeautifulSoup
import re
import requests

url = "https://www.fantasypros.com/nfl/rankings/half-point-ppr-cheatsheets.php"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")

print(doc)