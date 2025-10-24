import requests
import pandas as pd

drinkingFountainsAPIURL = "https://data.cityofnewyork.us/api/v3/views/qnv7-p7a2/query.json"
treesCensusAPIURL = "https://data.cityofnewyork.us/api/v3/views/uvpi-gqnh/query.json"

def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status() 
    data = response.json()
    return data

def extract_drinking_fountains_data():
    data = fetch_data(drinkingFountainsAPIURL)
    return data

def extract_trees_census_data():
    data = fetch_data(treesCensusAPIURL)
    return data


def read_drinking_fountains_data():
    data = extract_drinking_fountains_data()
    fountains = pd.read_json(data)
    print(fountains.head(5))
    print(fountains.info())