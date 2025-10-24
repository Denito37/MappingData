import pandas as pd
from etl.extract import extract_drinking_fountains_data, extract_trees_census_data

dropFountainColumns = [
    'painted', 'fountain_count', 'fountain_type', 'gispropnum','district', 'ompropid'
]

dropTreeColumns = [
    'stump_diam', 'curb_loc', 'root_stone', 'root_grate', 'root_other',
    'trunk_wire', 'trunk_other', 'trunk_light', 'brch_light', 'brch_heavy', 'brch_other',
    'sidewalk', 'zip_city', 'state', 'cb_num', 'borocode',
    'x_sp', 'y_sp', 'block_id', 'bbl', 'bin', 'spc_latin', 'steward',
    'guards', 'sidewalk', 'health','tree_dhb','user_type','problems', 'address', 'postcode', 'cncldist',
    'st_assem', 'st_senate', 'nta', 'nta_name', 'boro_ct'
]
