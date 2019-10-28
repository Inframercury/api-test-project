import requests
import logging


class TestApi:

    LOGGER = logging.getLogger(__name__)

    """Тестирование endpoint http://httpbin.org/headers"""
    def test_headers(self):
        link = "http://httpbin.org/headers"
        TestApi.LOGGER.info("Sending request: " + link)
        result = requests.get(link)
        TestApi.LOGGER.info("Getting response: " + str(result.json()))
        try:
            #проверяем, что вернулся status_code 200
            assert 200 == result.status_code
        except AssertionError as err:
            TestApi.LOGGER.error(err, exc_info=True)
            raise err

    """Тестирование endpoint http://httpbin.org/status с параметром 200"""
    def test_status(self):
        link = "http://httpbin.org/status/300"
        TestApi.LOGGER.info("Sending request: " + link)
        result = requests.get(link)
        TestApi.LOGGER.info("Getting response: " + str(result.content))
        try:
            #проверяем, что вернулся status_code 200
            assert 300 == result.status_code
        except AssertionError as err:
            TestApi.LOGGER.error(err, exc_info=True)
            raise err

    def test_redirect(self):
        """Тестирование endpoint http://httpbin.org/redirect/ с параметром 1"""
        link = "http://httpbin.org/redirect/1"
        TestApi.LOGGER.info("Sending request: " + link)
        result = requests.get(link)
        TestApi.LOGGER.info("Getting response: " + str(result.json()))
        try:
            #проверяем, что вернулся status_code 302
            assert 302 == result.status_code
        except AssertionError as err:
            TestApi.LOGGER.error(err, exc_info=True)
            raise err
