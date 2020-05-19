*** Settings ***
Library     DebugLibrary
Library    ./RPALib/Browser.py

*** Test Cases ***
Test webpage title
    Open Chrome Browser Headless
    Open Url            https://saisyam.com
    Check If Title Is   Saisyam: Developer - Photographer - Foodie
    Close Browser