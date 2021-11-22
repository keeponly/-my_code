# _*_coding: utf-8 _*_
# @Time     :2019/5/24  10:32
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :test_add_loan.py
# 引入单元测试
import unittest
import pymysql
from zl_api.test_common.http_request import HttpRequests
from zl_api.test_common.do_excel import DoExcel
from zl_api.test_common import project_path
from ddt import ddt, data
from zl_api.test_common.my_log import Mylog
from zl_api.test_common.get_data import GetData
from zl_api.test_common.do_mysql import DoMysql
from zl_api.test_case.test_login import token

from zl_api.test_common.get_token import get_token

test_data = DoExcel(project_path.case_path, 'create_getGroupAndUserTree').read_excel('getGroupAndUserTree')
My_log = Mylog()
token = None
@ddt
class TestCase(unittest.TestCase):
    def setUp(self):
        self.T = DoExcel(project_path.case_path, 'create_getGroupAndUserTree')

    def tearDown(self):
        pass

    @data(*test_data)

    def test_case(self, case):
        global TestResult  # 全局变量
        #global token
        # 执行测试
        method = case['Method']
        url = case['Url']
        # if case['Params'].find('loanid') != -1:   # param里面发现loanid
        #     param = eval(case['Params'].replace('loanid', str(getattr(GetData, 'LOAN_ID'))))  # 将param里loanid替换
        # else:
        param = eval(case['Params'])
        print(type(param))
        print(param)
        headers= dict(token=get_token())
        print(headers)
    # 发起测试
        # res = HttpRequests().http_request(method,url,param,headers,verify=False)
        My_log.info('------正在测试{}模块里的第{}条测试用例：{}'.format(case['Module'], case['CaseId'], case['Title']))
        My_log.info('测试数据是{}'.format(case))
        resp = HttpRequests().http_request(method, url, param,headers,verify=False)
        print(resp.json())
        # if case['sql']!=None:
        #     loan_id = DoMysql().do_mysql(eval(case['sql'])['sql'], 1)  # 从大的case字典里取出sql的字典，并通过键值对取出sql查询语句
        #     setattr(GetData, 'LOAN_ID', loan_id[0])
        #data = resp.json()
        # if (data['token']):  # 判断cookies是否为空
        #      setattr(GetData, 'token', data["token"])
        message = resp.json()["code"]
        print(message)
        # print(type(message))
        try:
            print(type(case['ExpectedResult']))
            self.assertEqual(str(case['ExpectedResult']), str(message))
            TestResult = 'pass'
        except AssertionError as e:
            TestResult = 'failed'
            My_log.error('测试执行过程中出错，错误是:{}'.format(e))
            raise e
        finally:
            # 写回结果
            self.T.write_back(case['CaseId'] + 1, 9, resp.text)
            self.T.write_back(case['CaseId'] + 1, 10, TestResult)
        My_log.info('测试结果是：{}'.format(TestResult))  # http发送请求拿回的实际结果
