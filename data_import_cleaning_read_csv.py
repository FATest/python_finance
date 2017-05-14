import pandas as pd
import numpy as np
from urllib import urlretrieve

### retrieve and store data from urls
es_url = 'http://www.stoxx.com/download/historical_values/hbrbcpe.txt'
vs_url = 'http://www.stoxx.com/download/historical_values/h_vstoxx.txt'

cols = ['SX5P', 'SX5E','SXXP','SXXE','SXXF','SXXA','DK5F','DKXF']

es = pd.read_csv(es_url, index_col=0,parse_dates=True,sep=':', dayfirst=True,header=None,skiprows=4,names=cols)

es.tail()

vs = pd.read_csv('./data/vs.txt', index_col=0,header=2,parse_dates=True,sep=',',dayfirst=True)

vs.info()