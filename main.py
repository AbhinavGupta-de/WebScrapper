def compare_prices():
    """
    This function compares the prices of a product from different e-commerce websites.
    It takes the URL of the product as input and scrapes the website to get the price.
    The function then compares the prices and prints the website where the product is cheaper.
    """
    price1 = 0
    price = 0

    for i in range(1, 3):
        website_url = input("Enter the URL of the product: ")
        if 'flipkart' in website_url:
            from flipkartScrapper import flipkartScrapper
            price1 = flipkartScrapper(website_url)
        elif 'amazon' in website_url:
            from amazonScrapper import amazonScrapper
            price = amazonScrapper(website_url)
        elif 'myntra' in website_url:
            from myantraScrapper import myantraScrapper
            myantraScrapper(website_url)
        elif 'croma' in website_url:
            from cromaScrapper import cromaScrapper
            cromaScrapper(website_url)
        elif 'shopclues' in website_url:
            from shopcluesScrapper import shopcluesScrapper
            shopcluesScrapper(website_url)
        elif 'jiomart' in website_url:
            from jiomartScrapper import jiomartScrapper
            jiomartScrapper(website_url)

    price1 = price1.replace('₹', '')
    price1 = price1.replace(',', '')
    price = price.replace(',', '')
    price = price.replace('.', '')

    if int(price) > int(price1):
        print(f'The Product is cheaper at Flipkart for ₹{price1}')
    elif int(price) < int(price1):
        print(f'The Product is cheaper at Amazon for ₹{price}')


compare_prices()
