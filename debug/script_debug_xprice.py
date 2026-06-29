import requests
from bs4 import BeautifulSoup

print("Script OK")

url = "https://www.megadental.fr/desinfection-sterilisation/desinfection/desinfection-des-instruments.html"

response = requests.get(url)

print(response.status_code)

html = response.text
soup = BeautifulSoup(html, "html.parser")

products = soup.select("form.product-item")

for p in products:
    name = p.find("h3").text
    brand = p.find("div", class_="text-secondary").text

    print(name)
    print(brand)
    print("-" * 30)