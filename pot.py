import requests
from bs4 import BeautifulSoup

URL = "https://www.selver.ee/soodushinnaga-tooted/toidukaubad?limit=94"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

food_elements = soup.find_all("div", class_="ProductCard_link")

Price_list = []

for food_el in food_elements:
    food_name = food_el.find("a").string.lower()
    if "juust" in food_name:
        # print(food_name)
        if len(food_el.find_parents("span", class_="ProductBage_bage--label")) == 1:
            price = food_el.find_parents("span", class_="ProductBage_bage--label")[0].find("label").contents[-1]
            Price_list.append([price, food_name])

print(Price_list)
