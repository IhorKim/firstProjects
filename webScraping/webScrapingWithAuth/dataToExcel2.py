import xlsxwriter
from webScrapingWithAuthorization import get_url


def writer(parameters):
    book = xlsxwriter.Workbook(r"C:\Python\myProjects\webScraping\data2.xlsx")
    page = book.add_worksheet("Quotes")

    row = 0
    column = 0

    page.set_column("A:A", 50)
    page.set_column("B:B", 50)

    for item in parameters():
        page.write(row, column, item[0])
        page.write(row, column + 1, item[1])

        row += 1

    book.close()

writer(get_url)
