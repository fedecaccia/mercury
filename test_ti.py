import unittest

import numpy as np
import pandas as pd

from technical_indicators import TechnicalIndicators

class TestTI(unittest.TestCase):

    def setUp(self):
        
        # random data
        returns = pd.DataFrame(np.random.normal(1.0, 0.03, (100, 10)))
        self.prices = returns.cumprod()
        self.prices = prices.set_index(pd.DatetimeIndex(start="01/01/2001", freq="1d", periods=100))

        # TI instance
        self.TI = TechnicalIndicators()

    def test_rsi(self):
        rsi = self.TI.RSI(self.prices[0])