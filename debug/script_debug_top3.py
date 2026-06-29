import requests
import json
from bs4 import BeautifulSoup
products_list = []

print("Script OK")

url = "https://www.megadental.fr/desinfection-sterilisation/desinfection/desinfection-des-instruments.html"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

products = soup.select("form.product-item")

for p in products:
    name = p.find("h3").text.strip()
    brand = p.find("div", class_="text-secondary").text.strip()
    price_tag = p.find("span", class_="price")
    price = price_tag.text.strip() if price_tag else "Prix non trouvé"
    price = price.replace("€", "").replace(",", ".").strip()
    price = float(price)
    products_list.append({
    "name": name,
    "brand": brand,
    "price": price
})

print(len(products_list))

products_sorted = sorted(products_list, key=lambda x: x["price"])

for p in products_sorted:
    print(p["name"], "|", p["price"], "€")

print("\nLes 3 produits les moins chers")
for p in products_sorted[:3]:
    print(p["name"], "|", p["price"], "€")

print("\nLes 3 produits les plus chers")
for p in products_sorted[-3:]:
    print(p["name"], "|", p["price"], "€")

with open("products.json", "w", encoding="utf-8") as f:
    json.dump(products_list, f, ensure_ascii=False, indent=4)