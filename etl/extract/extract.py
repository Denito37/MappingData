import requests
import pandas as pd
import geopandas as gpd
import rasterio 
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
limit = 1000
pageNum = 1
drinkingFountainsAPIURL = f"https://data.cityofnewyork.us/api/v3/views/qnv7-p7a2/query.json?page_number={pageNum}&page_size={limit}&app_token={API_TOKEN}"
treesCensusAPIURL = f"https://data.cityofnewyork.us/api/v3/views/uvpi-gqnh/query.json?page_number={pageNum}&page_size={limit}&app_token={API_TOKEN}"
nycTifFile = 'assets/nyc.tif'
def fetch_data(url):
    response = requests.get(url)
    response.raise_for_status() 
    data = response.json()
    return data

def read_drinking_fountains_data():
    data = fetch_data(drinkingFountainsAPIURL)
    dataFrame = gpd.GeoDataFrame(data)
    return dataFrame

def read_tree_census_data():
    data = fetch_data(treesCensusAPIURL)
    dataFrame = pd.DataFrame(data)
    return dataFrame

def open_map(file = nycTifFile):
    nycMap = rasterio.open(file)
    return nycMap

def read_nyc_map(file = nycTifFile):
    with rasterio.open(file) as data:
        print(f'metadata: {data.meta}\nshape: {data.shape}\nbands: {data.count}')
        data = data.read(1)
    return data

def create_raster():
    return