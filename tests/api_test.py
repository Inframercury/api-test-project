import requests
import logging
from allure_commons._allure import step
import pytest


class TestApi:

    LOGGER = logging.getLogger(__name__)

    @pytest.mark.api
    def test_headers(self):
        """Тестирование endpoint http://httpbin.org/headers"""
        with step("Тест заголовков"):
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

    @pytest.mark.api
    def test_status(self):
        """Тестирование endpoint http://httpbin.org/status с параметром 300"""
        with step("Тест статус кода"):
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

    @pytest.mark.api
    def test_redirect(self):
        """Тестирование endpoint http://httpbin.org/redirect/ с параметром 1"""
        with step("Тест редиректа"):
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
