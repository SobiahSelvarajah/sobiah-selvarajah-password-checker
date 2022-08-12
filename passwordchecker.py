import requests


# func - requesting data from the API url
def request_api_data(query):
    url = 'https://api.pwnedpasswords.com/range/' + query
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and please try again.')
    return res


print(request_api_data('vhs'))
