Feature: Test CRUD methods in Sample REST API testing framework

Background:
	Given I set sample REST API url

Scenario: POST post example
  Given I Set POST posts api endpoint
 When I Set HEADER param request content type as "application/json." 
    And Set request Body
 And Send a POST HTTP request 
 Then I receive valid HTTP response code 201
    And Response BODY "POST" is non-empty. 


Scenario: GET posts example
  Given I Set GET posts api endpoint "1"
  When I Set HEADER param request content type as "application/json." 
	And Send GET HTTP request
  Then I receive valid HTTP response code 200 for "GET." 
	And Response BODY "GET" is non-empty


Scenario: UPDATE posts example
  Given I Set PUT posts api endpoint for "1"
  When I Set Update request Body
	And Send PUT HTTP request
  Then I receive valid HTTP response code 200 for "PUT." 
	And Response BODY "PUT" is non-empty


Scenario: DELETE posts example
  Given I Set DELETE posts api endpoint for "1"
  When I Send DELETE HTTP request
  Then I receive valid HTTP response code 200 for "DELETE." 
