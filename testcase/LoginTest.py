#!usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import os
from interface.Login import Login
from common.request import request
from common.ParseCSV import ParseCSV


class Test(unittest.TestCase):

    
    def test_01(self):

        login_data = ParseCSV(os.getcwd() +'/data/login.csv').readCSV()
        print(login_data)

        for i in range(len(login_data)):

            data = 0
            if login_data[i][1].lower() == "phone":
                data = Login.login_phone(self, login_data[i][2], login_data[i][3])
            response = request.pull_post(self, login_data[i], data)

            #analyze the response for add assert
            req_result = Login.login_analyse(self, response)
            
            #add assert
            n = int(login_data[i][4])
            self.assertEqual(n, req_result)
            

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()