import requests
from bs4 import BeautifulSoup

url = "https://appbrewery.github.io/instant_pot/"

response = requests.get(url=url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

price = soup.find(class_ = "a-offscreen").get_text()

price_without_currency = price.split("$")[1]
