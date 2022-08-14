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


# func - get the number of password leaks from the responses that match the first 5 characters
# param1 - list of response hashes matching first 5 characters
# param2 - my hashed password
def password_leaks_count(response_hashes, my_password_hash):
    response_hashes = (each_hash.split(':') for each_hash in response_hashes.text.splitlines())
    for res_hash, count in response_hashes:
        if res_hash == my_password_hash:
            return count
        return 0


# func - checks existence of password in API response using sha1 algo
# param - our actual password
# response - all the hashed passwords that match the first 5 characters of my password
def pwned_api_response_check(my_password):
    sha1pass = hashlib.sha1(my_password.encode('utf-8')).hexdigest().upper()
    first5char = sha1pass[:5]
    tail = sha1pass[5:]
    response = request_api_data(first5char)
    print(first5char, tail)
    print(response)
    return password_leaks_count(response, tail)


pwned_api_response_check('123')
