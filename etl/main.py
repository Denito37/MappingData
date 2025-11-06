from extract.extract  import read_drinking_fountains_data, read_tree_census_data, read_nyc_map
from transform.transform import transform_drinking_fountains_data, transform_trees_census_data, transform_map_data
import time

def main():
    print("Starting ETL process...")
    start = time.time()

    fountain = read_drinking_fountains_data()
    transformedFountain = transform_drinking_fountains_data(fountain)
    #tree = read_tree_census_data()
    #transformedTree = transform_trees_census_data(tree)
    print(transformedFountain.info())
    read_nyc_map()

    end = time.time()
    print(f"Execution time: {round(end - start)} Second(s)")
    

if __name__ == "__main__":
    main()

# !ISSUE: calling the api endpoint for the tree data results in long load : 30+ sec load