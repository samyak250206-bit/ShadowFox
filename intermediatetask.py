import numpy as py
import pandas as pd

# Load the Dataset
df = pd.read_csv("delhiaqi.csv")

#Checking the whether the dataset is load or not
print(df.head(5))

#Statistics Summary for all Pollutants
print(df.describe())

# Line Charts between PM2.5 AND PM10 based on the each day
import matplotlib.pyplot as plt

# Make a copy of the original DataFrame to avoid modifying it directly
copy_data = df.copy()
#Checking the whether the dataset is load or not
print(copy_data.head(5))

# Convert the date column to datetime format
copy_data["date"] = pd.to_datetime(copy_data["date"])
copy_data["day"] = copy_data["date"].dt.day

#Group the date column by day and calculate the mean for PM2.5 and PM10
group_hour = copy_data.groupby("day")[["pm2_5", "pm10","co","no","no2","o3","so2","nh3"]].mean()
day = group_hour.index
pm2_5 = group_hour["pm2_5"]
pm10 = group_hour["pm10"]
co = group_hour["co"]
no = group_hour["no"]
no2 = group_hour["no2"]
o3 = group_hour["o3"]
so2 = group_hour["so2"]
nh3 = group_hour["nh3"]

# Line chart for PM2.5 and PM10 based on each day
plt.plot(day,pm2_5, label = "PM2.5")
plt.plot(day,pm10, label = "PM10")
plt.xticks(day)
plt.xlabel("Day")
plt.ylabel("Pollutant Levels(PM2_5 and PM10)")
plt.title("Line Chart for PM2.5 and PM10 based"
" on each day")
plt.grid()
plt.legend()
plt.show()

# Calculate the correlation between CO and PM2.5
correlation = group_hour["co"].corr(group_hour["pm2_5"])
print("Correlation between CO and PM2.5:", correlation.round(2))

# Scatter Chart between CO and PM2_5
plt.scatter(co,pm2_5,color="green")
plt.xlabel("CO")
plt.ylabel("PM2.5")
plt.title("Scatter Chart between CO and PM2_5")
plt.show()

# Calculate the correlation between all pollutants
import seaborn as sns
correlation = group_hour.corr()
print(correlation.round(2))

# Heatmap for correlation between all pollutants
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.tight_layout()
plt.show()