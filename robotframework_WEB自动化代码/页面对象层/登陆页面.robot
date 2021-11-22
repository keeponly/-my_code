*** Settings ***
Library    SeleniumLibrary
Resource    ../元素定位层/登陆页面_元素定位.robot   


*** Keywords ***
登陆
    [Arguments]    ${user}    ${passwd}
    Wait Until Element Is Visible    ${用户名输入框}    20
    Input Text    ${用户名输入框}    ${user}
    Input Text    ${密码输入框}    ${passwd}
    Click Element    ${登录按钮} 
    
获取页面错误提示-登陆表单区域
    [Return]    ${errorMsg}   
    ${errorMsg}=    Get Text    ${错误提示-登陆表单区域}
    
获取错误提示-从页面正中间
     ${errorMsg}=    Get Text    ${页面正中间的提示框}
     [Return]    ${errorMsg}
    