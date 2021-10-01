import requests
from bs4 import BeautifulSoup

URL = "https://www.selver.ee/liha-ja-kalatooted/varske-kala-mereannid?page=1"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

food_elements = soup.find_all("div", class_="ProductCard")
#print(food_elements)

price_list = []

for food_el in food_elements:
    #print(food_el)
    food_name = food_el.find("h3").string.lower()
    if "filee" in food_name:
        #print(food_name)
        print(food_el.find("div", class_="ProductPrice"))
        if len(food_el.find_parents("div", class_="ProductPrice__unit-price")) == 1:
            price = food_el.find_parents("div", class_="ProductPrice__unit-price")[0].find("div").contents[-1]
            price_list.append([price, food_name])

print(price_list)
