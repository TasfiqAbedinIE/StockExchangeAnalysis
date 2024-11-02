import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

word_to_meaning = "abate"
url = f'https://www.dictionary.com/browse/{word_to_meaning}'
# url = 'https://www.dse.com.bd/latest_share_price_scroll_l.php'
r = requests.get(url)
print(r)

soup = BeautifulSoup(r.text, 'lxml')
# print(soup)
# meta_data = {
#     "Price": [],
#     "Title": []
# }

# price_data = soup.find_all("h4", {"class": "price float-end card-title pull-right"})
# meta_data["Price"].extend(i.text for i in price_data)
# product_des = soup.find_all("a", {"class": "title"})
# print(product_des)
# meta_data["Title"].extend(i.text for i in product_des)
#
# print(meta_data)

# data = soup.find_all(["h4", "a", "p"])
# data = soup.find_all(string=re.compile("Acer"))
#
# print(data)


# -------------------- Video Lecture - 13 --------------------- #
# names = soup.find_all("a", class_="title")
# product_names = []
# product_names.extend(i.text for i in names)
# print(product_names)
#
# prices = soup.find_all("h4", class_="price float-end card-title pull-right")
# prices_list = []
# prices_list.extend(i.text for i in prices)
# print(prices_list)
#
# desc = soup.find_all("p", class_="description card-text")
# desc_list = []
# desc_list.extend(i.text for i in desc)
# print(desc_list)
#
# reviews = soup.find_all("p", class_="review-count float-end")
# reviews_list = []
# reviews_list.extend(i.text for i in reviews)
# print(reviews_list)
#
# product_description = {
#     "Products": product_names,
#     "prices": prices_list,
#     "Description": desc_list,
#     "Reviews": reviews_list
# }
#
# product_dataframe = pd.DataFrame(product_description)
# print(product_dataframe)
#
# product_dataframe.to_csv("products_details.csv")

#-------------------------- Video Lecture - 14 --------------------------- #
# boxes = soup.find_all("div", class_="col-md-4 col-xl-4 col-lg-4")
# print(len(boxes))

# box = soup.find_all("div", class_="col-md-4 col-xl-4 col-lg-4")[2]
# print(box)
# name = box.find("a").text
# print(name)

# ------------------------- Video Lecture - 15 ---------------------------- #

# table = soup.find("table", class_="table table-bordered")
# # print(table)
# headers = table.find("thead")
# # print(headers)
# header_row = headers.find_all("th")
# # print(header_row)
# titles = []
# titles.extend(i.text for i in header_row)
# print(titles)

# ------------------------- Video Lecture - 16 ---------------------------- #

# rows = table.find_all("tr")
# for i in rows[1:]:
#     data = table.find_all("td")
#     print(data)

# ------------------------ Video Lecture - 17 ------------------------------ #
# Extracting data from Dictionary.com

word = soup.find("h1", class_="elMfuCTjKMwxtSEEnUsi")
parts_of_speech_section = soup.find("div", class_="S3nX0leWTGgcyInfTEbW")
parts_of_speech = parts_of_speech_section.find("h2")
definition_section = soup.find("ol", class_="lpwbZIOD86qFKLHJ2ZfQ E53FcpmOYsLLXxtj5omt")
definition_section = definition_section.find_all("li")
print(word.text)
print(parts_of_speech.text)
print(len(definition_section))

for i in definition_section:
    print(i)