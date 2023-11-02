from bs4 import BeautifulSoup
import requests

header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8"}


def flipkartScrapper(url):
    """
    Scrapes the product name and price from Flipkart website.

    Args:
        url (str): The URL of the product page on Flipkart.

    Returns:
        tuple: A tuple containing the product name (str), website name (str), and price (str).
    """
    try:
        html_text = requests.get(url, headers=header).text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying to access the URL: {e}")
        return None, None, None

    soup = BeautifulSoup(html_text, 'lxml')

    # Check if the product is available or not
    if not soup.find('span', class_='B_NuCI'):
        print("Product not found on Flipkart.")
        return None, None, None

    # Getting the name of the product
    try:
        title_div = soup.find('span', class_='B_NuCI')
        title = title_div.text.strip()
        product_name = title
    except Exception as e:
        print(
            f"An error occurred while trying to get the name of the product: {e}")
        return None, None, None

    # Check if the product name is available or not
    if product_name is None:
        print("Unable to get name of the product. Please try again later or try another product.")
        return None, None, None

    # Getting the price of the product
    try:
        price_div = soup.find('div', class_='_30jeq3 _16Jk6d')
        price = price_div.text.strip()
    except Exception as e:
        print(
            f"An error occurred while trying to get the price of the product: {e}")
        return None, None, None

    # Check if the price is available or not
    if price is None:
        print("Unable to get price of the product. Please try again later or try another product.")
        return None, None, None

    print(f'The Product: {product_name} is available at Flipkart for {price}')

    return product_name, "Flipkart", price
