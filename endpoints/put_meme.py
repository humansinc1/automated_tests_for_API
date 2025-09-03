import requests
import allure

from endpoints.endpoint import Endpoint


class PutMeme(Endpoint):


    @allure.step('Updating a meme')
    def put_meme(self, meme_id, token, body=None):
        self.text = "updated"
        self.body = {
            "id": meme_id,
            "text": f"{self.text}",
            "url": "updated",
            "tags": ['updated', 'qa', 'fun'],
            "info": {'updated': ['qa', 'bugs'], 'color': 'sand'}
        }
        body = body if body else self.body
        self.result = requests.put(f'{self.url}/meme/{meme_id}', headers=self.authorization(token), json=body)
        return self.result.status_code
    
    @allure.step('Checking if body text was changed')
    def is_body_text_changed(self):
        assert self.result.json()['text'] == self.text
