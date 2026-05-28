import allure
import requests


class ApiClient:
    base_url = 'https://postman-echo.com'
    @allure.step('GET запрос')
    def get_request(self):
        response = requests.get(f'{self.base_url}/get')

        allure.attach(f'{self.base_url}/get', name='URL',
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text, name='Response',
                      attachment_type=allure.attachment_type.JSON)
        return response

    @allure.step('POST запрос')
    def post_request(self):
        response = requests.post(f'{self.base_url}/post')

        allure.attach(f'{self.base_url}/post', name='URL',
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text, name='Response',
                      attachment_type=allure.attachment_type.JSON)
        return response



    @allure.step('PUT запрос')
    def put_request(self):
        response = requests.put(f'{self.base_url}/put')

        allure.attach(f'{self.base_url}/put', name='URL',
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text, name='Response',
                      attachment_type=allure.attachment_type.JSON)
        return response


    @allure.step('GET запрос с query параметрами')
    def get_query_parameters_request(self, params):
        response = requests.get(f'{self.base_url}/get', params)

        allure.attach(f'{self.base_url}/get', name='URL',
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text, name='Response',
                      attachment_type=allure.attachment_type.JSON)
        return response


    @allure.step('DELETE запрос')
    def delete_request(self):
        response = requests.delete(f'{self.base_url}/delete')

        allure.attach(f'{self.base_url}/delete', name='URL',
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(response.text, name='Response',
                      attachment_type=allure.attachment_type.JSON)
        return response
