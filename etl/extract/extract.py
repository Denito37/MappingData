import requests

drinkingFountainsAPIURL = "https://data.cityofnewyork.us/api/v3/views/qnv7-p7a2/query.json"
treesCensusAPIURL = "https://data.cityofnewyork.us/api/v3/views/uvpi-gqnh/query.json"

def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

