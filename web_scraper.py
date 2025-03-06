from bs4 import BeautifulSoup
import requests

def extract_info(html):
    # take html extract faculty info return list of dictionaries
    soup = BeautifulSoup(html, "lxml")
    stock = {
        "name": soup.select("div#qwidget_pageheader h1")[0].text,
        "price": soup.select("div#qwidget_lastsale")[0].text,
        "change": soup.select("div#qwidget_percent")[0].text,
    }
    return stock 

def get_html(url):
    # Get html from url
    response = requests.get(url)
    return response.text

# MAIN PROGRAM
symbol = input("Enter Stock Symbol: ")
url = 'http://www.nasdaq.com/symbol/' + symbol
html = get_html(url)
result = extract_info(html)
print("Name: %s" % result["name"])
print("Price: %s" % result["price"])
print("Change: %s" % result["change"])
