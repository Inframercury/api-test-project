import logging

import pytest
from _pytest.python import Function
from _pytest.runner import CallInfo

def pytest_exception_interact(node, call: CallInfo, report):
    logger = logging.getLogger(__name__)
    if report.failed:
        logger.error(call.excinfo)