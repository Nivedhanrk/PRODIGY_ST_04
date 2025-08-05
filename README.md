# Task 04 - Cross-Browser Testing using BrowserStack

**Internship Track:** Software Testing  
**Intern Name:** Nivedhan  
**Website Tested:** https://www.saucedemo.com/

## Objective:
To run automated login tests across multiple browsers and operating systems using BrowserStack’s Selenium Grid and report the consistency and issues across environments.

 Tools Used:
- Selenium (Python)
- BrowserStack Cloud Platform
- Remote WebDriver

Browsers/OS Tested:
- Chrome on Windows 10
- Edge on Windows 10
- Safari on macOS Ventura
- Firefox on Windows

 Summary:
We tested the login functionality using valid credentials on different browser environments. BrowserStack helped simulate real user conditions without requiring manual setup for each OS/browser.

Test Results:

| Test Case ID | Browser & OS | Observed Behavior | Expected Behavior | Result |
|--------------|--------------|-------------------|-------------------|--------|
| TC-401 | Chrome on Windows 10 | Login passed | Should login successfully | ✅ Pass |
| TC-402 | Edge on Windows 10 | Login passed | Should login successfully | ✅ Pass |
| TC-403 | Safari on macOS | Login passed after slight delay | Should login successfully | ⚠️ Pass |
| TC-404 | Firefox on Windows | Login passed | Should login successfully | ✅ Pass |

Script File:
`browserstack_login_test.py`

Make sure to replace your BrowserStack Username and Access Key in the script before running.
