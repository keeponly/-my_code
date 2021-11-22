# _*_coding: utf-8 _*_
# @Time     :2019/5/22  20:46
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :test_recharge.py
# 引入单元测试
import unittest
from test_common.http_request import HttpRequests
from test_common.do_excel import DoExcel
from test_common import project_path
from ddt import ddt, data, unpack
from test_common.my_log import Mylog
from test_common.get_data import GetData

# 测试注册
test_data = DoExcel(project_path.case_path, 'register').read_excel('RegisterCASE')
print(test_data)
My_log = Mylog()
@ddt
class TestCase(unittest.TestCase):
    def setUp(self):
        self.T = DoExcel(project_path.case_path, 'register')

    def tearDown(self):
        pass

    @data(*test_data)
    def test_case(self, case):
        global TestResult  # 全局变量
        # 执行测试
        method = case['Method']
        url = case['Url']
        param = eval(case['Params'])
    # 发起测试
        My_log.info('------正在测试{}模块里的第{}条测试用例：{}'.format(case['Module'], case['CaseId'], case['Title']))
        My_log.info('测试数据是{}'.format(case))
        resp = HttpRequests().http_request(method, url, param,None)
        try:
            self.assertEqual(eval(case['ExpectedResult']), resp.json())
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
