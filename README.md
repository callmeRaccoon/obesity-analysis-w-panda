# obesity-analysis-w-panda
obesity-analysis-pandas

🏋️‍♂️ Obesity Data Analysis

📌 Overview

This project analyzes obesity levels based on various factors such as gender, physical activity, high-calorie food intake, and family history with overweight. The dataset is obtained from Kaggle, containing 2111 entries and 17 columns, covering different lifestyle habits, BMI categories, and demographic details.

The analysis aims to identify patterns and trends in obesity through statistical summaries and visualizations.

📂 Dataset Description

The dataset includes the following features:
	•	Demographic Information: Gender, Age, Height, Weight
	•	Lifestyle Habits:
	•	FAF: Frequency of Physical Activity
	•	FAVC: High Calorie Food Consumption (Yes/No)
	•	SMOKE: Smoking Habit
	•	TUE: Time Using Technology Devices
	•	MTRANS: Mode of Transportation
	•	Obesity Indicators:
	•	NObeyesdad: Obesity Level (e.g., Normal Weight, Obesity Type I, II, III)
	•	family_history_with_overweight: Presence of overweight individuals in the family (Yes/No)

 📊 Exploratory Data Analysis

We conducted various analyses to understand how different factors correlate with obesity levels. Below are the key findings:

1️⃣ Obesity Level Distribution
	•	Analysis: The first graph represents the overall distribution of obesity levels in the dataset.
![Obesity Level Distribution](Obesity%20Analysis%20Results/distribution%20of%20obesity%20levels%20--bar.png)
	•	Key Insight:
	•	Most individuals fall into Obesity Type I and Type III categories, while the number of insufficient weight individuals is significantly lower.
	•	The dataset is not normally distributed but is skewed towards overweight and obesity.

 2️⃣ Obesity Levels by Gender
	•	Analysis: A stacked bar chart shows the distribution of obesity levels between males and females.
![Obesity Level by Gender](Obesity%20Analysis%20Results/obesity%20level%20distribution%20by%20gender.png)
	•	Key Insight:
	•	Males have a higher proportion of obesity in Type I and Type II.
	•	Females tend to have a higher normal weight ratio but still contribute significantly to the overweight and obesity categories.

 3️⃣ Obesity Levels by Family History with Overweight
	•	Analysis: This visualization categorizes obesity levels based on whether individuals have a family history of overweight.
![Obesity Levels by Family History](Obesity%20Analysis%20Results/obesity%20levels%20by%20family%20history%20with%20overweight.png)
	•	Key Insight:
	•	Individuals with a family history of obesity have a significantly higher rate of severe obesity.
	•	People without an overweight family history mostly fall into Normal Weight or Overweight Level I.

 4️⃣ Obesity Levels by High Calorie Food Intake
	•	Analysis: This graph shows how frequently consuming high-calorie foods affects obesity.
![Obesity Levels by High Calorie Food Intake](Obesity%20Analysis%20Results/Obesity%20levels%20by%20high%20calorie%20food%20intake.png)
	•	Key Insight:
	•	People who consume high-calorie foods are far more likely to be in the Obesity Type II and Type III categories.
	•	Those who do not consume high-calorie foods are mostly normal weight or slightly overweight.

 5️⃣ Obesity Levels by Physical Activity
	•	Analysis: A categorized stacked bar chart showing how physical activity levels (low, medium, high) impact obesity.
![Obesity Levels by Physical Activity](Obesity%20Analysis%20Results/obesity%20levels%20by%20physical%20activity%20level.png)
	•	Key Insight:
	•	Individuals with low physical activity show the highest rates of Obesity Type I, II, and III.
	•	Higher physical activity levels correlate with a decrease in obesity rates and an increase in normal weight individuals.


 🚀 Conclusion

📌 Key Takeaways:
	1.	Obesity is highly prevalent in the dataset, with Obesity Type I and Type III being the most common.
	2.	Family history of overweight significantly increases obesity risk.
	3.	Frequent consumption of high-calorie food is strongly associated with obesity.
	4.	Low physical activity levels lead to a higher obesity rate, while higher activity levels correlate with lower obesity.
	5.	Males tend to have higher obesity rates, while females are more likely to fall into the normal weight category.

 🏆 Future Work

🔹 Exploring Machine Learning Approaches to predict obesity levels.
🔹 Analyzing dietary habits and caloric intake in more detail.
🔹 Studying socioeconomic and geographical factors affecting obesity.

🔗 References
	•	Dataset Source: Kaggle - Obesity Data Set(https://www.kaggle.com/datasets/lesumitkumarroy/obesity-data-set)
	•	Documentation & Analysis: Python, Pandas, Matplotlib
