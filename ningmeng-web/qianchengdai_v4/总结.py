#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:muji
# datetime:2019/5/13 20:08


# 为什么要使用 pytest
# mark. 随机运行某一些测试用例，冒烟，
# mark,可以放到方法,也可以放到类上面。
# 一个方法和类上面，可以有多个标签。
# 注意1：mark 表达式 一定要用 双引号。
# 注意2：

# 缓存文件： .pyc .pyd .pyo
# 缓存文件夹 cache

# 2. 跳过函数

# 3. 自动化发现测试
# 4. 断言很方便 assert
# 5. 非常多插件。重运行，allure 测试报告
# 6、 unittest
# 7、fixture 环境管理非常灵活。


# 怎么知道我这个是测试用例呢？

# demo_  发现测试用例的规则可以改吗？ 可以改。

def find_test():
    # 文件名 以 a = test 开头：pass
    # 在全局保存一个变量 配置文件的形式。
    # 改配置文件  课后练习。
    pass


# pytest 的参数化： ddt

#@pytest.mark.parametrize('data', user_info_error)
# 不能和 unittest 同时使用


# fixture 测试环境

# yield  和 return 的作用类似


# 作用域，函数，类，模块，会话。

