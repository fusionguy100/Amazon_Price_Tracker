import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/Instant-Pot-Duo-Mini-Programmable/dp/B06Y1YD5W7"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

# Try to find the price
whole = soup.find("span", class_="a-price-whole")
fraction = soup.find("span", class_="a-price-fraction")

if whole and fraction:
    full_price = f"{whole.get_text().strip()}{fraction.get_text().strip()}"
    print(f"Full Price: ${full_price}")
else:
    print("Price not found — Amazon may be blocking the request or the HTML structure changed.")
