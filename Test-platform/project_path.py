# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 21:24
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : project_path.py
import os
# 文件的路径 spilt一最后的一个/为分割，最后一个/前的索引为0，后面的为1
project_path = os.path.split(os.path.realpath(__file__))[0]
# print(project_path)
# html的路径
html_path = os.path.join(project_path, 'front-end', 'templates')
# folder 路径
css_path = os.path.join(project_path, 'front-end', 'folder')
