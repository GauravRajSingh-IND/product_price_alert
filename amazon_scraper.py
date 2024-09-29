from bs4 import BeautifulSoup
from time import sleep

import requests
import logging



class FlipKart:

    def __init__(self, product_url):

        self.product_url = product_url
        self.product_content = None

        self.get_html_content()

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

scraper = FlipKart(product_url="https://www.flipkart.com/fastrack-revoltt-fs1-1-83-display-bt-calling-fastcharge-110-sports-mode-200-watchfaces-smartwatch/p/itmab38b5cb1e3fb?pid=SMWGN4YEWGNZ2GGM&lid=LSTSMWGN4YEWGNZ2GGMLUF0DF&marketplace=FLIPKART&store=ajy%2Fbuh&srno=b_1_1&otracker=browse&fm=organic&iid=en_b7JsMyyguhWLYks8TTYbjVqU07YmcRcrBhmo0l8ZJWfIoZphkA9_s5Cmd769LKLGumbirN8aXntYeeti4EWO_vUFjCTyOHoHZs-Z5_PS_w0%3D&ppt=hp&ppn=homepage&ssid=7eozf4qgio0000001727584549633")
