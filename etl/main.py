from extract.extract  import read_drinking_fountains_data, read_tree_census_data, read_nyc_map, open_map
from transform.transform import transform_drinking_fountains_data, transform_trees_census_data 
from load.load import load_data
import time
import asyncio
import pandas as pd

async def test_ETL():
    testData = [
        {
            ':updated_at':'test',
            'id':'123',
            'located_at':'test',
            'borough':'test',
            'department':'test',
            'status':'test',
            'coordinates':'test'

    },
    {
            ':updated_at':'test',
            'id':'456',
            'located_at':'test',
            'borough':'test',
            'department':'test',
            'status':'test',
            'coordinates':'test'
    },
    {
            ':updated_at':'test',
            'id':'789',
            'located_at':'test',
            'borough':'test',
            'department':'test',
            'status':'test',
            'coordinates':'test'

    }]
    testData = pd.DataFrame(testData)
    fountain = read_drinking_fountains_data()
    fountainTransformed = transform_drinking_fountains_data(fountain)
    print(fountainTransformed.info())
    await load_data('Fountains', testData)
    return 0

def main():
    print("Starting ETL process...")
    start = time.time()

    asyncio.run(test_ETL())

    end = time.time()
    print(f"Execution time: {round(end - start)} Second(s)")
    

if __name__ == "__main__":
    main()

# !ISSUE: calling the api endpoint for the tree data & transforming data results in long load : 30+ sec load
# !ISSUE: loading map of tree points results in long load: 4 mins
# !ISSUE: Error using tree functions with docker