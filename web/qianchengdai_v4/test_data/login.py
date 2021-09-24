#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:muji
# datetime:2019/5/8 20:51


# 数据 1. 账号 2. 密码 3、预期 caseid
# 测试用例分组
# 用户分组依据：测试用例方法步骤逻辑是否发生变化。

# 用户成功

user_info_success = {"username": "18684720553", "pwd": "python", "expected": "小蜜蜂96027921"}


user_info_error = [
    {"username": "", "pwd": "", "expected": "请输入手机号"},
    {"username": "12", "pwd": "", "expected": "请输入正确的手机号"},
    {"username": "18654321456", "pwd": "", "expected": "请输入密码"},
]


user_info_authorize = [
    {"username": "18654321456", "pwd": "12", "expected": "此账号没有经过授权，请联系管理员!"}
]

