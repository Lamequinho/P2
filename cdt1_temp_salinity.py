import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("C:\python/cdt.txt", sep='\t')
headers=["date", "time (in s)", "depth (in m)", "T (in degC)", "salinity (in psu)"]
df.columns=headers
fig, ax=plt.subplots(1, 2)
ax[0, ].plot(df["depth (in m)"], df["T (in degC)"], color="blue")
ax[1].plot(df["depth (in m)"], df["salinity (in psu)"], color="red")
plt.title("CDT: Temperatura and Salinity")
ax[0, ].set_xlabel("Depth (in m)")
ax[1].set_xlabel("Depth (in m)")
ax[0, ].set_ylabel("Temperature (in degC)")
ax[1].set_ylabel("Salinity (in psu)")
plt.show()
