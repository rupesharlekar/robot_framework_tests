#### Assignment
Task 2 and Task 3 in  
 
#### Technology / Frameworks used
- python
- robotframework
- [robotframework-selenium2library](https://github.com/robotframework/Selenium2Library)
- robotframework-pageobjects
- selenium
- [beautifulsoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

#### Features
- page object patterns
- layered structure
- can be used for [rest api](https://github.com/bulkan/robotframework-requests) automation

#### Installation
`git clone git@github.com:rupesharlekar/robot_framework_tests.git  && cd robot_framework_tests`  
`pip install -r requirements.txt`

#### How to run tests
`robot -d Logs\latest -vbaseurl:https://www.google.com -vbrowser:ff Tests\test_search.robot`
