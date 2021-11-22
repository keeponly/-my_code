# _*_coding: utf-8 _*_
# @Time     :2019/5/17  16:18
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :case_suite.py

import sys
sys.path.append('./')
import unittest
import HTMLTestRunnerNew
from test_common import project_path
# from test_case.test_register import TestCase
#from test_case.test_recharge import TestCase
from test_case.test_login import TestCase

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestCase))
with open(project_path.report_path, 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity=2,
                                              title='蘑菇云自动化测试报告',
                                              description='蘑菇云自动化测试报告',
                                              tester='huididi')
    runner.run(suite)
