import pandas as pd
import json
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
import itertools


data = pd.read_csv('classifications.csv')


def vals_to_new_column(data_column):
    """
    takes the data.annotations column as a parameter
    returns dataframe with individual segment coordinates stored in a row
    """
    list_vals = []
    for entry in json.loads(data_column)[0]['value']:
        list_vals.append([entry['x1'], entry['y1'], entry['x2'], entry['y2']])
    return list_vals

data['listed_vals'] = data['annotations'].apply(vals_to_new_column)



def make_plant_datasheet(data_table):
    """
    takes the datasheet with 'listed_vals' column as a parameter
    returns dataframe with useful metadata, angle, axis length and axis coordinates.
    """
    df = pd.DataFrame() #columns = [0: 'classification_id', 'username', 'created_at', 'subject_data' , 'angle', 'major_axis_length', 'x1_major', 'x2_major', 'y1_major', 'y2_major', 'minor_axis_length', 'x1_minor', 'x2_minor', 'y1_minor', 'y2_minor'] (will rename at end)
    for row_num in range(len(data_table)):
        for combo in itertools.combinations(data_table.listed_vals[row_num], 2):
            segments_to_check = CheckLeaf(combo[0],combo[1])
            if segments_to_check.on_screen() and segments_to_check.line_segments_intersect() and segments_to_check.calc_angle_between_segments() > 80.0:
                lengths_minor_major = segments_to_check.calc_lengths_minor_major()
                df = df.append([[data_table.classification_id[row_num], \
                                 data_table.user_name[row_num], \
                                 data_table.created_at[row_num], \
                                 data_table.subject_data[row_num], \
                                 data_table.subject_ids[row_num], \
                                 segments_to_check.calc_angle_between_segments(), \
                                 float(str(segments_to_check.find_the_intersection_point()[0])[2:-2]), \
                                 float(str(segments_to_check.find_the_intersection_point()[1])[2:-2]), \
                                 lengths_minor_major[0], \
                                 lengths_minor_major[1][0], \
                                 lengths_minor_major[1][1], \
                                 lengths_minor_major[1][2], \
                                 lengths_minor_major[1][3], \
                                 lengths_minor_major[2], \
                                 lengths_minor_major[3][0], \
                                 lengths_minor_major[3][1], \
                                 lengths_minor_major[3][2], \
                                 lengths_minor_major[3][3]]]) 

    df = df.rename({0: 'classification_id', \
                    1: 'username', \
                    2: 'created_at', \
                    3: 'subject_data', \
                    4: 'subject_id', \
                    5: 'angle', \
                    6: 'intersection_point_x', \
                    7: 'intersection_point_y', \
                    8: 'major_axis_length', \
                    9: 'major_x1', \
                    10: 'major_y1', \
                    11: 'major_x2', \
                    12: 'major_y2', \
                    13:'minor_axis_length', \
                    14: 'minor_x1', \
                    15: 'minor_y1', \
                    16: 'minor_x2', \
                    17: 'minor_y2',},\
                   axis = 'columns')
    #figure out how to rename index
    return df
