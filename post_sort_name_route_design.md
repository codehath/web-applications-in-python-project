# POST /sort-names Route Design Recipe

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# Request:
POST /sort-names

# With body parameters:
names=Joe,Alice,Zoe,Julia,Kieran

# Expected response (sorted list of names):
Alice,Joe,Julia,Kieran,Zoe

### Route Signature - POST sort-names route
POST /sort-names
    names: string
```

## 2. Create Examples as Tests

```python
# POST "names=Alice" /sort-names
#  Expected response (200 OK):
"""
Alice
"""

# POST "names=Joe,Alice,Julia" /sort-names
#  Expected response (200 OK):
"""
Alice,Joe,Julia
"""

# POST "names=Joe,Alice,Zoe,Julia,Kieran" /sort-names
#  Expected response (200 OK):
"""
Alice,Joe,Julia,Kieran,Zoe
"""
# POST /sort-names
#  Expected response (400 Bad Request):
"""
Please provide names!
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

```python
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
    assert response.data.decode('utf-8') == "Please provide names!"
```

---
