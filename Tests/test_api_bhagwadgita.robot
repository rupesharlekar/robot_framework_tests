*** Settings ***
Documentation       This test suite contains following test cases:
...                 1.

Resource    ../Resources/api/bhagwadgita_resource.robot

Suite Setup         SuiteSetup
Suite Teardown      SuiteTeardown

*** Variables ***

*** Test Cases ***
Verify total number of chapters and name meaning of sixth chapter
    [Tags]              Smoke
    [Documentation]     chapters in bhagwadgita

    Verify there are total "18" chapters in bhagwad gita
    Verify chapter "6" name meaning is "\"Path of Meditation\""

Verify total number of verses in chapter 6 and starting text for verse 1
    [Tags]              Smoke
    [Documentation]     verses in bhagwadgita

    Verify in chapter "6" there are total "47" verses in bhagwad gita
    Verify verse "1" of chapter "6" starts with "The Blessed Lord said"

*** Keywords ***
SuiteSetup
    API is authenticated for CLIENT_ID and CLIENT_SECRET

SuiteTeardown
    BuiltIn.Log  Suite Setup Section
