import pandas as pd
import numpy as np
import ee
import glob
import geemap
from datetime import timedelta
import datetime
from os import remove



if __name__ == '__main__':
    Map = geemap.Map()
    dataset = ee.ImageCollection('COPERNICUS/S5P/NRTI/L3_CO')
    

