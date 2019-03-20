*** Settings ***
Library     search_result_page.SearchResultPage

*** Keywords ***
Verify non zero numbers of results are displayed for ${searched_text}
    verify_results_counts_non_zero      searched_text=${searched_text}

Verify description section of all the results displayed contains searched text "${searched_text}" atleast once
    verify_each_description_contains_searched_text      searched_text=${searched_text}