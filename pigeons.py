import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style
import seaborn as sns

sns.set(font_scale=1)
import pandas as pd
from scipy import stats

# Fetch data
data = pd.read_csv("data.csv")
n_pigeons = np.array(data.Pigeons)

# Fit a model
distribution = stats.norm
params = distribution.fit(
    n_pigeons,
)

print("Fit Parameters:\n", params)

# Visualize distribution
fig, ax = plt.subplots(1, 1, figsize=(6.4, 4.8), dpi=200)
x = np.linspace(0, np.max(n_pigeons) + 0.5, 500)
distribution_out = distribution.pdf(x, *params) / (1 - distribution.cdf(0, *params))
x = np.hstack((0, x))
distribution_out = np.hstack((0, distribution_out))
plt.plot(
    x,
    distribution_out,
    label="Model",
    color=np.array((64, 143, 255)) / 255,
    linewidth=3,
    zorder=11
)
plt.fill_between(
    x,
    0,
    distribution_out,
    color=np.array((64, 143, 255, 255 * 0.2)) / 255,
    zorder=10
)
plt.hist(
    n_pigeons,
    bins=np.arange(np.ceil(np.max(n_pigeons)) + 2) - 0.5,
    density=True,
    label="Data",
    color=np.array((255, 64, 99)) / 255,
    zorder=9
)
plt.annotate(
    "Note: All responses rounded\nto the nearest whole pigeon.",
    (0.45, 0.9),
    xycoords="axes fraction",
    fontsize=10
)
plt.xlabel("Number of Pigeons They Could Carry [pigeons]")
plt.ylabel("Probability Distribution Function [-]")
plt.title("A Survey of Tinder:\n\"How many pigeons do you think you could carry?\"")
plt.tight_layout()
plt.legend()
plt.savefig("pigeons.svg")
plt.savefig("pigeons.png")
plt.show()
