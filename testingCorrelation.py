from scipy.stats.stats import pearsonr
import pandas as pd

df = pd.read_csv("trafficking_data.csv")
print pearsonr(df["persons prosecuted"],df["Adult victims"])
