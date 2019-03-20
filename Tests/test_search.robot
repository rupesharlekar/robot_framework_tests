*** Settings ***
Documentation       This test suite contains following test cases:
...                 1. Search functionality on Google

Library     search_page.SearchPage

Resource    ../Resources/gui/search_resource.robot
Resource    ../Resources/gui/search_result_resource.robot

Suite Setup         SuiteSetup
Suite Teardown      SuiteTeardown

*** Variables ***
${searchthis}   python

*** Test Cases ***
Verify input text yeilds relevant results
    [Tags]              Smoke
    [Documentation]     input text in google and verify results page content

    [Setup]             Open Search Page

    Given Googles main search page displayed
    When Input text "${searchthis}" on main page and click Google Search button
    Then Verify non zero numbers of results are displayed for ${searchthis}
         Verify description section of all the results displayed contains searched text "${searchthis}" atleast once

    [Teardown]          Close Browser

Verify auto suggestion is shown for input text and upon selection it yields relevant results
    [Tags]              Smoke
    [Documentation]     auto suggestion shown with input text as prefix and verify results page content

    [Setup]             Open Search Page

    Given Googles main search page displayed
    When Search input text "${searchthis}" with auto suggestions and click "1" th option
    Then Verify non zero numbers of results are displayed for ${searchthis}
         Verify description section of all the results displayed contains searched text "${searchthis}" atleast once

    [Teardown]          Close Browser

*** Keywords ***
SuiteSetup
    BuiltIn.Log  Suite Setup Section

SuiteTeardown
    BuiltIn.Log  Suite Setup Section
