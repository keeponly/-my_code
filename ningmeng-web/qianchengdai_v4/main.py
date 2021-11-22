#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:muji
# datetime:2019/5/13 20:59
import pytest

if __name__ == '__main__':
    pytest.main(["-m demo", r"--junitxml=report\test.xml"])