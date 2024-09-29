import twilio
import os

from dotenv import load_dotenv
from twilio.rest import Client

class SendMessage:

    def __init__(self, phone_number):

        load_dotenv()

        self.user_phone_number = phone_number
        self.sid = os.getenv('twilio_SID')
        self.token = os.getenv('twilio_token')
        self.company_number = os.getenv('twilio_my_number')

        self.client = self.set_client()
        self.is_client_set = False

    def set_client(self, retries:int=3):
        """
        This function set twilio client object.
        :param retries: number of retries.
        :return:
        """

        for retrie in range(retries):
            client = Client(self.sid, self.token)

            if client:
                self.is_client_set= True
                return client
            else:
                raise f"Client not set properly on try: {retrie}"

whatsapp = SendMessage("123456")