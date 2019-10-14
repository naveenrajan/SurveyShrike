# SurveyShrike Survey Form Generator
This application is buit using the followin tech stack:

  1) HTML,CSS, Java Sript - Front End
  2) Python 3.7.2 - Back End
  3) Oracle Exadata - Database
  4) Oath2.0 - Authentication protocol
  5) Behave & Allure test framework for Python tests
  
The purpose of the application is to help any authenticated user to perform the following operations :

___

> **Create/Design an online survey form.**

> **Take any survey desired by the user.**

> **View the results of the survey.**

> **View any survey created by the user.**

___

An authenticated admin user can create a form using the following options:

  1) Single Line Input
  2) Multi Line Input
  3) Radio Buttons with any number of options
  4) Checkbox with any number of optiosn
  5) Dropdown with any number of options
  6) Bool
  7) File upload
  8) Dynamic Matrix
  9) HTMl embed
  10) Image Picker
  11) Panel
  12) Comment
  13) Ratings
  14) Mathematical expressions (supporting supercript)
  
  Note : Option numbers 1-5 are currently supported , however all other options are already on your way...
  
  ___
  
# Workflow:

# Page-1: Login

The user authentication is done using the secure OAuth2.0 protocol which uses the Okta which helps any application to onboard to Oauth2.

# Page-2 : Options

The page lets users to select from the options such as Create, View and Take survey.

# Page 3 : Create

The page lets user to create an online survey.

Step-1: Click on Single line, Multi line, Dropdown. radio button and checkbox buttons in order.

Step-2: The user needs to provide the survey name, survey creator name, the questions selected in step-1, its corresponding option description and click on Submit button.

Once submitted the details will be saved on the Back-end storage layer.

# Page-4: View

This page lets user to :

  1) View the already created survey forms.
  2) View the results of the survey

# Page-5 : View results

In this page, an admin user can see the results of the survey with details such as: 
  
  1) Result ID column
  2) Survey Taken By-Name of the person
  3) Survey Taken On - Time of submission of the survey
  4) The questions attempted by the user taken the survey
  5) The options submitted for the respective questions by the users.
  
 # Testing Framework written using Behave & Allure
 
 Behave framework identifies the Step function by decorators matching with feature file predicate. For Example, Given predicate in Feature file Scenario searches for step function having decorator "given." Similar matching happens for When and Then. But in the case of 'But,' 'And,' Step function takes decorator same as it's preceding step. For Example, If 'And' comes for Given, matching step function decorator is @given.
 
 > Execute the following command on command prompt to run our feature file :
 
> C: \Programs\Python\Python37>behave -f pretty C:\<your projectpath>\ features \feature_files_folder \ Sample_REST_API_Testing.feature 
 
 
