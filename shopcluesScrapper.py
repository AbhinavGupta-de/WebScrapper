from bs4 import BeautifulSoup
import requests

header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0"}


def shopcluesScrapper(url):
    url = "https://www.shopclues.com/hrv-geneva-wrist-watch-women-stainless-steel-gold-watch-luxury-casual-ladies-watches-149210967.html"
    html_text = requests.get(url, headers=header).text

    soup = BeautifulSoup(html_text, 'lxml')

    print(soup.prettify())
