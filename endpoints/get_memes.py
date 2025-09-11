import requests
import allure

from endpoints.endpoint import Endpoint


class GetAllMemes(Endpoint):


    @allure.step('Getting all memes list')
    def get_all_memes(self, token):
        self.result = requests.get(f'{self.url}/meme', headers=self.authorization(token))

    @allure.step('Checking that result is not empty')
    def is_result_not_empty(self):
        assert self.result is not None


class GetOneMeme(Endpoint):


    @allure.step('Getting one meme by ID')
    def get_one_meme(self, meme_id, token):
        self.result = requests.get(f'{self.url}/meme/{meme_id}', headers=self.authorization(token))
        if self.result.status_code == 200:
            return self.result.json()
        else:
            return self.result
        
    @allure.step('')
    def is_id_the_same_as_in_request(self, meme_id):
        assert self.result.json()['id'] == meme_id
