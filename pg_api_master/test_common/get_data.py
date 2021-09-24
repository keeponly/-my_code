# _*_coding: utf-8 _*_
# @Time     :2019/5/23  17:05
# @Author   :wangkai
# @Email    :1063699580@qq.com
# @ File    :get_data.py    
# 反射，可以动态的查看，增加，删除，更改类里面的属性
from test_common import project_path
from test_common.read_config import ReadConfig


class GetData:
    token = None
    #LOAN_ID = None #新增加的标id
    user_phone = ReadConfig(project_path.conf_path).get_str('data', 'user_phone')
    user_pwd = ReadConfig(project_path.conf_path).get_str('data', 'user_pwd')
    user_id = ReadConfig(project_path.conf_path).get_str('data', 'user_id')
# 类属性


# print(GetData.user_id)
print(getattr(GetData, 'token'))
# print(hasattr(GetData, 'COOKIE'))  # 返回布尔值
# print(setattr(GetData, 'COOKIE', '4567'))  # 修改新的数值，没有返回值
# print(getattr(GetData, 'COOKIE'))
# print(delattr(GetData, 'COOKIE'))  # 删除类的属性
# print(getattr(GetData, 'COOKIE'))