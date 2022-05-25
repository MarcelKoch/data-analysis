import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import ticker, cycler

_default_cycler = mpl.rcParams["axes.prop_cycle"]
mpl.rcParams["axes.prop_cycle"] = (_default_cycler + cycler(marker=["o", "v", "^", "<", ">", "s", "p", "*",
                                                                   "D", "P", "X"][:len(_default_cycler)]))
default_cycler = mpl.rcParams["axes.prop_cycle"]
dashed_cylcer = (default_cycler + cycler(linestyle=["--"] * len(default_cycler)))