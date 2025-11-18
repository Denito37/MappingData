from extract.extract  import read_drinking_fountains_data, read_tree_census_data, read_nyc_map, open_map
from transform.transform import transform_drinking_fountains_data, transform_trees_census_data 
from load.load import load_data
import time
import asyncio
import folium as fm

def test_Map():
    fountain = read_drinking_fountains_data()
    fountainTransformed = transform_drinking_fountains_data(fountain)

    map = fm.Map(
        max_bounds=True,
        location=[40.7,-74.0],
        min_lat= 40.49,
        max_lat=40.92,
        min_lon=-74.27,
        max_lon=-73.97
    )

    fm.TileLayer('OpenStreetMap', overlay=True).add_to(map)

    for index, row in fountainTransformed.iterrows():
        fm.Marker(
            location=[row['coordinates'].x,row['coordinates'].y],
            popup=row['located_at'],
            icon=fm.Icon(color='blue'),
            lazy=True
        ).add_to(map)

    map.save('index.html')
    return
async def test_ETL(): 
    fountain = read_drinking_fountains_data()
    fountainTransformed = transform_drinking_fountains_data(fountain)
    for index, row in fountainTransformed.iterrows():
        fountainTransformed['coordinates'] = f'{row['coordinates'].x},{row['coordinates'].y}'
    await load_data('Fountains', fountainTransformed)
    return 0

def main():
    print("Starting ETL process...")
    start = time.time()

    asyncio.run(test_ETL())
    #test_Map()

    end = time.time()
    print(f"Execution time: {round(end - start)} Second(s)")
    

if __name__ == "__main__":
    main()

# !ISSUE: calling the api endpoint for the tree data & transforming data results in long load : 30+ sec load
# !ISSUE: loading map of tree points results in long load: 4 mins
# !ISSUE: Error using tree functions with docker