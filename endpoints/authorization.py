from re import split
from urllib import request
import requests
import allure
import dotenv
import os

from endpoints.endpoint import Endpoint


class Authorization(Endpoint):
    auth_name = "SergeiL"
    body = {"name": f"{auth_name}"}
    user_name = None
    token = None
    result = None
    base_path = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_path, '.env')
    dotenv.load_dotenv()

    def get_token_status(self):
        result = requests.get(f'{self.url}/authorize/{dotenv.get_key(self.file_path, 'AUTH_TOKEN')}')
        return result
    
    def create_token(self, body=None):
        body = body if body else self.body
        self.result = requests.post(f'{self.url}/authorize', json=body)
        if self.result.status_code == 200:
            self.user_name = self.result.json()['user']
            self.token = self.result.json()['token']
            dotenv.set_key(self.file_path, 'AUTH_TOKEN', self.token)
            return self.token
        else:
            return print(f'Status code: {self.result}. Token was not created!')

    @allure.step('Creating a token')
    def get_token(self):
        if self.get_token_status().status_code == 404:
            self.create_token()
        else:
            self.token = dotenv.get_key(self.file_path, 'AUTH_TOKEN')
            self.result = self.get_token_status()
            self.user_name = self.get_token_status().text.split()[-1]
            return self.token

    @allure.step('Checking if token user name is correct')
    def is_user_name_correct(self):
        assert self.user_name == self.auth_name, 'Wrong user name'

    @allure.step('Checking if token created')
    def is_token_created(self):
        assert self.token is not None, 'token is empty'


class CheckToken(Endpoint):
    def check_token_status(self, token=None):
        if token == None:
            self.result = requests.get(f'{self.url}/authorize/{dotenv.get_key(self.file_path, 'AUTH_TOKEN')}')
        else:
            self.result = requests.get(f'{self.url}/authorize/{token}')
        return self.result
