from scipy.stats.stats import pearsonr
import pandas as pd

#Remember to run help on pearsonr to explain
df = pd.read_csv("trafficking_data.csv")
print pearsonr(df["persons prosecuted"],df["Adult victims"])
