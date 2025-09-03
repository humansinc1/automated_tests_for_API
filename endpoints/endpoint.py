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
