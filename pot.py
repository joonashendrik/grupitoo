import requests
from bs4 import BeautifulSoup

URL = "https://www.selver.ee/soodushinnaga-tooted/toidukaubad?limit=96"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

food_elements = soup.find_all("div", class_="ProductCard")
#print(food_elements)

price_list = []
food_e = input("Sisesta toode: ")
for food_el in food_elements:
    #print(food_el)
    food_name = food_el.find("h3").string.lower()
    if food_e in food_name:
        #print(food_name)
        #print(food_el.find("div", class_="ProductPrice"))
        if len(food_el.find("div", class_="ProductPrice")):
            #print(food_el.find("div", class_="ProductPrice"))
            price = food_el.find("div", class_="ProductPrice").find("span").contents[0]
            price_list.append([price, food_name])
            #print(price)
print(price_list)
