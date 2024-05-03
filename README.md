# Python BDD Automation Framework
* Note:
This is a basic automation framework that can be expanded upon as needed. It provides a solid foundation for building comprehensive test suites using Behave and Allure.

## Prerequisites:
### This automation framework requires the following tools:

* Python 3.9 or above: Download and install Python from https://www.python.org/downloads/.
* Behave: A behavior-driven development (BDD) framework for Python. Install using pip install behave.
* Allure: A reporting framework for generating comprehensive test reports. Install using pip install allure-behave.

### Install:
```Bash
pip install -r requirements.txt
``` 
### Running Tests:
To execute the example test, use the following command:

```Bash
behave -D browser=firefox -D options=--headless tests/features/open_website.feature
``` 

### Explanation:
#### Specifies the browser to use:
```Bash
-D browser=firefox 
``` 
 Supported browsers include firefox, chrome, opera, and edge. Default is firefox.

#### Specify options capabilities:
```Bash
-D option=--headless
``` 
```Bash
-D option=--option1, --option2, optionN...
``` 

#### Path to the features:
```Bash
tests/features/open_website.feature
 ``` 
Path to the feature/s file/s containing the test scenario.

## Reporting
### Allure Reports:

The framework generates Allure reports in the allure.output directory. To view these reports, run the following command:

```Bash
allure serve allure-results
 ``` 
This will open a web browser with the generated Allure report.

### JUnit Reports:

The framework also generates JUnit reports in the reports directory. These reports are compatible with Jenkins and other CI/CD tools.

* Note:
This is a basic automation framework that can be expanded upon as needed. It provides a solid foundation for building comprehensive test suites using Behave and Allure.

#### Additional Resources:
* Behave documentation: https://behave.readthedocs.io/
* Allure documentation: https://github.com/allure-framework
* Python documentation: https://www.python.org/
