*** Settings ***
Resource    前置后置关键字.robot
Resource    ../页面对象层/首页.robot
Resource    ../页面对象层/标详情页面.robot
Resource    ../页面对象层/用户页面.robot

Test Setup    登陆系统
Test Teardown    关闭浏览器

*** Test Cases ***
用例1-正常场景-投资成功
    首页.点击抢投标按钮
    ${投资前的用户余额}=    标详情页面.获取用户余额
    标详情页面.投资操作    1000
    标详情页面.投资成功弹出框-点击查看并激活按钮
    ${投资后的用户余额}=    用户页面.获取用户余额
    ${diff}=    Evaluate    ${投资前的用户余额}-${投资后的用户余额}
    Should Be Equal As Integers    ${diff}    1000      
    