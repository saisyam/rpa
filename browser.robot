*** Settings ***
Library     DebugLibrary
Library    ./RPALib/Browser.py

*** Test Cases ***
Test webpage title
    Open Chrome Browser Headless
    Open Url            https://saisyam.com
    Check If Title Is   Saisyam: Developer - Photographer - Foodie
    Close Browser

Query Google for Saisyam
    Open Chrome Browser
    Open Url            https://google.com
    Input Text          q   saisyam
    Click Button        name:btnK
    Is Text Present     saisyam.com
    Close Browser

Select Mobiles Category in Amazon
    Open Chrome Browser
    Open Url            https://amazon.in
    Click Button        id:nav-hamburger-menu
    Click Item By Text  Mobiles, Computers
    Click Item By Text  All Mobile Phones
    Is Text Present     Mobiles & Accessories
    Close Browser