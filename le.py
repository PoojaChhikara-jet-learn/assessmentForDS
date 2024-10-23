import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv('assesments/LifeExpectancy.csv')

print(data.columns)

# Step 1: Rename columns by removing leading and trailing spaces
data.columns = data.columns.str.strip()

print(data.columns)

# Step 2: Identify columns with missing values
# print(data.info())

# identifying and getting total missing values
missing_values = data.isnull().sum()
print(missing_values)
print("\nColumns with missing values and the count is:")
print(missing_values[missing_values > 0])

# Step 3: Drop columns with more than 15% missing values
threshold = 0.15 * len(data)  # 15% threshold
# index is required else it will throw error bcz .drop require col names not entire series
columns_to_drop = missing_values[missing_values > threshold].index
data = data.drop(columns=columns_to_drop)
print(f"\nDropped columns: {list(columns_to_drop)}")



# Step 4: Replace remaining missing values with the median
# only numeric one we will pick now
# data.fillna(data.median(), inplace=True)
# Step 1: Fill missing values with median for numeric columns only
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].median())

# Step 2: For categorical columns, fill missing values with the mode (most frequent value)
categorical_columns = data.select_dtypes(include=['object']).columns
data[categorical_columns] = data[categorical_columns].fillna(data[categorical_columns].mode().iloc[0])

print("Missing values handled.")


# Step 5: Create a bar plot for average life expectancy between 2000 and 2015
period_data = data[(data['Year'] >= 2000) & (data['Year'] <= 2015)]
avg_life_expectancy = period_data.groupby('Year')['Life expectancy'].mean()
print(avg_life_expectancy)

# Plotting the bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x=avg_life_expectancy.index, y=avg_life_expectancy.values, palette="Blues_d")
plt.title('Average Global Life Expectancy (2000-2015)')
plt.xlabel('Year')
plt.ylabel('Average Life Expectancy')
plt.xticks(rotation=45)
plt.show()

# Step 6: Find the year with maximum life expectancy
max_life_expectancy_year = data.groupby('Year')['Life expectancy'].mean().idxmax()
print(f"\nYear with maximum average life expectancy: {max_life_expectancy_year}")

# Step 7: Create a bar plot for yearly life expectancy of developing and developed countries
life_expectancy_by_status = data.groupby(['Year', 'Status'])['Life expectancy'].mean().unstack()

# Plotting
plt.figure(figsize=(12, 6))
life_expectancy_by_status.plot(kind='bar', stacked=False, colormap='Paired', figsize=(12, 6))
plt.title('Life Expectancy for Developed vs Developing Countries (Yearly)')
plt.xlabel('Year')
plt.ylabel('Average Life Expectancy')
plt.legend(title='Country Status')
plt.xticks(rotation=45)
plt.show()