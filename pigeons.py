import numpy as np
import matplotlib.pyplot as plt
from matplotlib import ticker
import seaborn as sns
from scipy import stats

plt.ion()
sns.set(font_scale=1)
import pandas as pd

# Fetch data
data = pd.read_csv("data.csv")
data = data.apply(
    lambda x: x.str.strip()
    if x.dtype == "object"
    else x
)
n_pigeons = data["Pigeons"].values

# Visualize distribution
fig, ax = plt.subplots(1, 1, figsize=(6.4, 4.8), dpi=200)
max = int(np.ceil(np.max(n_pigeons)))
sns.distplot(
    n_pigeons,
    bins=np.arange(max + 2) - 0.5,
    color="#ff4063",
    label="Data",
)
plt.annotate(
    "Note: All responses rounded\n"
    "to the nearest whole pigeon.\n"
    f"Mean = {np.mean(n_pigeons):.1f}, "
    f"SD = {np.std(n_pigeons):.1f}, "
    f"$N$ = {len(n_pigeons)}",
    (0.80, 0.97),
    xycoords="axes fraction",
    ha="right",
    va="top",
    fontsize=10
)
plt.xlim(0-0.5, max+0.5+3)
ax.xaxis.set_major_locator(ticker.MultipleLocator(base=2))
plt.xlabel("Number of Pigeons They Could Carry [pigeons]")
plt.ylabel("Probability Distribution Function [-]")
plt.title("A Survey of Tinder:\n\"How many pigeons do you think you could carry?\"")
plt.tight_layout()
plt.legend()
plt.savefig("media/pigeons.svg")
plt.savefig("media/pigeons.png")
plt.show()
