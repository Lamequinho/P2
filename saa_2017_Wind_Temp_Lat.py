import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
saa=pd.read_csv("C:\python/saa_2017_met.txt")
WIND=saa["WIND_SPEED_TRUE"][1:907]
AIR_TEMP1=saa["AIR_TEMPERATURE"][1:907]
LATDEG=saa["LATITUDE"][1:907]/100.
fig, ax=plt.subplots()
plt.scatter(WIND,AIR_TEMP1, c=LATDEG)
plt.title("Wind_Temp_Latitude")
ax.set_xlabel("Wind (m/s)")
ax.set_ylabel("Temperature (in degC)")
plt.show()
chmod +x Wind_Temp_Lat
