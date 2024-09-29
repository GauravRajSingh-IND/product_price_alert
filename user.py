import json

from flipkart_scraper import FlipKart

class User:

    def __init__(self):

        self.username = None
        self.email = None
        self.whatsapp_number = None
        self.product_links = None
        self.postal_code = None


    def add_new_user(self, username, email, whatsapp_number, postal_code):
        """
        This function create a new account of a user.
        :param username: name of the user.
        :param email: email address of the user.
        :param whatsapp_number: whatsapp number of the user.
        :param postal_code: postal code of the user.
        :return: return None
        """

        # check if all the values are not empty.
        if not all([username, email, whatsapp_number, postal_code]):
            return False

        self.username = username
        self.email= email
        self.whatsapp_number = whatsapp_number
        self.postal_code = postal_code

        # Check if user already exist.
        if self.check_user_email(email=email):
            print("User already exist.")
            return False

        # create a dictionary using user information.
        data = {
                "username": self.username,
                "whatsapp_number": self.whatsapp_number,
                "postal_code": self.postal_code
                }


        # open json user file.
        with open("user_data.json", "r") as user_file:
            user_data = json.load(user_file)

        # add/dump json data to user_data.json.
        user_data[self.email] = data

        # Write back to json file.
        with open("user_data.json", "w") as user_file:
            json.dump(user_data, user_file, indent=4)

        print("User added successfully.")
        return True

    def check_user_email(self, email):
        """
        This function check if the user email is already exist or not.
        :param email: email of the user.
        :return:
        """

        # check if email id is not empty.
        if len(email) <= 0:
            print("Please enter the email address.")
            return False

        # open user_data json file.
        with open("user_data.json", "r") as file:
            user_data = json.load(file)

        # check if username exist in the user dataset.
        if email in user_data.keys():
            return True
        else:
            return False

    def add_product(self, email, product_link):
        """
        This function takes email id and product link and add it to product_link.
        :param email: email of user.
        :param product_link: product link
        :return:
        """

        # load json file and extract user data.
        with open("user_data.json", "r") as file_data:
            user_data = json.load(file_data)

        # Extract user data.
        user_info = user_data[email]

        # check weather product_link key exist or not.
        if "product_link" in user_info.keys():
            product_links = user_info["product_link"]

            # Check weather the product already exist.
            if product_link in product_links:
                print("Product already exist")
            else:
                user_info["product_link"].append(product_link)

        else:
            user_info["product_link"] = [product_link]

        # Update the user data.
        user_data[email].update(user_info)

        # add data to json file.
        with open("user_data.json", "w") as file:
            json.dump(user_data, file, indent=4)

    def delete_product(self, email):
        """
        This function delete one or more products.
        :param email: email of the user
        :return:
        """

        # Load the user_data json file.
        with open("user_data.json", "r") as file:
            user_data = json.load(file)

        # get user data.
        data = user_data[email]

        # extract product link list.
        products = data['product_link']

        # Check if product link exist.
        if len(products) == 0:
            print("Please enter products first")
            return False

        # loop over each product and create a list of product name's.
        for i, product in enumerate(products):
            scraper = FlipKart(product_url=product)
            product_name = scraper.scrape_product_data()['Product_info']['name']

            print(f"{i+1}: {product_name}")

        del_index = int(input("Please enter the number of the product which you want to delete: "))

        # delete the link from the user product list.
        products.pop(del_index-1)

        # Add/update the product section.
        if len(products) >0:
            user_data[email]['product_link'] = products
        else:
            user_data[email]['product_link'] = []

        # add data to json file.
        with open("user_data.json", "w") as file:
            json.dump(user_data, file, indent=4)


user = User()
user.delete_product(email="grsmanohar007@gmail.com")