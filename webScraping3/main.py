"""
pip install requests
pip install beautifulsoup4
pip install lxml

In this case for downloading .xlsx files from site we need to use Burp Suite. It is an integrated platform
and graphical tool for performing security testing of web applications, it supports the entire testing process,
from initial mapping and analysis of an application's attack surface, through to finding and exploiting security
vulnerabilities.
"""
import requests
import csv
from datetime import datetime
from bs4 import BeautifulSoup


requests.packages.urllib3.disable_warnings()  # turn off warnings in terminal

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
}


def get_data(url):
    cur_date = datetime.now().strftime("%Y_%m_%d")
    response = requests.get(url=url, headers=headers)

    with open(file="index.html", mode="w") as file:  # saving site in index.html file
        file.write(response.text)

    with open(file="index.html") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    table = soup.find("table", id="ro5xgenergy")  # finding html tags on site

    data_tag_th = table.find("thead").find_all("tr")[-1].find_all("th")

    table_headers = ["Area"]
    for dth in data_tag_th:
        dth = dth.text.strip()
        table_headers.append(dth)

    with open(file=f"data-{cur_date}.csv", mode="w") as file:  # writing all headers in .csv file
        writer = csv.writer(file)

        writer.writerow(
            (
                table_headers
            )
        )

    tbody_tags_trs = table.find("tbody").find_all("tr")

    ids = []
    data = []
    for tr in tbody_tags_trs:
        area = tr.find("th").text.strip()

        data_by_month = tr.find_all('td')
        data = [area]
        for dbm in data_by_month:
            if dbm.find("a"):
                area_data = dbm.find("a").get("href")
                id = area_data.split("/")[4].split("?")[0]
                ids.append(id)
            elif dbm.find("span"):
                area_data = dbm.find("span").text.strip()
            else:
                area_data = "No data"

            data.append(area_data)

        with open(file=f"data-{cur_date}.csv", mode="a") as file:
            writer = csv.writer(file)

            writer.writerow(
                (
                    data
                )
            )

    with open(file="ids.txt", mode="w") as file:
        for id in ids:
            file.write(f"{id}\n")


def download_xlsx(file_path="ids.txt"):
    with open(file=file_path) as file:
        ids = [line.strip() for line in file.readlines()]

    for id in ids:
        headers = {
            "Host": "data.bls.gov",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://data.bls.gov",
            "Dnt": "1",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Te": "trailers",
            "Connection": "close",
        }

        data = f"request_action=get_data&reformat=true&from_results_page=true&years_option=specific_years&delimiter=comma&output_type=multi&periods_option=all_periods&output_view=data&output_format=excelTable&original_output_type=default&annualAveragesRequested=false&series_id={id}"

        response = requests.post("https://data.bls.gov/pdq/SurveyOutputServlet", headers=headers, data=data,
                                 verify=False)

        with open(file=f"xlsx_files/{id}.xlsx", mode="wb") as file:
            file.write(response.content)


def main():
    get_data(url="https://www.bls.gov/regions/midwest/data/AverageEnergyPrices_SelectedAreas_Table.htm")
    # download_xlsx()


if __name__ == "__main__":
    main()