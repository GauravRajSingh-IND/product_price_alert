from dis import disco

from bs4 import BeautifulSoup
from time import sleep

import requests
import logging



class FlipKart:

    def __init__(self, product_url):

        self.product_url = product_url
        self.product_content = None

        self.get_html_content()

    def scrape_product_data(self):

        soup = BeautifulSoup(self.product_content, "html.parser")

        product_image = self._get_src(soup.find("img", class_="DByuf4 IZexXJ jLEJ7H"),
                                      default="https://cdn.shopify.com/s/files/1/0070/7032/articles/product-label-design.jpg?v=1727450748&originalWidth=1848&originalHeight=782")
        product_name = self._get_text(soup.find("span", class_="VU-ZEz"), default="None")
        product_rating= self._get_text(soup.find("div", class_="XQDdHH"), default="None")
        user_rating_review = soup.find("span", class_="Wphh3N")
        offer_type = self._get_text(soup.find("div", class_="_2lX4N0"), default="None")

        price_now = self._get_text(soup.find("div", class_="Nx9bqj CxhGGd"), default="None")
        price_mrp = self._get_text(soup.find("div", class_="yRaY8j A6+E6v"), default="None")
        discount = self._get_text(soup.find("div", class_="UkUFwK WW8yVX"), default="None")

        total_user_rating = self._get_text(user_rating_review.select("span span")[1], default="None")
        total_user_reviews = self._get_text(user_rating_review.select("span span")[3], default="None")

        return {"Product_info": {"image":product_image, "name":product_name, "rating":product_rating, "offer":offer_type,
                                 "price_now":price_now, "price_mrp":price_mrp, "discount":discount, "total_rating":total_user_rating,
                                 "total_reviews":total_user_reviews}}

    def get_html_content(self, retries:int =3):
        """
        This function request flipkart product html data. If the data is fetched successfully self.product_content
        variable is assigned with the data.
        :return: nothing/None
        """

        # Set headers to mimic a browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        for i in range(retries):

            try:
                response = requests.get(url=self.product_url, headers=headers, timeout=10)

                if response.status_code == 200:
                    self.product_content = response.content
                    return True
                else:
                    logging.error(f"Unable to fetch data: {response.status_code}")
                    return False

            except requests.exceptions.Timeout:
                logging.warning("Request timed out, retrying...")
            except requests.exceptions.RequestException as e:
                logging.error(f"Request failed: {e}")

            sleep(3)

        return False

    def _get_text(self, element, default="N/A"):
        """Helper function to safely extract text from an element."""
        return element.get_text(strip=True) if element else default

    def _get_src(self, element, default="N/A"):
        """Helper function to safely extract text from an element."""
        return element['src'] if element else default

scraper = FlipKart(product_url="https://www.flipkart.com/fastrack-revoltt-fs1-1-83-display-bt-calling-fastcharge-110-sports-mode-200-watchfaces-smartwatch/p/itmab38b5cb1e3fb?pid=SMWGN4YEWGNZ2GGM&lid=LSTSMWGN4YEWGNZ2GGMLUF0DF&marketplace=FLIPKART&store=ajy%2Fbuh&srno=b_1_1&otracker=browse&fm=organic&iid=en_b7JsMyyguhWLYks8TTYbjVqU07YmcRcrBhmo0l8ZJWfIoZphkA9_s5Cmd769LKLGumbirN8aXntYeeti4EWO_vUFjCTyOHoHZs-Z5_PS_w0%3D&ppt=hp&ppn=homepage&ssid=7eozf4qgio0000001727584549633")

if scraper.product_content is not None:
    scraped_data = scraper.scrape_product_data()

    print(scraped_data)