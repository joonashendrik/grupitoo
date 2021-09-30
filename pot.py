import requests
from bs4 import BeautifulSoup

URL = "https://www.selver.ee/soodushinnaga-tooted/toidukaubad?limit=1000"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

food_elements = soup.find_all("h3", class_="ProductCard__title")
# print(food_elements)

price_list = []

for food_el in food_elements:
    food_name = food_el.find("a").string.lower()
    if "sink" in food_name:
        print(food_name)
        if len(food_el.find_parents("a", class_="ProductBage_bage--label")) == 1:
            price = food_el.find_parents("a", class_="ProductBage_bage--label")[0].find("label").contents[-1]
            price_list.append([price, food_name])

# print(price_list)
