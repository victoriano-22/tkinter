import pandas as pd
import numpy as np
import math
# import unit_test

def load_csv(filepath):
    df = pd.read_csv(filepath, sep=',')
    return df

def avg_depth_sta():
    #get index yg ke 20
    #ambil index 21 & 19
    list_depth = [2.7,2.6,2.5]
    calc_avg = np.average(list_meters)
    return calc_avg

def measure_meter(lat1, lon1, lat2, lon2):
    rad_earth = 6378.137 #km
    dLat = lat2 * math.pi / 180 - lat1 * math.pi / 180
    dLon = lon2 * math.pi / 180 - lon1 * math.pi / 180;
    a = math.sin(dLat/2) * math.sin(dLat/2)+math.cos(lat1 * math.pi / 180) * math.cos(lat2 * math.pi / 180)*math.sin(dLon/2) * math.sin(dLon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a));
    d = rad_earth * c