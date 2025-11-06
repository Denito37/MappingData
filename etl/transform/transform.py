import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from shapely import wkt

dropFountainColumns = [
    'painted', 'fountainco', 'fountainty', 'gispropnum','decription', 'parentid','position',
    ':id',':version',':@computed_region_f5dn_yrer',':@computed_region_yeji_bk3q',':@computed_region_sbqj_enih',':@computed_region_92fq_4b7q', ':created_at'
]

renameFountainColumns = {
    'system': 'id',
    'featuresta': 'status',
    'propertyna':'located_at',
    'the_geom':'coordinates'
}

dropTreeColumns = [
    'stump_diam', 'curb_loc', 'root_stone', 'root_grate', 'root_other',
    'trunk_wire', 'trnk_other', 'trnk_light', 'brch_light', 'brch_shoe', 'brch_other',
    'sidewalk', 'zip_city', 'state', 'cb_num', 'borocode',
    'x_sp', 'y_sp', 'block_id', 'bbl', 'bin', 'spc_latin', 'steward',
    'guards', 'sidewalk', 'health','tree_dbh','user_type','problems', 'address', 'zipcode', 'cncldist',
    'st_assem', 'st_senate', 'nta', 'nta_name', 'boro_ct', 'census_tract', 'council_district',
    ':id',':version',':created_at','created_at','latitude','longitude'
]

renameTreeColumns = {
    'tree_id':'id',
    'spc_common':'name',
    'boroname':'borough',
    'geometry':'coordinates'
}

def transform_drinking_fountains_data(data):
    fountains_cleaned = data.drop(dropFountainColumns, axis=1)
    fountains_cleaned = fountains_cleaned.rename(columns=renameFountainColumns)
    return fountains_cleaned

def transform_trees_census_data(data):
    data = gpd.GeoDataFrame(data, geometry=gpd.points_from_xy(data.longitude, data.latitude))
    trees_cleaned = data.drop(dropTreeColumns,axis=1)
    trees_cleaned = trees_cleaned.rename(columns=renameTreeColumns)
    trees_cleaned['name'] = trees_cleaned['name'].fillna('Unknown')
    return trees_cleaned  

def transform_map_data(data):
    return