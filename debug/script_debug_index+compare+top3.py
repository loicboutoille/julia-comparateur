import requests
import json
from bs4 import BeautifulSoup
products_list = []

print("Bienvenue sur le comparateur JULiA pour les produits de désinfection des instruments MEGADENTAL")


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

print("Nombre de produits présents dans cette catégorie :")
print(len(products_list))

products_sorted = sorted(products_list, key=lambda x: x["price"])

print("\nLes 3 produits les moins chers")
for p in products_sorted[:3]:
    print(p["name"], "|", p["price"], "€")

print("\nLes 3 produits les plus chers")
for p in products_sorted[-3:]:
    print(p["name"], "|", p["price"], "€")

print()
print("----------INDEX des PRODUITS-----------")

for i, p in enumerate(products_sorted):
    print(i, p["name"], "|", p["price"], "€")

print("Pour comparer deux produits, utiliser leur numérotation :")

a = int(input("Produit A (numéro) : "))
b = int(input("Produit B (numéro) : "))

prod_a = products_sorted[a]
prod_b = products_sorted[b]

diff = prod_a["price"] - prod_b["price"]

print("\nCOMPARAISON")
print(prod_a["name"], prod_a["price"], "€")
print(prod_b["name"], prod_b["price"], "€")
print("Différence :", round(abs(diff), 2), "€")

with open("products.json", "w", encoding="utf-8") as f:
    json.dump(products_list, f, ensure_ascii=False, indent=4)