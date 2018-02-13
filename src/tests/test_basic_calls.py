#!/usr/bin/env python
"""
Example
"""
import sys
import requests
import os
import pytest
from src.GhostInspector.GIClient import Client


def test_get_tests():
    
    assert(True)

def test_get_test_by_id(GIAPIClient):
    a = GIAPIClient.get_test_by_id("99")
    print(a)
    assert(a != None)

def test_get_test_by_name(GIAPIClient):
    a = GIAPIClient.get_test_by_name("testees")
    print(a)
    assert(a != None)

def test_get_test_results(GIAPIClient):
    a = GIAPIClient.get_test_results_by_id("sd")
    print(a)
    assert(a != None)

def test_get_test_suites(GIAPIClient):
    a = GIAPIClient.get_test_suites()
    print(a)
    assert(a != None)

def test_get_test_details(GIAPIClient):
    a = GIAPIClient.get_test_suites()
    print(a)
    assert(a != None)

def test_get_tests_failure(GIAPIClient):
    a = GIAPIClient.get_test_suites()
    print(a)
    assert(a != None)
    
def test_generate_report(GIAPIClient):
    assert(True)
