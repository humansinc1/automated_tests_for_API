import requests
import allure

from endpoints.endpoint import Endpoint


class Authorization(Endpoint):
    auth_name = "SergeiL"
    body = {"name": f"{auth_name}"}
    user_name = None
    token = None
    result = None


    @allure.step('Creating a token')
    def get_token(self, body=None):
        body = body if body else self.body
        self.result = requests.post(f'{self.url}/authorize', json=body)
        if self.result.status_code == 200:
            self.user_name = self.result.json()['user']
            self.token = self.result.json()['token']
            return self.token
        else:
            return self.result

    @allure.step('Checking if token user name is correct')
    def is_user_name_correct(self):
        assert self.user_name == self.auth_name, 'Wrong user name'

    @allure.step('Checking if token created')
    def is_token_created(self):
        assert self.token is not None, 'token is empty'
