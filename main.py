def comparePrices():
    """
    This function compares the prices of a product from different e-commerce websites.
    It takes the URL of the product as input and scrapes the website to get the price.
    The function then compares the prices and prints the website where the product is cheaper.
    """

    # Initialize empty lists to store the product prices, names and domains
    price = []
    name = []
    domain = []

    product_fetched = True

    # Loop through the range of 1 to 3 to get the URLs of the products
    for i in range(1, 3):
        website_url = input("Enter the URL of the product: ")

        # Check if the URL belongs to Flipkart
        if 'flipkart' in website_url:
            from flipkartScrapper import flipkartScrapper
            [product_name, domain_name, product_price] = flipkartScrapper(
                website_url)

            if product_name == None or domain_name == None or product_price == None:
                product_fetched = False
                print(
                    "Error occurred while trying to get the product details. Please try again later or try another product.")
                break

            # Append the product details to the respective lists
            price.append(product_price)
            name.append(product_name)
            domain.append(domain_name)

        # Check if the URL belongs to Amazon
        elif 'amazon' in website_url:
            from amazonScrapper import amazonScrapper
            [product_name, domain_name,
                product_price] = amazonScrapper(website_url)

            if product_name == None or domain_name == None or product_price == None:
                product_fetched = False
                print(
                    "Error occurred while trying to get the product details. Please try again later or try another product.")
                break

            # Append the product details to the respective lists
            price.append(product_price)
            name.append(product_name)
            domain.append(domain_name)

        # Check if the URL belongs to Myntra
        elif 'myntra' in website_url:
            from myantraScrapper import myantraScrapper
            [product_name, domain_name,
                product_price] = myantraScrapper(website_url)

            if product_name == None or domain_name == None or product_price == None:
                product_fetched = False
                print(
                    "Error occurred while trying to get the product details. Please try again later or try another product.")
                break

            # Append the product details to the respective lists
            price.append(product_price)
            name.append(product_name)
            domain.append(domain_name)

        # Check if the URL belongs to Croma
        elif 'croma' in website_url:
            from cromaScrapper import cromaScrapper
            [product_name, domain_name,
                product_price] = cromaScrapper(website_url)

            if product_name == None or domain_name == None or product_price == None:
                product_fetched = False
                print(
                    "Error occurred while trying to get the product details. Please try again later or try another product.")
                break

            # Append the product details to the respective lists
            price.append(product_price)
            name.append(product_name)
            domain.append(domain_name)

        # Check if the URL belongs to Shopclues
        elif 'shopclues' in website_url:
            from shopcluesScrapper import shopcluesScrapper
            [product_name, domain_name,
                product_price] = shopcluesScrapper(website_url)

            if product_name == None or domain_name == None or product_price == None:
                product_fetched = False
                print(
                    "Error occurred while trying to get the product details. Please try again later or try another product.")
                break

            # Append the product details to the respective lists
            price.append(product_price)
            name.append(product_name)
            domain.append(domain_name)

        # Check if the URL belongs to JioMart
        elif 'jiomart' in website_url:

            from jiomartScrapper import jiomartScrapper
            [product_name, domain_name,
                product_price] = jiomartScrapper(website_url)

            if product_name == None or domain_name == None or product_price == None:
                product_fetched = False
                print(
                    "Error occurred while trying to get the product details. Please try again later or try another product.")
                break

            # Append the product details to the respective lists
            price.append(product_price)
            name.append(product_name)
            domain.append(domain_name)

        # This part is commented out because the BigBasket scraper is not currently ready.
        # elif 'bigbasket' in website_url:

        #     from bigbasketScrapper import bigbasketScrapper
        #     [product_name, domain_name,
        #         product_price] = bigbasketScrapper(website_url)

        #     price.append(product_price)
        #     name.append(product_name)
        #     domain.append(domain_name)

        else:
            print("Please enter a valid URL")
            break

    if (product_fetched == False):
        return

    # Remove the currency symbol and commas from the prices
    for i in range(len(price)):
        price[i] = price[i].replace('₹', '')
        price[i] = price[i].replace(',', '')
        price[i] = price[i].replace('.', '')

    # Find the minimum price and its index in the list
    min_price = min(price)
    min_price_index = price.index(min_price)

    # Print the website where the product is cheaper
    print(
        f'The Product: {name[min_price_index]} is available at {domain[min_price_index]} for ₹{min_price}')


comparePrices()


"""

This function below is the old version of the comparePrices() function. It is not used in the program. It is kept here for reference.

"""

# def compare_prices():
#     """
#     This function compares the prices of a product from different e-commerce websites.
#     It takes the URL of the product as input and scrapes the website to get the price.
#     The function then compares the prices and prints the website where the product is cheaper.
#     """
#     price1 = 0
#     price = 0

#     for i in range(1, 3):
#         website_url = input("Enter the URL of the product: ")
#         if 'flipkart' in website_url:
#             from flipkartScrapper import flipkartScrapper
#             price1 = flipkartScrapper(website_url)
#         elif 'amazon' in website_url:
#             from amazonScrapper import amazonScrapper
#             price = amazonScrapper(website_url)
#         elif 'myntra' in website_url:
#             from myantraScrapper import myantraScrapper
#             myantraScrapper(website_url)
#         elif 'croma' in website_url:
#             from cromaScrapper import cromaScrapper
#             cromaScrapper(website_url)
#         elif 'shopclues' in website_url:
#             from shopcluesScrapper import shopcluesScrapper
#             shopcluesScrapper(website_url)
#         elif 'jiomart' in website_url:
#             from jiomartScrapper import jiomartScrapper
#             jiomartScrapper(website_url)

#     price1 = price1.replace('₹', '')
#     price1 = price1.replace(',', '')
#     price = price.replace(',', '')
#     price = price.replace('.', '')

#     if int(price) > int(price1):
#         print(f'The Product is cheaper at Flipkart for ₹{price1}')
#     elif int(price) < int(price1):
#         print(f'The Product is cheaper at Amazon for ₹{price}')

# compare_prices()
