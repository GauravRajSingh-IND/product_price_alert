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

        self.is_message_send = False

    def set_client(self, retries:int=3):
        """
        This function set twilio client object.
        :param retries: number of retries.
        :return:
        """
        for retrie in range(retries):

            # Set client object using sid and token.
            client = Client(self.sid, self.token)

            # check if client is set or not.
            if client:
                self.is_client_set= True
                return client
            else:
                raise f"Client not set properly on try: {retrie}"

    def send_message(self, message= "Hello Testing", retries:int = 3):
        """
        This function send whatsapp message to user.
        :return:
        """
        for retry in range(retries):
            message = self.client.messages.create(
                body=message,
                from_=self.company_number,
                to = f"whatsapp:{self.user_phone_number}"
            )

            if message.sid:
                self.is_message_send = True
                return None

