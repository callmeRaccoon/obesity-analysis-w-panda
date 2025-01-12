import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

obesity_df = pd.read_csv("ObesityDataSet_raw_and_data_sinthetic.csv")
print(obesity_df.head())
#Having an overview to dataset
print(obesity_df.info())
#Having an overview of the data types in the dataset
print(obesity_df.isnull().sum())
#Checking if the dataset has any missing values
print(obesity_df.describe())
#Having a statistical summary for columns

#Creating a barplot to visualize distribution of obesity levels
obesity_distribution = obesity_df.value_counts("NObeyesdad").plot(kind="bar", color="green")
plt.xlabel("Obesity Levels")
plt.ylabel("Number of People")
plt.title("Distribution of Obesity Levels")
plt.xticks(rotation=45)
plt.grid()
plt.show()

#Creating a barplot to visualizing obesity levels based on gender
obesity_by_gender = obesity_df.groupby(["NObeyesdad", "Gender"]).size().unstack()

obesity_by_gender.plot(kind="bar", stacked=True, color=["pink", "blue"])
plt.xlabel("Obesity Level")
plt.ylabel("Number of People")
plt.title("Obesity Level Distribution by Gender")
plt.xticks(rotation=45)
plt.legend(title="Gender")
plt.show()

#Categorizing FAF as low, medium and high for better observations
FAF_categories = pd.cut(obesity_df["FAF"], bins=[0, 1, 2, 3], labels=["low", "medium", "high"], include_lowest=True)
obesity_df["FAF_category"] = FAF_categories

#Grouping obesity levels distribution for every FAF(activity level)
obesity_FAF_dist = obesity_df.groupby("FAF_category")["NObeyesdad"].value_counts().unstack()

obesity_FAF_dist.plot(kind="bar", stacked=True, figsize=(8,6))

plt.title("Obesity Levels by Physical Activity Level")
plt.xlabel("Physical Activity Level")
plt.ylabel("Number of People")
plt.xticks(rotation=0)
plt.legend(title="Obesity Level")
plt.show()

#Grouping obesity levels distribution by high calorie food intake
obesity_FAVC_dist = obesity_df.groupby("FAVC")["NObeyesdad"].value_counts().unstack()

obesity_FAVC_dist.plot(kind="bar", stacked=True, figsize=(8,6))

plt.title("Obesity Levels by High Calorie Food Intake")
plt.xlabel("High Calorie Food Intake Y/N")
plt.ylabel("Number of People")
plt.xticks(rotation=0)
plt.legend(title="Obesity Level")
plt.show()

#Grouping obesity levels distribution by family history with overweight

obesity_FHWO_dist = (obesity_df.groupby("family_history_with_overweight")["NObeyesdad"]
                     .value_counts().unstack()
                     )
obesity_FHWO_dist.plot(kind="bar", stacked=True, figsize=(8,6))

plt.title("Obesity Levels by Family History with Overweight")
plt.xlabel("Family History with Overweight")
plt.ylabel("Number of People")
plt.xticks(rotation=0)
plt.legend(title="Obesity Level")
plt.show()