*** Settings ***
Library     DebugLibrary
Library    ./RPALib/Browser.py

*** Test Cases ***

Filter Mobiles By Samsung in Amazon
    Open Chrome Browser
    Open Url            https://amazon.in
    Click               id:nav-hamburger-menu
    Click               text:Mobiles, Computers
    Click               text:All Mobile Phones
    Check Item          s-ref-checkbox-Samsung
    Is Text Present     Mobiles & Accessories : Samsung
    Close Browser
    
Test webpage title
    Open Firefox Browser Headless
    Open Url            https://saisyam.com
    Check If Title Is   Saisyam: Developer - Photographer - Foodie
    Close Browser

Query Google for Saisyam
    Open Chrome Browser Incognito
    Open Url            https://google.com
    Input Text          name:q   saisyam
    Click               name:btnK
    Is Text Present     saisyam.com
    Close Browser

Select Mobiles Category in Amazon
    Open Chrome Browser Headless Incognito
    Open Url            https://amazon.in
    Click               id:nav-hamburger-menu
    Click               text:Mobiles, Computers
    Click               text:All Mobile Phones
    Is Text Present     Mobiles & Accessories
    Close Browser