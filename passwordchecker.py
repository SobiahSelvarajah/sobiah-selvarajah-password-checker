import requests
import hashlib


# func - requesting data from the API url
# param - hashed version of password
def request_api_data(query):
    url = 'https://api.pwnedpasswords.com/range/' + query
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and please try again.')
    return res


def read_response(response):
    print(response.text)


# func - checks existence of password in API response using sha1 algo
# param - our actual password
# response - all the hashed passwords that match the first 5 characters of my password
def pwned_api_response_check(password):
    sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5char = sha1pass[:5]
    tail = sha1pass[5:]
    response = request_api_data(first5char)
    print(first5char, tail)
    print(response)
    return read_response(response)


pwned_api_response_check('123')
