#!/usr/bin/env python
"""
Example
"""
import sys
import requests
import os
import pytest
from src.GhostInspector.GIClient import Client

###HELPERS

def basic_payload_validation_tests(payload):
    assert(payload != None)
    assert payload['code'] != 'ERROR', 'Erro type: {0}, Error message: {1}'.format(payload['errorType'], payload['message'])

def failure_payload_validation_tests(payload):
    assert(payload != None)
    assert payload['code'] == 'ERROR'
    assert payload['errorType'] == 'VALIDATION_ERROR'
    assert str(payload['message']).endswith('not found')


###EXTRAS

def test_get_test_by_id(GIAPIClient):
    a = GIAPIClient.get_id_by_test_name("Test1")
    a = GIAPIClient.get_test_by_id(a)
    basic_payload_validation_tests(a)

def test_get_test_by_name(GIAPIClient):
    a = GIAPIClient.get_test_by_name("Test1")
    basic_payload_validation_tests(a)

def test_get_test_details(GIAPIClient):
    a = GIAPIClient.get_test_details("Test1")
    assert ("CB-23452") in a
    assert ("CB-34") in a
    assert ("CB-245") in a
    assert ("CB-9424523") in a
    assert len(a) == 4


###TESTS

def test_get_test_results(GIAPIClient):
    a = GIAPIClient.get_test_results_by_id("sd")
    failure_payload_validation_tests(a)
    
def test_get_tests(GIAPIClient):
    a = GIAPIClient.get_tests()
    basic_payload_validation_tests(a)
    

###TESTS_SUITES   

def test_get_test_suites(GIAPIClient):
    a = GIAPIClient.get_test_suites()
    basic_payload_validation_tests(a)
    
def test_get_test_suite(GIAPIClient):
    a = GIAPIClient.get_test_suite("Ghost Inspector")
    failure_payload_validation_tests(a)
    
def test_get_tests_failure(GIAPIClient):
    a = GIAPIClient.get_test_suites()
    basic_payload_validation_tests(a)
    

###TESTS_RESULTS

def test_get_suite_results_by_results_id(GIAPIClient):
    a = GIAPIClient.get_suite_results_by_results_id("noid")
    
    failure_payload_validation_tests(a)

def test_get_results_suite_results_by_results_id(GIAPIClient):
    a = GIAPIClient.get_suite_results_by_results_id("noid")
    
    failure_payload_validation_tests(a)

def test_cancel_suite_results_by_results_id(GIAPIClient):
    a = GIAPIClient.cancel_suite_results_by_results_id("noid")
    
    failure_payload_validation_tests(a)


def test_get_suite_results_by_suite_id(GIAPIClient):
    a = GIAPIClient.get_suite_results_by_suite_id("noid")
    
    failure_payload_validation_tests(a)


def test_get_test_results_by_id(GIAPIClient):
    a = GIAPIClient.get_test_results_by_id("noid")
    
    failure_payload_validation_tests(a)


def test_get_results_id(GIAPIClient):
    a = GIAPIClient.get_results_id("noid")
    
    failure_payload_validation_tests(a)


def test_cancel_results_id(GIAPIClient):
    a = GIAPIClient.cancel_results_id("noid")
    
    failure_payload_validation_tests(a)


def test_generate_report(GIAPIClient):
    assert(True)

