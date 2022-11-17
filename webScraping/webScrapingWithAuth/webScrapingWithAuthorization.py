# type in terminal: pip install beautifulsoup4
# type in terminal: pip install requests
# type in terminal: pip install lxml
# type in terminal: pip install XlsxWriter
"""
Beautiful Soup is a Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages
that can be used to extract data from HTML, which is useful for web scraping
lxml is the most feature-rich and easy-to-use library for processing XML and HTML in the Python language
"""
from requests import Session
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.3"}  # When your
# browser is connected to a website, a User-Agent field is included in the HTTP header. The data of the header field
# varies from browser to browser. This information is used to serve different websites to different web browsers and
# different operating systems. "We are not a bot"

work = Session()  # class in requests for work with cookies

work.get("https://quotes.toscrape.com/", headers=headers)  # just open site

response = work.get("https://quotes.toscrape.com/login", headers=headers)  # login page

soup = BeautifulSoup(response.text, "lxml")

token1 = soup.find("form").find("input").get("value")

data = {"csrf_token": token1, "username": "123", "password": "123"}

result = work.post("https://quotes.toscrape.com/login", headers=headers, data=data, allow_redirects=True)  # we have redirect
# from main login page


def get_url():  # turning into generator object for better memory usage
    for count in range(1, 15):  # loop for every page on site, we have 15 pages
        url = f"http://quotes.toscrape.com/page/{count}"
        response = work.get(url, headers=headers)
        sleep(3)
        soup = BeautifulSoup(response.text, "lxml")  # "lxml" using instead of built-in "html.parser"

        data = soup.find_all("div", class_="quote")  # returns a list of all divs with such class

        for i in data:
            author = i.find("small", class_="author").text
            quote = i.find("span", class_="text").text
            yield author, quote









