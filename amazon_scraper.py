from dis import disco

from bs4 import BeautifulSoup
import requests
from numpy.core.defchararray import strip


class AmazonScraper:

    def __init__(self, product_link):

        self.amazon_product_url = product_link
        self.product_html = requests.get(url= self.amazon_product_url).content


    def get_product_data(self):

        soup = BeautifulSoup(self.product_html, "html.parser")

        product_section = soup.find("div", id= "centerCol")
        product_name = strip(product_section.find("span", id= "productTitle").getText())

        price_section = soup.find("div", {"data-csa-c-slot-id":"apex_dp_center_column"})
        price_section = price_section.find("div", class_="celwidget")
        price = price_section.find("div", class_="a-section a-spacing-none aok-align-center aok-relative")
        print(price)






test = AmazonScraper(product_link="https://www.amazon.in/Apple-iPhone-15-Pro-256/dp/B0CHX6M6C8/ref=sr_1_2_sspa?crid=3P19WSN1KSBIU&dib=eyJ2IjoiMSJ9.U3tYZTJytmY17fRy4cOaBo44umHOYL8KAKQ7jrY_rHKKCWLSTjUM3lExE-OB0gQr3GBVB4UeFhVHMHbu39E2J1Jxn416_HXGTvQaJE5X5Ki9LAzpmCi0mp7yw4pY63XSl20ZqFASam7MIwzDYWcLDiOKWnx0T63S1dxCxGqR5MgsFuz9hkxGu2tWxM30oCagMgHWVDJ0OWlYvirqj11245sv8WgwGARBtKQ0Hv8ys08.1JjOk477-mHnSe8Jd9sBr0xs52EQ3m6RDTkHYgKq070&dib_tag=se&keywords=iphone+16+pro+max&qid=1727510477&sprefix=iphone%2Caps%2C209&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1")
test.get_product_data()

