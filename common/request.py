#!usr/bin/python
# -*- coding: UTF-8 -*-

import requests
from common.ParseCSV import ParseCSV
import logging



class request:
    '''
    package requests
    '''
    def post_req(self, name, data):
        try:
            headers = {"Content-Type": "application/octet-stream"}
            api_data = ParseCSV('../data/api.csv').readCSV()
            url = api_data[0][0]
            logging.info("test start...")
            logging.info(name)
            response = requests.post(url, data = data, headers = headers, verify=False)
            logging.info("test end...")
            return response
        except Exception as e:
            return e
    

    
    