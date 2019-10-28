import requests
import logging


class TestApi:

    LOGGER = logging.getLogger(__name__)

    def test_headers(self):
        link = "http://httpbin.org/headers"
        TestApi.LOGGER.info("Sending request: " + link)
        result = requests.get(link)
        TestApi.LOGGER.info("Getting response: " + str(result.json()))
        assert 200 == result.status_code

    def test_status(self):
        link = "http://httpbin.org/status/200"
        TestApi.LOGGER.info("Sending request: " + link)
        result = requests.get(link)
        TestApi.LOGGER.info("Getting response: " + str(result.content))
        assert 200 == result.status_code

    def test_redirect(self):
        link = "http://httpbin.org/redirect/1"
        TestApi.LOGGER.info("Sending request: " + link)
        result = requests.get(link)
        TestApi.LOGGER.info("Getting response: " + str(result.json()))
        assert 302 == result.status_code