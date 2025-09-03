import requests
import allure

from endpoints.endpoint import Endpoint


class CreateMeme(Endpoint):
    text = "99 little bugs"
    body = {
        "text": f"{text}",
        "url": "https://imgs.search.brave.com/uxF23AlGbpdMvtkhGF_yNDyCkkiEjG_4JdYd9Pw1GI0/rs:fit:500:0:1:0/g:ce/" +
               "aHR0cHM6Ly93d3cu/c2lsaWNvbnJlcHVi/bGljLmNvbS93cC1j/b250ZW50L3VwbG9h/ZHMvMjAxNS8wNS9R/" +
               "QS1UZXN0ZXItbWVt/ZS0wMy5qcGc",
        "tags": ['grumpy cat', 'qa', 'fun'],
        "info": {'subject': ['qa', 'bugs'], 'color': 'sand'}
    }
    meme_id = None


    @allure.step('Creating a meme')
    def create_meme(self, token, body=None):
        body = body if body else self.body
        self.result = requests.post(f'{self.url}/meme', json=body, headers=self.authorization(token))
        if self.result.status_code == 200:
            self.meme_id = self.result.json()['id']

    @allure.step('Checking if body text is correct')
    def is_body_text_correct(self):
        assert self.result.json()['text'] == self.text
