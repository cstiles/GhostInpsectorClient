import sys
import os
import requests

class Client(object):
    """A simple API client for the GhostInspector's API.
    see README for more details
    """


    tests_name = []
    test_suites = []
    #last_update = 89    


    
    def __init__(self, api_token=None, url_base="https://api.ghostinspector.com/v1/"):
        self.api_token = api_token
        self.vars = "" #["startUrl" : "http://google.com",... ]
        self.url_base = url_base

###

    def _request(self, path, parameters=None):

        data = requests.get("%s%s?apiKey=%s" % (self.url_base, path, self.api_token))
        print("%s%s?apiKey=%s" % (self.url_base, path, self.api_token))
        return data.json()


###EXTRAS


    def get_id_by_test_name(self, testid):
        """
        Retrieve the 
        """
        response = self._request("tests/<testId>/")
        print(response)
        return response
   
    def get_test_by_name(self, test_name):
        """
        Retrieve the 
        """ 
        id = self.get_id_by_test_name(test_name)
        self.get_test_by_id(id)
        response = self._request("tests/<testId>/")
        print(response)
        return response

###TESTS

    def get_test_by_id(self, testid):
        """
        https://api.ghostinspector.com/v1/tests/<testId>/?apiKey=<apiKey> 
        """
        response = self._request("tests/<testId>/")
        print(response)
        return response

    def dup_test_by_id(self):
        """        
        https://api.ghostinspector.com/v1/tests/<testId>/duplicate/?apiKey=<apiKey>
        
        """
        response = self._request("tests/")
        print(response)
        return response

    def get_tests(self):
        """        
        https://api.ghostinspector.com/v1/tests/?apiKey=<apiKey>

        """
        response = self._request("tests/")
        print(response)
        return response

###TESTS_SUITES

    def get_test_suites(self):
        """
        https://api.ghostinspector.com/v1/suites/?apiKey=<apiKey> 
        """
        response = self._request("tests/")
        print(response)
        return response

    def get_test_suite(self):
        """
        https://api.ghostinspector.com/v1/suites/<suiteId>/?apiKey=<apiKey>
        """
        response = self._request("tests/")
        print(response)
        return response
    

###TESTS_RESULTS


    def get_suite_results_by_results_id(self, id):
        """
        https://api.ghostinspector.com/v1/suite-results/<suiteResultId>/?apiKey=<apiKey>
        """
        print("get_test_results")
        response = self._request("tests/")
        print(response)
        return response

    def get_results_suite_results_by_results_id(self, id):
        """
        https://api.ghostinspector.com/v1/suite-results/<suiteResultId>/results/?apiKey=<apiKey>
        """
        print("get_test_results")
        response = self._request("tests/")
        print(response)
        return response
        
    def cancel_suite_results_by_results_id(self, id):
        """
        https://api.ghostinspector.com/v1/suite-results/<suiteResultId>/cancel/?apiKey=<apiKey>
        """
        print("get_test_results")
        response = self._request("tests/")
        print(response)
        return response

    def get_suite_results_by_suite_id(self, id):
        """
        
        https://api.ghostinspector.com/v1/suites/<suiteId>/results/?apiKey=<apiKey>

        """
        print("get_test_results")
        response = self._request("tests/")
        print(response)
        return response

    def get_test_results_by_id(self, id):
        """
        https://api.ghostinspector.com/v1/tests/<testId>/results/?apiKey=<apiKey>

        """
        print("get_test_results")
        response = self._request("tests/")
        print(response)
        return response

    def get_results_id(self, id):
        """
        https://api.ghostinspector.com/v1/results/<resultId>/?apiKey=<apiKey>

        """
        print("get_test_results")
        response = self._request("tests/")
        print(response)
        return response
    
    def cancel_results_id(self, id):
        """
        https://api.ghostinspector.com/v1/results/<resultId>/cancel/?apiKey=<apiKey>

        """
        print("get_test_results")
        response = self._request("tests/")
        print(response)
        return response
    

###TESTS_EXUCUTIONS
        
    def run_test(self):
        """
        https://api.ghostinspector.com/v1/tests/<testId>/execute/?apiKey=<apiKey>&startUrl=<startUrl> 
        
        """
        response = self._request("tests/")
        print(response)
        return response
    
###EXPORT_SEL


    def export_test_by_id_in_selenuim(self, id, version):
        """
        https://api.ghostinspector.com/v1/tests/<testId>/export/selenium-html/?apiKey=<apiKey>
        https://api.ghostinspector.com/v1/tests/<testId>/export/selenium-json/?apiKey=<apiKey>
        """
        response = self._request("tests/")
        print(response)
        return response

    def export_suite_by_id_in_selenuim(self, id, version):
        """
        https://api.ghostinspector.com/v1/suites/<suiteId>/export/selenium-html/?apiKey=<apiKey>
        https://api.ghostinspector.com/v1/suites/<suiteId>/export/selenium-json/?apiKey=<apiKey>
        """
        response = self._request("tests/")
        print(response)
        return response
