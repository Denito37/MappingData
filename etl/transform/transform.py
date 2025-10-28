import pandas as pd
from etl.extract import extract_drinking_fountains_data, extract_trees_census_data

dropFountainColumns = [
    'painted', 'fountainco', 'fountainty', 'gispropnum','decription', 'parentid'
]

dropTreeColumns = [
    'stump_diam', 'curb_loc', 'root_stone', 'root_grate', 'root_other',
    'trunk_wire', 'trunk_other', 'trunk_light', 'brch_light', 'brch_heavy', 'brch_other',
    'sidewalk', 'zip_city', 'state', 'cb_num', 'borocode',
    'x_sp', 'y_sp', 'block_id', 'bbl', 'bin', 'spc_latin', 'steward',
    'guards', 'sidewalk', 'health','tree_dhb','user_type','problems', 'address', 'zipcode', 'cncldist',
    'st_assem', 'st_senate', 'nta', 'nta_name', 'boro_ct', 'census_tract', 'council_district'
]

def transform_drinking_fountains_data():
    data = extract_drinking_fountains_data()
    fountains = pd.json_normalize(data)
    fountains_cleaned = fountains.drop(columns=dropFountainColumns)
    fountains_cleaned = fountains_cleaned.rename(columns={
        'system': 'id',
        'featurestatus': 'status',
        'propertyna':'located_at'
    })
    return fountains_cleaned

def transform_trees_census_data():
    data = extract_trees_census_data()
    trees = pd.json_normalize(data)
    trees_cleaned = trees.drop(columns=dropTreeColumns)
    trees_cleaned = trees_cleaned.rename(columns={
        
    })
    return trees_cleaned

# run transformation in batches   