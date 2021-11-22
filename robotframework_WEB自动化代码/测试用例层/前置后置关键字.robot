*** Settings ***
Library    SeleniumLibrary
Resource    ../页面对象层/登陆页面.robot   

*** Keywords ***
登陆系统
    Open Browser    http://120.79.176.157:8012/Index/login.html    chrome
    Maximize Browser Window
    登陆页面.登陆    18684720553    python
    
关闭浏览器
    Close Browser