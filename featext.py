import pyphysio as ph
import pandas as pd
import numpy as np
import pyphysio.indicators.timedomain as td_ind
import pyphysio.indicators.frequencydomain as fd_ind
import pyphysio.indicators.peaks as peaks
import pyphysio.indicators.nonlinear as nl
import pycatch22
 
def featext(df, name):
    fs = 1/ pd.to_datetime(df.time).diff()[1].total_seconds()
    signal  =ph.create_signal(df[name], sampling_freq=fs, name=name)
    indicators = ['Max', 'Mean', 'Median', 'RMSSD', 'StDev']
    result = {}
    for i in indicators:
        TR = getattr(td_ind,i)()(signal, add_signal = False)
        string = name +'_'+ i 
        result[i] = float(TR[string][0])
    indicators = ['PeakInBand', 'PowerInBand']
    for i in indicators:
        TR = getattr(fd_ind,i)(freq_min=0, freq_max=1000, method='welch')(signal, add_signal = False)
        string = name +'_'+ i 
        result[i] = float(TR[string][0])
    YEP = pycatch22.catch22_all(df[name])
    d = YEP['names']
    for i in range(0, len(d)):
        result[d[i]] = YEP['values'][i]
    return result

        
