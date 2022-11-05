import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import os
import glob

path = r'.\data'
all_files = glob.glob(os.path.join(path, "*.csv"))

df_from_each_file = (pd.read_csv(f) for f in all_files)
df = pd.concat(df_from_each_file, ignore_index=True)

df["Date"] = pd.to_datetime(df["Date"], infer_datetime_format = True)

test_df = df[df["Date"] >= "2015-10-01"]
train_df = df[df["Date"] < "2015-10-01"]

X_train, y_train = train_df.drop(["Yield", "Date"], axis=1), train_df["Yield"]
X_test, y_test = test_df.drop(["Yield", "Date"], axis=1), test_df["Yield"]

reg = XGBRegressor(n_estimators=500, learning_rate=.04)
reg.fit(X_train, y_train, eval_set=[(X_train, y_train), (X_test, y_test)], eval_metric='mae')

predictions = reg.predict(X_test)

test_df = test_df.reset_index().drop("index", axis=1)
test_df['Predictions'] = pd.Series(predictions)

plt.rcParams.update({"figure.figsize": (17, 4), "figure.dpi":100})
fig, ax = plt.subplots()
sns.lineplot(data=df, x="Date", y="Yield", errorbar=None)
sns.lineplot(data=test_df, x= "Date", y="Predictions", errorbar=None)
plt.grid(linestyle='-', linewidth=0.3)
ax.set(ylim = (120, 180))

plt.show()