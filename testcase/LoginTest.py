#!usr/bin/python
# -*- coding: UTF-8 -*-

import unittest
import os
from interface.Login import Login
from common.request import request
from common.ParseCSV import ParseCSV
from Parameterized import parameterized


class Test(unittest.TestCase):
	
	@parameterized.expend([
	("aa", "qwe", "登录成功")
	])
    def test_01(self, name, pwd, assert_text):

		data = Login.login_phone(self, name, pwd)
		response = request.pull_post(self, data)

		#analyze the response for add assert
		req_result = Login.login_analyse(self, response)
		
		#add assert
		n = int(assert_text)
		self.assertEqual(n, req_result)
            

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()