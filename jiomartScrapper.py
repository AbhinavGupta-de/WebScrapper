from bs4 import BeautifulSoup
import requests

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"}


def jiomartScrapper(url):
    url = "https://www.jiomart.com/p/groceries/nutri-binge-1kg-vitals-california-almonds/603409805"
    html_text = requests.get(url, headers=header).text

    soup = BeautifulSoup(html_text, 'lxml')

    # print(soup.prettify())

    # Getting the name of the product
    title_div = soup.find('div', id='pdp_product_name')
    product_name = title_div.text.strip()

    # print(product_name)

    # Getting the price of the product
    price_div = soup.find('div', class_='product-price-offer-box')
    price_span = price_div.find('div', id='price_section')
    price = price_span.text.strip()
    print(price)
