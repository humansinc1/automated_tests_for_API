import allure


class Endpoint:
    url = 'http://memesapi.course.qa-practice.com'
    headers = None
    result = None


    @allure.step('Adding token to headers')
    def authorization(self, token, headers=None):
        self.headers = {"Authorization": f"{token}"}
        headers = headers if headers else self.headers
        return headers

    @allure.step('Checking if response status is 200')
    def is_response_status_200(self):
        assert self.result.status_code == 200, 'Wrong status code'

    @allure.step('Checking if response status is 401')
    def is_response_status_401(self):
        assert self.result.status_code == 401, 'Wrong status code'

    @allure.step('Checking if response status is 400')
    def is_response_status_400(self):
        assert self.result.status_code == 400, 'Wrong status code'

    @allure.step('Checking if response status is 404')
    def is_response_status_404(self):
        assert self.result.status_code == 404, 'Wrong status code'

    @allure.step('Checking if response status is 403')
    def is_response_status_403(self):
        assert self.result.status_code == 403, 'Wrong status code'

    @allure.step('Checking if body text is correct')
    def is_body_text_correct(self, body=None):
        body = body if body else self.body
        assert self.result.json()['text'] == body['text']

    @allure.step('Checking if body url is correct')
    def is_body_url_correct(self, body=None):
        body = body if body else self.body
        assert self.result.json()['url'] == body['url']

    @allure.step('Checking if body tags is correct')
    def is_body_tags_correct(self, body=None):
        body = body if body else self.body
        assert self.result.json()['tags'] == body['tags']

    @allure.step('Checking if body info is correct')
    def is_body_info_correct(self, body=None):
        body = body if body else self.body
        assert self.result.json()['info'] == body['info']
