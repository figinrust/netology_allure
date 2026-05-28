import allure

from utils.api_client import ApiClient
from utils.helpers import assert_status_code

@allure.epic('Api запросы')
@allure.feature('Проверка отправки api запросов')
class TestEcho:
    @allure.title('Успешная отправка GET-запроса')
    @allure.description('Api запрос: метод GET')
    def test_get_basic(self):
        client = ApiClient()
        response = client.get_request()

        assert_status_code(response, 200)
        assert response.headers["Content-Type"] == 'application/json; charset=utf-8'

        data = response.json()
        assert data['args'] == {}

        assert data['url'] == 'https://postman-echo.com/get'
        assert data["headers"]["host"] == 'postman-echo.com'

    @allure.title('Успешная отправка POST-запроса')
    @allure.description('Api запрос: метод POST')
    def test_post_basic(self):
        client = ApiClient()
        response = client.post_request()

        assert_status_code(response, 200)
        assert response.headers["Content-Type"] == 'application/json; charset=utf-8'

        data = response.json()

        assert data['args'] == {}
        assert data['data'] == {}
        assert data['files'] == {}
        assert data['form'] == {}

        assert data['url'] == 'https://postman-echo.com/post'
        assert data["headers"]["host"] == 'postman-echo.com'

    @allure.title('Успешная отправка PUT-запроса')
    @allure.description('Api запрос: метод PUT')
    def test_put_basic(self):
        client = ApiClient()
        response = client.put_request()

        assert_status_code(response, 200)
        assert response.headers["Content-Type"] == 'application/json; charset=utf-8'

        data = response.json()

        assert data['args'] == {}
        assert data['data'] == {}
        assert data['files'] == {}
        assert data['form'] == {}

        assert data['url'] == 'https://postman-echo.com/put'
        assert data["headers"]["host"] == 'postman-echo.com'

    @allure.title('Успешная отправка GET-запроса с qwery параметрами')
    @allure.description('Api запрос: метод GET + qwery параметры')
    def test_get_qwery_parameters_basic(self, valid_qwery_params):
        client = ApiClient()
        response = client.get_query_parameters_request(valid_qwery_params)

        assert_status_code(response, 200)
        assert response.headers["Content-Type"] == 'application/json; charset=utf-8'

        data = response.json()

        assert data['args'] == valid_qwery_params
        assert data['url'] == 'https://postman-echo.com/get?foo=bar&test=123'
        assert data["headers"]["host"] == 'postman-echo.com'

    @allure.title('Успешная отправка DELETE-запроса')
    @allure.description('Api запрос: метод DELETE')
    def test_delete_basic(self):
        client = ApiClient()
        response = client.delete_request()

        assert_status_code(response, 200)
        assert response.headers["Content-Type"] == 'application/json; charset=utf-8'

        data = response.json()

        assert data['args'] == {}
        assert data['data'] == {}
        assert data['files'] == {}
        assert data['form'] == {}

        assert data['url'] == 'https://postman-echo.com/delete'
        assert data["headers"]["host"] == 'postman-echo.com'