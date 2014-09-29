import pandas as pd
import numpy as np
import re
df = pd.read_csv("trafficking_data.csv")

#swapping out values
print df[["gdp","Adult victims"]]

#methods of replacement

df_replace = df.replace(np.nan,0)
print df_replace
print df.interpolate()


