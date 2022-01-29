*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  uusi
    Set Password  kayttaja123
    Confirm Password  kayttaja123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  aa
    Set Password  kayttaja123
    Confirm Password  kayttaja123
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  uusi2
    Set Password  k123
    Confirm Password  k123
    Submit Credentials
    Register Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  uusi3
    Set Password  kayttaja123
    Confirm Password  kauttaja123
    Submit Credentials
    Register Should Fail With Message  Confirmation does not match

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Confirm Password
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}