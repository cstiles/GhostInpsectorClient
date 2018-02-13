import sys
import os


class Client(object):
    """A simple API client for the GhostInspector's API.
    see README for more details
    """
    
    def __init__(self, api_token=None, url_base="https://api.ghostinspector.com/"):
        self.api_token = api_token
        self.vars = "" #["startUrl" : "http://google.com",... ]
        self.url_base = url_base
    
    def get_test_results(self):
        """Retrieve the 
        """
        print("get_test_results")
        return self._request("")
    
    def get_test(self):
        """Retrieve the 
        """
        return self._request("")
    
    def run_test(self):
        """Retrieve the 
        """
        return self._request("")
    
    def run_tests(self):
        """Retrieve the 
        """
        return self._request("")
    
    def get_test_results2(self):
        """Retrieve the 
        """
        return self._request("")
    
    def _request(self, path, parameters=None):
        # Throw out parameters where the value is not None
        return True
