from extract.extract  import read_drinking_fountains_data, read_tree_census_data, read_nyc_map, open_map
from transform.transform import transform_drinking_fountains_data, transform_trees_census_data, transform_map_data
import time
import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt

def testMap():
    tempMap = open_map()
    fig, ax = plt.subplots()

    extent =[tempMap.bounds[0],tempMap.bounds[2],tempMap.bounds[1],tempMap.bounds[3]]
    ax = rasterio.plot.show(tempMap,extent=extent,ax=ax, cmap='Blues')

    #fountain = read_drinking_fountains_data()
    #fountainTransformed = transform_drinking_fountains_data(fountain)
    #fountainTransformed.plot(ax=ax)

    tree = read_tree_census_data()
    treeT = transform_trees_census_data(tree)
    treeT.plot(ax=ax)

    return 0

def main():
    print("Starting ETL process...")
    start = time.time()

    testMap()

    end = time.time()
    print(f"Execution time: {round(end - start)} Second(s)")
    

if __name__ == "__main__":
    main()

# !ISSUE: calling the api endpoint for the tree data results in long load : 30+ sec load