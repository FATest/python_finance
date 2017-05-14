import pandas as pd
import numpy as np
from urllib import urlretrieve

### retrieve and store data from urls
es_url = 'http://www.stoxx.com/download/historical_values/hbrbcpe.txt'
vs_url = 'http://www.stoxx.com/download/historical_values/h_vstoxx.txt'
urlretrieve(es_url,'./data/es.txt')
urlretrieve(vs_url,'./data/vs.txt')

### data cleaning & display top 6 lines
# remove all blanks
lines = open('./data/es.txt','r').readlines()
lines = [line.replace(" ","") for line in lines]
print lines[:6] 

# delete unneeded header lines and create a new file
for line in lines[3883:3890]:
	print line[41:]

new_file = open('./data/es50.txt','w')
new_file.writelines('date' + lines[3][:-1] + ';DEL' + lines[3][-1])
new_file.writelines(lines[4:])
new_file.close()
new_lines = open('./data/es50.txt','r').readlines()
print new_lines[:5]

### import data using pandads
es = pd.read_csv('./data/es50.txt',index_col=0,parse_dates=True,sep=';',dayfirst=True)
np.round(es.tail())

del es['DEL']
es.info()