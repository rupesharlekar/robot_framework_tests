#### Assignment
Coded Solution for assignment is as below

Task 2              : [test_api_bhagwadgita.robot](https://github.com/rupesharlekar/robot_framework_tests/blob/master/Tests/test_api_bhagwadgita.robot)

Task 2 Alternative  : [test_search.robot](https://github.com/rupesharlekar/robot_framework_tests/blob/master/Tests/test_search.robot) 

#### Project Structure

    ├── Config.py                                       # Config file contains the URL endpoints
    ├── geckodriver.exe									 
    ├── Logs
    │   ├── api
    │   │   └── latest                                  # latest test run files for API tests
    │   └── gui
    │       └── latest                                  # latest test run files for UI tests
    ├── Modules
    │   ├── __init__.py	
    │   ├── api
    │   │   ├── __init__.py
    │   │   └── bhagwadgita_api.py                      # contains all the test for REST API verification
    │   ├── api_util.py                                 # Helper file for REST API verification
    │   ├── gui			
    │   │   ├── __init__.py
    │	│   ├── search_page.py                          # Contains the Verification on first page
    │   │   └── search_result_page.py                   # Contains the Verification on Search Result page
    │   └── util.py                                     # Helper file for UI Verification
    ├── ObjectRepo
    │   ├── obj_search_page.py                          # contains locators for Google Search Main Page
    │   └── obj_search_result_page.py                   # contains locators for Google Search Result Page
    ├── README.md
    ├── requirements.txt			
    ├── Resources
    │   ├── api
    │   │   └── bhagwadgita_resource.robot              # robot resource keyword file for REST API verification
    │   └── gui
    │       ├── search_resource.robot                   # robot resource keyword file for Google Search Main Page
    │       └── search_result_resource.robot            # robot resource keyword file for Google Search Result Page
    ├── Test.pdf
    └── Tests
        ├── test_api_bhagwadgita.robot                  # Test for BhagwadGita REST API
        └── test_search.robot                           # Test for Google Search UI 
        
#### Technology / Frameworks used
- python
- robotframework
- [robotframework-selenium2library](https://github.com/robotframework/Selenium2Library)
- robotframework-pageobjects
- selenium
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- requests

#### Features
- page object patterns for Web UI automation
- layered structure
- also used for REST API automation

#### Installation
`git clone git@github.com:rupesharlekar/robot_framework_tests.git  && cd robot_framework_tests`  
`pip install -r requirements.txt`

#### How to run tests
###### Task2 - API Tests
`robot -d Logs\api\latest Tests\test_api_bhagwadgita.robot`

###### Task2 Alternative - UI Tests 
`robot -d Logs\gui\latest -vbaseurl:https://www.google.com -vbrowser:ff Tests\test_search.robot`

#### Execution Logs
###### Task2 - API Tests
![Alt text](https://github.com/rupesharlekar/robot_framework_tests/blob/master/Logs/api/latest/TestAPI.JPG?raw=true "Optional")

###### Task2 Alternative - UI Tests
![Alt text](https://github.com/rupesharlekar/robot_framework_tests/blob/master/Logs/gui/latest/Test_Search.JPG?raw=true "Optional")