import pandas as pd
import matplotlib.pyplot as plt
saa=pd.read_csv("C:\python/saa_2017_met.txt")
from matplotlib import dates as mpl_dates
from datetime import datetime, timedelta
saa["TIME_SERVER"]=pd.to_datetime(saa["TIME_SERVER"])
saa.sort_values("TIME_SERVER", inplace=True)
###SUBSETING TIME (TIME_SERVER TO FROM BEGGINING TO JULY 04):
TIME1=saa["TIME_SERVER"][1:907]
AIR_TEMP1=saa["AIR_TEMPERATURE"][1:907]
fig, ax=plt.subplots()
#plt.plot_date(TIME1,AIR_TEMP1)
ax.plot(TIME1,AIR_TEMP1)
plt.style.use("grayscale")
plt.title("Time series of temperature")
ax.set_xlabel("Time")
labels=TIME1
ax.set_xticklabels(labels, rotation=45, ha='right')
ax.set_ylabel("Temperature (in degC)")
fig.savefig(("Saa_2017_meto_Temperature profile.png", dpi=200)
plt.show()