from bs4 import BeautifulSoup
import requests

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"}


def cromaScrapper(url):
    url = "https://www.croma.com/croma-2-litres-2-stones-wet-grinder-with-coconut-scrapper-atta-kneader-in-built-overload-protection-white-purple-/p/227773"
    html_text = requests.get(url, headers=header).text

    soup = BeautifulSoup(html_text, 'lxml')

    print(soup.prettify())

    # Getting the name of the product
    # title_div = soup.find('div', class_='pdp-title')
    # title_h1 = soup.find('h1', id='pd-title').text.strip()
    # product_name = title_h1
    #
    # print(product_name)
