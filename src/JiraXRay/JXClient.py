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
      


    
    def __init__(self, api_token=None, jira_naming_convention='CB-', url_base="https://api.ghostinspector.com/v1/"):
        self.jira_naming_convention = jira_naming_convention 
        self.api_token = api_token
        self.vars = "" #["startUrl" : "http://google.com",... ]
        self.url_base = url_base

###

    def _request(self, path, parameters=None):

        data = requests.get("%s%s?apiKey=%s" % (self.url_base, path, self.api_token))
        return data.json()


###EXTRAS

    def get_id_by_test_name(self, testname):
        """
        Retrieve the 
        """
        response = self._request("tests/")

        for r in response['data']:
            if r["name"] == testname:
                return r['_id']
        return False
    
    def get_id_by_suite_name(self, testid):
        """
        Retrieve the 
        """
        response = self._request("suite/<testId>/")
        
        return response
   
    def get_test_by_name(self, test_name):
        """
        Retrieve the 
        """ 
        id = self.get_id_by_test_name(test_name)
        self.get_test_by_id(id)
        response = self._request("tests/{0}/".format(id))
        
        return response


    def get_test_details(self, test_name):
        """
        Retrieve the details for a given test case
        returns: A list of details broken down in array of the cases found based on jira_naming_convention
        """ 
        id = self.get_id_by_test_name(test_name)
        print(id)
        response = self.get_test_by_id(id)
        details = response['data']['details']
        return str(details).splitlines()


###TESTS

    def get_test_by_id(self, testid):
        """
        https://api.ghostinspector.com/v1/tests/<testId>/?apiKey=<apiKey> 
        """
        response = self._request("tests/{0}/".format(testid))
        
        return response

    def dup_test_by_id(self):
        """        
        https://api.ghostinspector.com/v1/tests/<testId>/duplicate/?apiKey=<apiKey>
        
        """
        response = self._request("tests/{0}/duplicate".format(testid))
        
        return response

    def get_tests(self):
        """        
        https://api.ghostinspector.com/v1/tests/?apiKey=<apiKey>

        """
        response = self._request("tests/")
        
        return response


###TESTS_SUITES

    def get_test_suites(self):
        """
        https://api.ghostinspector.com/v1/suites/?apiKey=<apiKey> 
        """
        response = self._request("suites/")
        
        return response

    def get_test_suite(self, suiteId):
        """
        https://api.ghostinspector.com/v1/suites/<suiteId>/?apiKey=<apiKey>
        """
        response = self._request("suites/{0}/".format(suiteId))
        
        return response
    

###TESTS_RESULTS

    def get_suite_results_by_results_id(self, suiteResultId):
        """
        https://api.ghostinspector.com/v1/suite-results/<suiteResultId>/?apiKey=<apiKey>
        """
        print("get_test_results")
        response = self._request("suite-results/{0}/".format(suiteResultId))
        
        return response

    def get_results_suite_results_by_results_id(self, suiteResultId):
        """
        https://api.ghostinspector.com/v1/suite-results/<suiteResultId>/results/?apiKey=<apiKey>
        """
        print("get_test_results")
        response = self._request("suite-results/{0}/results/".format(suiteResultId))
        
        return response
        
    def cancel_suite_results_by_results_id(self, suiteResultId):
        """
        https://api.ghostinspector.com/v1/suite-results/<suiteResultId>/cancel/?apiKey=<apiKey>
        """
        print("get_test_results")
        response = self._request("suite-results/{0}/cancel/".format(suiteResultId))
        
        return response

    def get_suite_results_by_suite_id(self, suiteId):
        """
        
        https://api.ghostinspector.com/v1/suites/<suiteId>/results/?apiKey=<apiKey>

        """
        print("get_test_results")
        response = self._request("suites/{0}/results/".format(suiteId))
        
        return response

    def get_test_results_by_id(self, testId):
        """
        https://api.ghostinspector.com/v1/tests/<testId>/results/?apiKey=<apiKey>

        """
        print("get_test_results")
        response = self._request("tests/{0}/results/".format(testId))
        
        return response

    def get_results_id(self, resultId):
        """
        https://api.ghostinspector.com/v1/results/<resultId>/?apiKey=<apiKey>

        """
        print("get_test_results")
        response = self._request("results/{0}/".format(resultId))
        
        return response
    
    def cancel_results_id(self, resultId):
        """
        https://api.ghostinspector.com/v1/results/<resultId>/cancel/?apiKey=<apiKey>

        """
        print("get_test_results")
        response = self._request("results/{0}/cancel".format(resultId))
        
        return response
    

###TESTS_EXUCUTIONS
        
    def run_test(self, testId):
        """
        https://api.ghostinspector.com/v1/tests/<testId>/execute/?apiKey=<apiKey>&startUrl=<startUrl> 
        
        """
        response = self._request("tests/{0}/execute/".format(resultId))
        
        return response


###EXPORT_SEL

    def export_test_by_id_in_selenuim(self, testId, version):
        """
        https://api.ghostinspector.com/v1/tests/<testId>/export/selenium-html/?apiKey=<apiKey>
        https://api.ghostinspector.com/v1/tests/<testId>/export/selenium-json/?apiKey=<apiKey>
        """
        response = self._request("tests/{0}/export/selenium-{1}/".format(testId, version))
        
        return response

    def export_suite_by_id_in_selenuim(self, suiteId, version):
        """
        https://api.ghostinspector.com/v1/suites/<suiteId>/export/selenium-html/?apiKey=<apiKey>
        https://api.ghostinspector.com/v1/suites/<suiteId>/export/selenium-json/?apiKey=<apiKey>
        """
        response = self._request("suites/{0}/export/selenium-{1}/".format(suiteId, version))
        
        return response
