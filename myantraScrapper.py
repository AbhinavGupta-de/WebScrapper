from bs4 import BeautifulSoup
import requests

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"}


def myantraScrapper(url):
    url = "https://www.myntra.com/sweatshirts/h%26m/hm-men-black-solid-relaxed-fit-zip-through-hoodie/15545792/buy"
    html_text = requests.get(url, headers=header).text

    soup = BeautifulSoup(html_text, 'lxml')

    print(soup.prettify())
    #
    # # Getting the name of the product
    # title_div = soup.find('div', class_='pdp-title')
    # title_h1 = title_div.find('h1', class_='pdp-title').text.strip()
    # product_name = title_div.text.strip()
    #
    # # print(product_name)
    #
    # # Getting the price of the product
    # price_span = soup.find('span', class_='pdp-price')
    # price = price_span.text.strip()
    # # print(price)
    #
    # # Getting the name of website
    # website_source = soup.find('title')
    # website_source = website_source.text.strip().split(' ')[-1]
    #
    # print(f'The Product: {product_name} is available at {website_source} for Rs.{price}')
