import talib

import numpy as np

class TechnicalIndicators(object):

    def __init__(self):
        pass

    def RSI(self, series, period):
        delta = series.diff().dropna()
        u = delta * 0
        d = u.copy()
        u[delta > 0] = delta[delta > 0]
        d[delta < 0] = -delta[delta < 0]
        u[u.index[period-1]] = np.mean( u[:period] ) #first value is sum of avg gains
        u = u.drop(u.index[:(period-1)])
        d[d.index[period-1]] = np.mean( d[:period] ) #first value is sum of avg losses
        d = d.drop(d.index[:(period-1)])    
        rs = talib.EMA(u, timeperiod=period) / talib.EMA(d, period)
        return 100 - 100 / (1 + rs)