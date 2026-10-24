import requests
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com/")
processing = BeautifulSoup(response.text, "html.parser")
find_all = processing.find_all("div", class_ = "quote")

quotes_list = []


for item in find_all:
    text =  item.find(class_ = "text").text
    author = item.find(class_ = "author" ).text


quotes_data = {
    "text" : text,
    "author": author
}
quotes_list.append(quotes_data)

print(quotes_list)