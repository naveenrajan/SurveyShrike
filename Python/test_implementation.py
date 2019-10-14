from behave import given, when, then, step
import requests

api_endpoints = {}
request_headers = {}
response_codes ={}
response_texts={}
request_bodies = {}
api_url=None

@given(u'I set sample REST API url')
def step_impl(context):
    global api_url
    api_url = 'http://jsonplaceholder.typicode.com'

# START POST Scenario
@given(u'I Set POST posts api endpoint')
def step_impl(context):
    api_endpoints['POST_URL'] = api_url+'/posts'
    print('url :'+api_endpoints['POST_URL'])

@when(u'I Set HEADER param request content type as "{header_conent_type}"')
def step_impl(context, header_conent_type):
    request_headers['Content-Type'] = header_conent_type

#You may also include "And" or "But" as a step - these are renamed by behave to take the name of their preceding step, so:
@when(u'Set request Body')
def step_impl(context):
    request_bodies['POST']={"title": "foo","body": "bar","userId": "1"}

#You may also include "And" or "But" as a step - these are renamed by behave to take the name of their preceding step, so:
@when(u'Send POST HTTP request')
def step_impl(context):
    # sending get request and saving response as response object
    response = requests.post(url=api_endpoints['POST_URL'], json=request_bodies['POST'], headers=request_headers)
    #response = requests.post(url=api_endpoints['POST_URL'], headers=request_headers) #https://jsonplaceholder.typicode.com/posts
    # extracting response text
    response_texts['POST']=response.text
    print("post response :"+response.text)
    # extracting response status_code
    statuscode = response.status_code
    response_codes['POST'] = statuscode

@then(u'I receive valid HTTP response code 201')
def step_impl(context):
    print('Post rep code ;'+str(response_codes['POST']))
    assert response_codes['POST'] is 201
# END POST Scenario

# START GET Scenario
@given(u'I Set GET posts api endpoint "{id}"')
def step_impl(context,id):
    api_endpoints['GET_URL'] = api_url+'/posts/'+id
    print('url :'+api_endpoints['GET_URL'])

#You may also include "And" or "But" as a step - these are renamed by behave to take the name of their preceding step, so:
@when(u'Send GET HTTP request')
def step_impl(context):
    # sending get request and saving response as response object
    response = requests.get(url=api_endpoints['GET_URL'], headers=request_headers) #https://jsonplaceholder.typicode.com/posts
    # extracting response text
    response_texts['GET']=response.text
    # extracting response status_code
    statuscode = response.status_code
    response_codes['GET'] = statuscode

@then(u'I receive valid HTTP response code 200 for "{request_name}"')
def step_impl(context,request_name):
    print('Get rep code for '+request_name+':'+ str(response_codes[request_name]))
    assert response_codes[request_name] is 200

@then(u'Response BODY "{request_name}" is non-empty')
def step_impl(context,request_name):
    print('request_name: '+request_name)
    print(response_texts)
    assert response_texts[request_name] is not None
# END GET Scenario

#START PUT/UPDATE
@given(u'I Set PUT posts api endpoint for "{id}"')
def step_impl(context,id):
    api_endpoints['PUT_URL'] = api_url + '/posts/'+id
    print('url :' + api_endpoints['PUT_URL'])

@when(u'I Set Update request Body')
def step_impl(context):
    request_bodies['PUT']={"title": "foo","body": "bar","userId": "1","id": "1"}

@when(u'Send PUT HTTP request')
def step_impl(context):
    # sending get request and saving response as response object  # response = requests.post(url=api_endpoints['POST_URL'], headers=request_headers) #https://jsonplaceholder.typicode.com/posts
    response = requests.put(url=api_endpoints['PUT_URL'], json=request_bodies['PUT'], headers=request_headers)
    # extracting response text
    response_texts['PUT'] = response.text
    print("update response :" + response.text)
    # extracting response status_code
    statuscode = response.status_code
    response_codes['PUT'] = statuscode
#END PUT/UPDATE

#START DELETE
@given(u'I Set DELETE posts api endpoint for "{id}"')
def step_impl(context,id):
    api_endpoints['DELETE_URL'] = api_url + '/posts/'+id
    print('url :' + api_endpoints['DELETE_URL'])

@when(u'I Send DELETE HTTP request')
def step_impl(context):
    # sending get request and saving response as response object
    response = requests.delete(url=api_endpoints['DELETE_URL'])
    # response = requests.post(url=api_endpoints['POST_URL'], headers=request_headers) #https://jsonplaceholder.typicode.com/posts
    # extracting response text
    response_texts['DELETE'] = response.text
    print("DELETE response :" + response.text)
    # extracting response status_code
    statuscode = response.status_code
    response_codes['DELETE'] = statuscode
#END DELETE
