import pandas as pd
from scipy import stats
import numpy as np

df = pd.read_csv("trafficking_data.csv")

print stats.mstats.normaltest(df["gdp"]), "gdp"
print stats.mstats.normaltest(df["Adult victims"]), "Adult victims"


