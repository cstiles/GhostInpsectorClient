import re
import pytest

pytest_plugins = 'pytester'

@pytest.fixture()
def gi_api_suite_tests_re():
    return 'suites/\w+/tests/'

@pytest.fixture()
def gi_api_test_re():
    return 'tests/\w+/$'

@pytest.fixture()
def gi_api_test_exec_re():
    return  'tests/\w+/execute/'

@pytest.fixture
def suite_resp():
    return '''
        {
            "data": [
                { "_id": 1, "name": "test 1", "suite": { "name": "ABC Suite" } },
                { "_id": 2, "name": "test 2", "suite": { "name": "ABC Suite" } }
            ]
        }'''

@pytest.fixture
def test_resp():
    return '''
        {
            "data": {
                "_id": "xyz789",
                "name": "test xyz789",
                "suite": { "name": "ABC Suite" }
            }
        }'''