*** Settings ***
Library       Remote    http://127.0.0.1:7080

*** Test Cases ***
Add two items
    ${alist}=     Add     1   2
    Numbers Should Be Equal     ${alist}    4
    
