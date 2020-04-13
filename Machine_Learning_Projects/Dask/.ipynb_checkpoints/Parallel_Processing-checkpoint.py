from dask import delayed, compute
import dask.bag as db
import dask.array as da

import numpy as np
import math
import os


@delayed
def distance(lat1, lon1, lat2, lon2):
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d


def read_json():

    coordinates = db.read_text("")

    print(coordinates.take(1))




if __name__ == '__main__':
    print('main')
    print(os.getcwd())
    # read_json()
        