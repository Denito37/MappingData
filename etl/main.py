from extract.extract  import read_drinking_fountains_data, read_tree_census_data, read_nyc_map, open_map
from transform.transform import transform_drinking_fountains_data, transform_trees_census_data 
from load.load import load_data
import time
import asyncio

async def test_ETL_Fountain(): 
    fountain = read_drinking_fountains_data()
    fountainTransformed = transform_drinking_fountains_data(fountain)
    for index, row in fountainTransformed.iterrows():
        fountainTransformed['coordinates'] = f'{row['coordinates'].x},{row['coordinates'].y}'
    await load_data('Fountains', fountainTransformed)
    return 0

async def test_ETL_Tree():
    tree = read_tree_census_data()
    treeTransformed = transform_trees_census_data(tree)
    print(treeTransformed.info())
    for index,row in treeTransformed.iterrows():
        treeTransformed['geometry'] = f'{row['geometry'].x},{row['geometry'].y}'
    await load_data('Trees', treeTransformed)
    return 0

def main():
    print("Starting ETL process...")
    start = time.time()

    asyncio.run(test_ETL_Fountain())
    stop = time.time()
    print(f"Execution time: {round(stop - start)} Second(s)")
    #asyncio.run(test_ETL_Tree())

    end = time.time()
    print(f"Execution time: {round(end - stop)} Second(s)")
    

if __name__ == "__main__":
    main()

# !ISSUE: calling the api endpoint for the tree data & transforming data results in long load : 30+ sec load
# !ISSUE: loading map of tree points results in long load: 4 mins
# !ISSUE: Error using tree functions with docker