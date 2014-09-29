import pandas as pd
import statsmodels.stats.api as sms
import statsmodels.formula.api as smf

df = pd.read_csv("trafficking_data.csv")

results = smf.ols('df["Adult victims"] ~ df["gdp"] + df["policy index"]',data=df).fit()

print sms.het_breushpagan(results.resid, results.model.exog)

