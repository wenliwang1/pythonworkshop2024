import os
import csv
import requests
import pandas as pd
import numpy as np

import plotly
import plotly.express as px
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib_venn

print ("all packages have been imported successfully")

groupone = set(["oak", "pecan", "walnut", "bald", "syc"])
grouptwo = set(["pecan", "walnut","peach","pear"])

matplotlib_venn.venn2((groupone, grouptwo), ("Park 1 Trees", "Park 2 Trees"))

plt.show()