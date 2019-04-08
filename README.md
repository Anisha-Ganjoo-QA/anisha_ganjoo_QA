# Project Title

This project is a Data-Driven Framework using POM(Page Object Model) design pattern which validates the error message when the incorrect password or username is entered.


#Prerequisites/ Installations

The tools and softwares required and used in this project are:
> Eclipse (Version: 2018-09 (4.9.0)) 
> Chromedriver (v2.38)
> Selenium (Version 3.12.0)
> Python 2.7 (Python 3.4+ can also be used)

This was created and tested on an Ubuntu 14.04 Linux system.



#Approach/ Criteria for the framework

This is a generic code which reduces the amount of repititive code and if the user interface changes, the fix needs to be changed at one place only. POM and Page Factory is the best approach for memory utilization, it breaks down the complex and lengthy code in seperate defined classes and packages. These Page Objects encapsulates the finer details of the web pages from the test script to make it more readable and robust.

> Language Used : I have used Python language with Selenium as the team is proficient in Python.

> POM : As per the POM model, I have maintained a class for the web page. We can create seperate classes for each web page for the web elements and the functionality used.

> Packages : AppUtilities : This package holds the methods defined to perform required actions on the web page.
	     PageRepository : This package contains the locators of the particular web page created in a seperate class.
	     TestRunnerClasses : The package has one or two test runner classes used to perform unit test and define test cases.
	     
> JavaScriptExecutor: It is an interface used to run the javascript on that particular window. I have used JavaScriptExecutor to fetch the hidden error message on the webpage. 

> Property File : The property file(config.properties) has the local system configurations and set up required for the project and cannot be hardcoded in the script. It may also contain the login details and database path.

> Drivers : store the .exe(executable) files of the browsers used in the code, locally in the project.


#Author

Anisha Ganjoo - QA Lead
Accenture Solutions Pvt Ltd.
SkypeID : ganjoo.anisha


