from extract.extract import open_map, read_drinking_fountains_data, read_tree_census_data
from transform.transform import transform_drinking_fountains_data, transform_trees_census_data
import matplotlib.pyplot as plt
import rasterio

def testMap():
    tempMap = open_map()
    fig, ax = plt.subplots()

    extent =[tempMap.bounds[0],tempMap.bounds[2],tempMap.bounds[1],tempMap.bounds[3]]
    ax = rasterio.plot.show(tempMap,extent=extent,ax=ax, cmap='Reds')

    fountain = read_drinking_fountains_data()
    fountainTransformed = transform_drinking_fountains_data(fountain)
    fountainTransformed.plot(ax=ax, color='blue')

    #tree = read_tree_census_data()
    #treeT = transform_trees_census_data(tree)
    #treeT.plot(ax=ax, color='green')

    plt.show()

    return 0