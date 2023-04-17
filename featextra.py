import tsfresh
import pandas as pd
import numpy as np

def featextra(df,name):
    feat = tsfresh.extract_features(df[['time',name,'ID']], column_value =name, 
    column_sort='time', column_id='ID', default_fc_parameters = tsfresh.feature_extraction.settings.EfficientFCParameters())
    string = name+'__'
    feat.columns = feat.columns.str.replace(string,'')    
    return feat