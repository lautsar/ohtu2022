*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  uusi  kayttaja12
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  salasana123
    Output Should Contain  Username already in use

Register With Too Short Username And Valid Password
    Input Credentials  ab  salasana123
    Output Should Contain  Username too short

Register With Valid Username And Too Short Password
    Input Credentials  matti  salis
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  matti  salasalasana
    Output Should Contain  Invalid password

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123
