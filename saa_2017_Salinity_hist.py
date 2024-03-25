import pandas as pd
saa=pd.read_csv("C:\python/saa_2017_met.txt")
import matplotlib.pyplot as plt
from matplotlib import dates as mpl_dates
from datetime import datetime, timedelta
saa["TIME_SERVER"]=pd.to_datetime(saa["TIME_SERVER"])
saa.sort_values("TIME_SERVER", inplace=True)
SAL=saa["TSG_SALINITY"][1:907]
fig, ax=plt.subplots()
bins=[30,30.5,31,31.5,32,32.5,33,33.5,34,34.5,35]
ax.hist(SAL, bins=bins)
plt.style.use("grayscale")
plt.title("Salinity profile")
ax.set_xlabel("Salinity")
ax.set_ylabel("Fequency")
plt.show()