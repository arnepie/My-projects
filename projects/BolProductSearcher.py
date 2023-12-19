from bs4 import BeautifulSoup
import requests
import re

search_term = input("What product do you want to search for? ")

url = f"https://www.bol.com/be/nl/s/?searchtext={search_term}"
page = requests.get(url).text
doc = BeautifulSoup(page, "html.parser")


div = doc.find_all(class_="product-title--inline")
div2 = doc.find_all(class_="price-block__price")

fixed_items = []
fixed_prices = []

for item in div:
    items = item.find("a")
    fixed_items.append(items.string)


for price in div2:
    prices = price.find("span")
    fixed_prices.append(prices.string)

item_counter = 0

for item in fixed_items:
    print(fixed_items[item_counter])
    print(fixed_prices[item_counter])
    print(" ")
    print("--------------------------------------------------")
    item_counter += 1