#### Assignment
Coded Solution for assignment is as below

Task 2              : [test_api_bhagwadgita.robot](https://github.com/rupesharlekar/robot_framework_tests/blob/master/Tests/test_api_bhagwadgita.robot)

Task 2 Alternative  : [test_search.robot](https://github.com/rupesharlekar/robot_framework_tests/blob/master/Tests/test_search.robot) 
 
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
