from bs4 import BeautifulSoup
import requests
from numpy.core.defchararray import strip


class AmazonScraper:

    def __init__(self, product_link):

        self.amazon_product_url = product_link
        self.product_html = requests.get(url= self.amazon_product_url).text


    def get_product_data(self):

        soup = BeautifulSoup(self.product_html, "html.parser")
        price = strip(soup.find("div", class_="a-section a-spacing-none aok-align-center aok-relative").text.split("$")[1])
        return price


