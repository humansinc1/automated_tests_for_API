import requests
import allure

from endpoints.endpoint import Endpoint
from endpoints.get_memes import GetOneMeme


class DeleteMeme(Endpoint):


    @allure.step('Deleting a meme')
    def delete_meme(self, token, meme_id):
        self.result = requests.delete(f'{self.url}/meme/{meme_id}', headers=self.authorization(token))

    @allure.step('Checking if meme is deleted')
    def is_deleted_meme_id_absent_in_meme_list(self, meme_id, token):
        get_meme = GetOneMeme().get_one_meme(meme_id, token)
        assert get_meme.status_code == 404
