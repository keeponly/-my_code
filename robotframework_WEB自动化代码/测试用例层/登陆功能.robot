*** Settings ***
Library    SeleniumLibrary
Resource    ../页面对象层/登陆页面.robot
Resource    ../页面对象层/首页.robot
#前置 #测试数据   
Suite Setup    Open Browser    http://120.79.176.157:8012/Index/login.html    chrome    
Suite Teardown    Close Browser
Test Teardown    Reload Page

Force Tags    login    

*** Test Cases ***
用例1-异常用例-用户名为空
    [Tags]    demo
        #步骤
    登陆页面.登陆    ${EMPTY}    python
    #断言
    ${errorMsg}=    登陆页面.获取页面错误提示-登陆表单区域
    Should Be Equal As Strings    ${errorMsg}    请输入手机号

用例2-异常用例-密码不正确    
    #步骤
    登陆页面.登陆    18684720553    python111
    ${errorMsg}=    登陆页面.获取错误提示-从页面正中间
    Should Be Equal As Strings    ${errorMsg}    帐号或密码错误!
    
用例3-正常用例-登陆成功
    [Tags]    smoke
    #步骤
    登陆页面.登陆    18684720553    python
    #断言
    ${status}=    首页.用户昵称元素是否存在
    Should Be True    ${status}  
    
用例4-使用pybot命令当中的变量
    [Tags]    demo1
    Log    ${testEnv}    
    
    
用例5-铁定要失败的用例
    [Tags]    demo1
    Should Be Equal As Integers    10    20     
    
    