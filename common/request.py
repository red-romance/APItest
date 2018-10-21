#!usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from common.ParseCSV import ParseCSV
import logging
import os


class request:
    """
    package requests
    """
    def pull_post(self, name, data):
        try:
            headers = {"Content-Type": "application/octet-stream"}
            api_data = ParseCSV(os.getcwd() +'/data/api.csv').readCSV()
            url = api_data[0][0]
            logging.info("test start...")
            logging.info(name)
            print(data)
            response = requests.post(url, data = data, headers = headers, verify=False)
            logging.info("test end...")
            return response
        except Exception as e:
            return e
    
    
    def push_post(self, name, data):
        try:
            headers = {"Content-Type": "application/octet-stream"}
            api_data = ParseCSV(os.getcwd() +'/data/api.csv').readCSV()
            url = api_data[1][0]
            logging.info("test start...")
            logging.info(name)
            response = requests.post(url, data = data, headers = headers, verify=False)
            logging.info("test end...")
            return response
        except Exception as e:
            return e
    
    
    