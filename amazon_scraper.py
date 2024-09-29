from dis import disco

from bs4 import BeautifulSoup
import requests
from numpy.core.defchararray import strip


class FlipKart:

    def init(self, product_url):

        self.product_url = product_url


