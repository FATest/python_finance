from market_environment import *
from short_rate import *
import datetime as dt

dates = [dt.datetime(2015,1,1),dt.datetime(2015,7,1),dt.datetime(2016,1,1)]

csr = Short_rate('csf',0.05)

market_environ_1 = Market_environment('me_1',dates)