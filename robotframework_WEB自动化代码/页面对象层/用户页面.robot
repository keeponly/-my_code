*** Settings ***
Library    SeleniumLibrary   
Library    String     
Resource    ../元素定位层/用户页面_元素定位.robot

*** Keywords ***
获取用户余额
    Wait Until Element Is Visible    ${可用余额}    20
    ${temp}=    Get Text    ${可用余额}
    ${money}=    Strip String    ${temp}    元
    [Return]    ${money}