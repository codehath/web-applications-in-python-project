# Tests for your routes go here

# """
# When: I make a GET request to /
# Then: I should get a 200 response
# """
# def test_get_wave(web_client):
#     # We'll simulate sending a GET request to /wave?name=Dana
#     # This returns a response object we can test against.
#     response = web_client.get('/wave?name=Dana')

#     # Assert that the status code was 200 (OK)
#     assert response.status_code == 200

#     # Assert that the data returned was the right string
#     assert response.data.decode('utf-8') == 'I am waving at Dana'

# """
# When: I make a POST request to /submit
# And: I send a name and message as body parameters
# Then: I should get a 200 response with the right content
# """
# def test_post_submit(web_client):
#     # We'll simulate sending a POST request to /submit with a name and message
#     # This returns a response object we can test against.
#     response = web_client.post('/submit', data={'name': 'Dana', 'message': 'Hello'})

#     # Assert that the status code was 200 (OK)
#     assert response.status_code == 200

#     # Assert that the data returned was the right string
#     assert response.data.decode('utf-8') == 'Thanks Dana, you sent this message: "Hello"'

# # To run these tests:
# # ; pipenv shell
# # ; pytest tests/test_app.py

# /count_vowels route tests
"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'


# /sort_names route tests
"""
POST /sort-names
    Parameters:
        names: Alice
    Expected response (200 OK):
        "Alice"
"""
def test_post_sort_names_one_name(web_client):
    response = web_client.post('/sort-names', data={'names': "Alice"})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Alice"

"""
POST /sort-names
    Parameters:
        names: Joe,Alice,Julia
    Expected response (200 OK):
        "Alice,Joe,Julia"
"""
def test_post_sort_names_three_unordered_names(web_client):
    response = web_client.post('/sort-names', data={'names': "Joe,Alice,Julia"})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Alice,Joe,Julia"

"""
POST /sort-names
    Parameters:
        names: Joe,Alice,Zoe,Julia,Kieran
    Expected response (200 OK):
        "Alice,Joe,Julia,Kieran,Zoe"
"""
def test_post_sort_names_five_unordered_names(web_client):
    response = web_client.post('/sort-names', data={'names': "Joe,Alice,Zoe,Julia,Kieran"})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Alice,Joe,Julia,Kieran,Zoe"

"""
POST /sort-names
    Expected response ((400 Bad Request)):
        "Please provide names!"
"""
def test_post_sort_names_no_names(web_client):
    response = web_client.post('/sort-names')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "Bad Request - Please provide names!"