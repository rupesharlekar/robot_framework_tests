*** Settings ***
Library     search_page.SearchPage

*** Keywords ***
Googles main search page displayed
    verify_google_landing_page

Input text "${search_text}" on main page and click Google Search button
    enter_search_text  search_text=${search_text}
    click_google_search_button

Search input text "${search_text}" with auto suggestions and click "${select_option}" th option
    enter_search_text_scroll_through_suggestion  search_text=${search_text}  select_option=${select_option}