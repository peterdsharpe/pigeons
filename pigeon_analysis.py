import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style
import seaborn as sns

sns.set(font_scale=1)
import pandas as pd
from scipy import stats

# Fetch data
data = pd.read_excel("data.xlsx")
n_pigeons = np.array(data.Pigeons)

# Fit a model
distribution = stats.chi2 # this has no physical basis, just picking this dist. for kicks
params = distribution.fit(
    n_pigeons,
    fscale = 1,
    floc = 0,
)

# distribution = stats.ncx2
# params = distribution.fit(
#     n_pigeons,
#     4,
#     0.5,
#     fscale = 1,
#     floc = 0,
# )

# distribution = stats.expon

# distribution = stats.norm
# params = distribution.fit(
#     n_pigeons,
#     # fscale=1,
#     # floc=0,
# )

# distribution = stats.truncnorm
# params = distribution.fit(
#     n_pigeons,
#     fa = -2,
#     fb = np.Inf,
#     # fscale=1,
#     floc=0,
# )

print("Fit Parameters:\n", params)

# Visualize distribution
fig, ax = plt.subplots(1, 1, figsize=(6.4, 4.8), dpi=200)
x = np.linspace(0, np.max(n_pigeons)+0.5, 500)
plt.plot(
    x,
    distribution.pdf(x, *params),
    label="Model",
    color=np.array((64,143,255))/255,
    linewidth=3,
    zorder = 11
)
plt.fill_between(
    x,
    0,
    distribution.pdf(x, *params),
    color=np.array((64,143,255,255*0.2))/255,
    zorder = 10
)
plt.hist(
    n_pigeons,
    bins=np.arange(np.ceil(np.max(n_pigeons)) + 2) - 0.5,
    density=True,
    label="Data",
    color=np.array((255,64,99))/255,
    zorder = 9
)
plt.annotate(
    "Note: All responses rounded\nto the nearest whole pigeon.",
    (0.45, 0.9),
    xycoords="axes fraction",
    fontsize = 10
)
plt.xlabel("Number of Pigeons They Could Carry [pigeons]")
plt.ylabel("Probability Distribution Function [-]")
plt.title("A Survey of Tinder:\n\"How many pigeons do you think you could carry?\"")
plt.tight_layout()
plt.legend()
plt.savefig("pigeons.svg")
plt.savefig("pigeons.png")
plt.show()
