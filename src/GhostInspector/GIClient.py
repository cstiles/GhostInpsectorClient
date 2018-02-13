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
        
    def get_test_results(self):
        """Retrieve the 
        """
        print("get_test_results")
        response = self._request("tests/")
        print(response)
        return response
    
    def get_test_by_id(self, testid):
        """Retrieve the 
        """
        response = self._request("tests/<testId>/")
        print(response)
        return response

    def get_id_by_test_name(self, testid):
        """Retrieve the 
        """
        response = self._request("tests/<testId>/")
        print(response)
        return response
   
    def get_test_by_name(self, test_name):
        """Retrieve the 
        """ 
        response = self._request("tests/<testId>/")
        id = self.get_id_by_test_name(test_name)
        self.get_test_by_id(id)
       
        return response
    
    def get_test_suites(self):
        """Retrieve the 
        """
        response = self._request("tests/")
        print(response)
        return response
    
    def run_test(self):
        """Retrieve the 
        """
        response = self._request("tests/")
        print(response)
        return response

    def get_tests(self):
        """Retrieve the 
        """
        response = self._request("tests/")
        print(response)
        return response
    
    def run_tests(self):
        """Retrieve the 
        """
        response = self._request("tests/")
        print(response)
        return response
    
    def get_test_results(self):
        """Retrieve the 
        """
        response = self._request("tests/")
        print(response)
        return response
    
    def _request(self, path, parameters=None):

        data = requests.get("%s%s?apiKey=%s" % (self.url_base, path, self.api_token))
        print("%s%s?apiKey=%s" % (self.url_base, path, self.api_token))
        return data.json()
