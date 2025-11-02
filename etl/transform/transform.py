import pandas as pd

dropFountainColumns = [
    'painted', 'fountainco', 'fountainty', 'gispropnum','decription', 'parentid',
]

renameFountainColumns = {
    'system': 'id',
    'featuresta': 'status',
    'propertyna':'located_at'
}

dropTreeColumns = [
    'stump_diam', 'curb_loc', 'root_stone', 'root_grate', 'root_other',
    'trunk_wire', 'trunk_other', 'trunk_light', 'brch_light', 'brch_heavy', 'brch_other',
    'sidewalk', 'zip_city', 'state', 'cb_num', 'borocode',
    'x_sp', 'y_sp', 'block_id', 'bbl', 'bin', 'spc_latin', 'steward',
    'guards', 'sidewalk', 'health','tree_dhb','user_type','problems', 'address', 'zipcode', 'cncldist',
    'st_assem', 'st_senate', 'nta', 'nta_name', 'boro_ct', 'census_tract', 'council_district'
]

renameTreeColumns = {}

def transform_drinking_fountains_data(data):
    fountains_cleaned = data.drop(dropFountainColumns, axis=1)
    fountains_cleaned = fountains_cleaned.rename(columns=renameFountainColumns)
    return fountains_cleaned

def transform_trees_census_data(data):
    trees_cleaned = data.drop(dropTreeColumns,axis=1)
    trees_cleaned = trees_cleaned.rename(columns=renameTreeColumns)
    return trees_cleaned

# run transformation in batches   