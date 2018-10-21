#!usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import os, time
import logging

logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
list_path = os.getcwd() +'/testcase'
print(os.getcwd()+'/testcase')
def RunSuite():
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(list_path, pattern='*Test.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
    return testunit

# now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())

