import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import statsmodels.api as sm
df = pd.read_csv("trafficking_data.csv")

results_victims = smf.ols('df["Adult victims"] ~ df["gdp"] + df["policy index"]',data=df).fit()

ind_vars = df[["gdp","policy index"]]

results_prosecuted = sm.OLS(df["persons prosecuted"], ind_vars).fit()
print results_victims.summary()
print "Parameters:", results_victims.params
print "R^2", results_victims.rsquared

print results_prosecuted.summary()
print "Parameters:", results_prosecuted.params
print "R^2", results_prosecuted.rsquared
