# type in terminal: pip install beautifulsoup4
# type in terminal: pip install requests
# type in terminal: pip install lxml
# type in terminal: pip install XlsxWriter
"""
Beautiful Soup is a Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages
that can be used to extract data from HTML, which is useful for web scraping
lxml is the most feature-rich and easy-to-use library for processing XML and HTML in the Python language
"""
import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.3"}  # When your
# browser is connected to a website, a User-Agent field is included in the HTTP header. The data of the header field
# varies from browser to browser. This information is used to serve different websites to different web browsers and
# different operating systems. "We are not a bot"

def download(url):  # function for downloading images
    resp = requests.get(url, stream=True)  # when stream=True on the request, this method will avoid reading the whole
    # file into memory at once for just the large responses
    r = open("C:\\Python\\myProjects\\webScraping\\images\\" + url.split("/")[-1], "wb")  # creating name of new
    # downloaded files. "wb" - write bytes
    for value in resp.iter_content(1024*1024):  # 1 mb per loop
        r.write(value)
    r.close()

def get_url():  # turning into generator object for better memory usage
    for count in range(1, 8):  # loop for every page on site, we have 7 pages
        url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")  # "lxml" using instead of built-in "html.parser"

        data = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")  # returns a list of all divs with such class

        for i in data:
            card_url = "https://scrapingclub.com" + i.find("a").get("href")
            yield card_url  # We should use yield when we want to iterate over a sequence, but don't want to store the entire sequence in memory.
            """
            name = i.find("h4", class_="card-title").text.strip()  
            price = i.find("h5").text
            url_img = "https://scrapingclub.com" + i.find("img", class_="card-img-top img-fluid").get("src")
            print(name + "\n" + price + "\n" + url_img)
            """


def array():  # also generator
    for i in get_url():
        response = requests.get(i, headers=headers)
        sleep(3)  # break between requests. Not loading server, site will not block us. "We are not a bot"
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find("div", class_="card mt-4 my-4")
        name = data.find("h3", class_="card-title").text
        price = data.find("h4").text
        description = data.find("p", class_="card-text").text
        url_img = "https://scrapingclub.com" + data.find("img", class_="card-img-top img-fluid").get("src")
        download(url_img)

        yield name, price, description, url_img




