from extract.extract  import read_drinking_fountains_data, read_tree_census_data, read_nyc_map, open_map
from transform.transform import transform_drinking_fountains_data, transform_trees_census_data 
from load.load import load_data
import time
import asyncio


async def test_ETL_Fountain(): 
    fountain = read_drinking_fountains_data()
    fountain = transform_drinking_fountains_data(fountain)
    for i, row in fountain.iterrows():
        fountain['coordinates'] = f'{row['coordinates'].x},{row['coordinates'].y}'
    await load_data('Fountains', fountain)
    return 0

async def test_ETL_Tree():
    tree = read_tree_census_data()
    tree = transform_trees_census_data(tree)
    tree = tree.drop(columns=['geometry'])
    await load_data('Trees', tree)
    return 0

def main():
    print("Starting ETL process...")
    start = time.time()

    asyncio.run(test_ETL_Fountain())
    stop = time.time()
    print(f"Execution time: {round(stop - start)} Second(s)")
    asyncio.run(test_ETL_Tree())

    end = time.time()
    print(f"Execution time: {round(end - stop)} Second(s)")
    

if __name__ == "__main__":
    main()

# !NOTICE: Will move from sqlite to spatialite to hold geo data
# !ISSUE: Error using tree functions with docker