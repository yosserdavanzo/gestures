import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = r"temp.csv"

df = pd.read_csv(DATA_PATH)

fig, axs = plt.subplots(2)

# Labels
axs[0].set_title("Raw Accels")
axs[1].set_title("Real Accels")


# Turn off tick labels
axs[0].set_yticklabels([])
axs[0].set_xticklabels([])
axs[1].set_yticklabels([])
axs[1].set_xticklabels([])
axs[0].set_yticks([])
axs[0].set_xticks([])
axs[1].set_yticks([])
axs[1].set_xticks([])

t = df["t"]
aa = df[["aa.x", "aa.y", "aa.z"]]

# df.plot(x="t", y = ["aa.x", "aa.y", "aa.z"], kind='line')

linex, =axs[0].plot(t, df["aa.x"], "r")
liney, =axs[0].plot(t, df["aa.y"], "g")
linez, =axs[0].plot(t, df["aa.z"], "b")
axs[1].plot(t, df["aReal.x"], "r")
axs[1].plot(t, df["aReal.y"], "g")
axs[1].plot(t, df["aReal.z"], "b")

fig.legend([linex, liney, linez], ["x", "y", "z"])


plt.show()
