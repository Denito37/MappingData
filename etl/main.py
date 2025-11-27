from extract.extract import read_drinking_fountains_data, read_tree_census_data, read_nyc_map, open_map
from transform.transform import transform_drinking_fountains_data, transform_trees_census_data 
from load.load import load_data
import time
import asyncio


async def test_ETL_Fountain(): 
    fountain = read_drinking_fountains_data()
    fountain = transform_drinking_fountains_data(fountain)
    # Fixed: Use .apply() for vectorized operation instead of iterrows loop
    # This is faster and correctly assigns to each row
    fountain['coordinates'] = fountain['coordinates'].apply(
        lambda coord: f"{coord.x},{coord.y}"
    )
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
    print(f"Fountain ETL execution time: {round(stop - start)} Second(s)")
    
    asyncio.run(test_ETL_Tree())
    end = time.time()
    print(f"Tree ETL execution time: {round(end - stop)} Second(s)")
    
    print(f"Total execution time: {round(end - start)} Second(s)")


if __name__ == "__main__":
    main()

# !NOTICE: Will move from sqlite to spatialite to hold geo data
# !ISSUE: Error using tree functions with docker