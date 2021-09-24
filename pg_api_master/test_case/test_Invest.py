# _*_coding: utf-8 _*_
# @Time     :2019/5/28  17:03
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :test_Invest.py
import unittest
from test_common.do_mysql import DoMysql
from ddt import ddt, data
from test_common.get_data import GetData
from test_common.http_request import HttpRequests
from test_common.my_log import Mylog
from test_common import project_path
from test_common.do_excel import DoExcel
# 测试充值
test_data = DoExcel(project_path.case_path, 'invest').read_excel('INVESTCASE')
My_log = Mylog()
@ddt
class TestCase(unittest.TestCase):
    def setUp(self):
        self.T = DoExcel(project_path.case_path, 'invest')

    def tearDown(self):
        pass

    @data(*test_data)
    def test_case(self, case):
        global TestResult
        url = case['Url']
        method = case['Method']
        param = eval(case['Params'])
        # if case['Params'].find('loanid') != -1:
        #     param = eval(case['Params'].replace('loanid', str(getattr(GetData, 'LOAN_ID'))))
        # else:
        #     param = eval(case['Params'])
        My_log.info('---------正在测试{}模块里的第{}条测试用例{}'.format(case['Module'], case['CaseId'], case['Title']))
        My_log.info('测试数据是{}'.format(case))
        # 投标前的账户金额查询
        if case['sql'] != None:
            before_amount = int(DoMysql().do_mysql(eval(case['sql'])['sql'], 1)[0])
            print('投资前金额{}'.format(before_amount))
        resp = HttpRequests().http_request(method, url, param, cookies=getattr(GetData, 'COOKIE'))

        if resp.cookies:
            setattr(GetData, 'COOKIE', resp.cookies)# 发送
        try:
            self.assertEqual(eval(case['ExpectedResult']), resp.json())
            # 投标后账户金额查询
            if case['sql'] != None:
                after_amount = int(DoMysql().do_mysql(eval(case['sql'])['sql'], 1)[0])
                print('投资后金额{}'.format(after_amount))
                invest_amount = int(param['amount'])
                print('投资金额{}'.format(invest_amount))
                ecpect_amount = before_amount - invest_amount
                print('投资后预期金额{}'.format(ecpect_amount))
                self.assertEqual(after_amount, ecpect_amount)

            TestResult = 'pass'
        except AssertionError as e:
            TestResult = 'failed'
            My_log.error('测试中出现错误{}'.format(e))
            raise e
        finally:
            self.T.write_back(case['CaseId']+1, 9, resp.text)
            self.T.write_back(case['CaseId']+1, 10, TestResult)
            My_log.info('测试结果是{}'.format(TestResult))



