# type in terminal: pip install beautifulsoup4
# type in terminal: pip install requests
# type in terminal: pip install lxml

import requests
from bs4 import BeautifulSoup
import time
from random import randrange
import json

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

def get_article_urls(url):  # For step 1, saving article links in .txt file
    s = requests.Session()  # creating session
    response = s.get(url=url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")
    # For step 1:
    # with open("index.html", "w") as file:  # save data in html file
    #     file.write(response.text)

    for page in range(1, 10):  # references
        response = s.get(url=f"https://techxplore.com/hi-tech-news/page{page}.html", headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find_all("article", class_="sorted-article d-flex")

        article_urls_list = []
        for i in data:
            articles_urls = i.find("a", class_="news-link").get("href")
            article_urls_list.append(articles_urls)

        time.sleep(randrange(2, 5))

    with open("articles_urls.txt", "w") as file:  # saving all links in .txt file
        for url in article_urls_list:
            file.write(f"{url}\n")


def get_data(file_path):  # receiving data from every link
    with open(file_path) as file:
        urls_list = [line.strip() for line in file.readlines()]

    s = requests.Session()

    urls_count = len(urls_list)
    result_data = []

    with requests.Session() as session:  # for opening and closing session
        for i, url in enumerate(urls_list):  # The enumerate function in Python converts a data collection object
            # into an enumerate object. Enumerate returns an object that contains a counter as a key for each value
            # within an object, making items within the collection easier to access
            response = session.get(url=url, headers=headers)
            soup = BeautifulSoup(response.text, "lxml")

            path1 = soup.find("main", class_="bg-white news").find("div", class_="col-12 mt-3 mb-5 mb-lg-0")
            article_title = path1.find("h1", class_="text-extra-large line-low mb-2").text.strip()
            article_date = path1.find("p", class_="text-uppercase text-low").text.strip()
            article_img = path1.find("div", class_="article-gallery lightGallery").find("img").get("src")
            article_text = path1.find("div", class_="mt-4 text-low-up text-regular article-main").find("p").text.strip()
            result_data.append(
                {
                    "original_url": url,
                    "article_title": article_title,
                    "article_date": article_date,
                    "article_img": article_img,
                    "article_text": article_text,
                }
            )
            print(f"Finished {i + 1}/{urls_count}")
            time.sleep(randrange(2, 5))  # "we are not a bot"

        with open("result.json", "w") as file:  # writing all data in .json file
            json.dump(result_data, file, indent=4, ensure_ascii=False)  # Using a ensure_ascii=False , we make sure
            # resulting JSON store Unicode characters as-is instead of \u escape sequence


def main():
    # For step 1:
    # get_article_urls(url="https://techxplore.com/hi-tech-news/")
    get_data("articles_urls.txt")

if __name__ == "__main__":
    main()
