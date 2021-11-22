*** Settings ***
Library    SeleniumLibrary
Resource    ../元素定位层/首页_元素定位.robot  


*** Keywords ***
用户昵称元素是否存在
    ${status}=    Run Keyword And Return Status    Wait Until Element Is Visible    ${用户昵称}    15
    [Return]    ${status} 
    
点击抢投标按钮
    Wait Until Element Is Visible    ${抢投标按钮}    20
    Click Element    ${抢投标按钮}      
    