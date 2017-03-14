# In[3]:

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# In[4]:
def startscrape():
    page = 'http://allrecipes.com/'
    uClient = uReq(page)
    page_html = uClient.read()
    page_soup = soup(page_html, "html.parser")
    items = page_soup.findAll("article", {"class": "grid-col--fixed-tiles"})
    return items


def getlinks(items):
    mealnames = []
    mealurls = []
    for item in items:
        try:
            stuff = item.img["title"]
            mealnames.appendF(stuff)
            print(stuff)
            mealurls.append("http://allrecipes.com" + item.a["href"])

        except TypeError:
            print("")
        except KeyError:
            print("")
    print("done")
    return mealurls


def getIngredients(foodpage):
    uClient = uReq(foodpage)
    food_html = uClient.read()
    page_soup = soup(food_html, "html.parser")
    uClient.close()
    ingredients = page_soup.find_all("span", {"class", "recipe-ingred_txt added"})
    clean = []
    count = 0
    fooditems = ingredients
    for fooditem in fooditems:
        clean.append(fooditem.text)
        print(clean[count])
        count = count + 1

    return clean






