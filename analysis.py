from data_import_cleaning_read_csv import *
import datetime as dt
import pandas as pd

data = pd.DataFrame({'EUROSTOXX':es['SX5E'][es.index>dt.datetime(1999,1,1)]})

data = data.join(pd.DataFrame({'VSTOXX': vs['V2TX'][vs.index>dt.datetime(1999,1,1)]}))

### missing value fills
data = data.fillna(method='ffill')
data.info()

### display last rows
data.tail()

### plot
data.plot(subplots=True, grid=True, style='b',figsize=(8,6))
