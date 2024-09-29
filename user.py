import json

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
