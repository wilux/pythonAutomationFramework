# Prerequisites:
## This automation framework requires the following tools:

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
behave -D browser=firefox -D option=--headless tests/features/open_website.feature
``` 

### Explanation:

```Bash
-D browser=firefox 
``` 
Specifies the browser to use. Supported browsers include firefox, chrome, opera, and edge. Default is firefox.
```Bash
-D option=--headless 
``` 
Runs the browser in headless mode (no visible window). Omit this option for a visible browser window.
```Bash
tests/features/open_website.feature
 ``` 
Path to the feature file containing the test scenario.

## Reporting
### Allure Reports:

The framework generates Allure reports in the allure.output directory. To view these reports, run the following command:

```Bash
allure serve allure.output
 ``` 
This will open a web browser with the generated Allure report.

### JUnit Reports:

The framework also generates JUnit reports in the reports directory. These reports are compatible with Jenkins and other CI/CD tools.

Note:
This is a basic automation framework that can be expanded upon as needed. It provides a solid foundation for building comprehensive test suites using Behave and Allure.

Additional Resources:
Behave documentation: https://behave.readthedocs.io/
Allure documentation: https://github.com/allure-framework
Python documentation: https://www.python.org/
