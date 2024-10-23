import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('assesments/vgsales.csv')
print(data.info())
# Step 1: Handle missing values
# either we can use same threshold value like 15% or we can fill all with mean or median values
# For 'Year', we will fill missing values with the median year of release
data['Year'] = data['Year'].fillna(data['Year'].median())

# For 'Publisher', we will fill missing values with the mode (most frequent publisher)
data['Publisher'] = data['Publisher'].fillna(data['Publisher'].mode()[0])

# Step 2: Convert 'Year' column to integer values
data['Year'] = data['Year'].astype(int)

# Step 3: Find the Top 10 Publishers by Sales in North America
top_publishers_na = data.groupby('Publisher')['NA_Sales'].sum().sort_values(ascending=False).head(10)

# Display the top 10 publishers in North America
print("\nTop 10 publishers by sales in North America:")
print(top_publishers_na)

# Step 4: Create publisher-wise line plots for sales across different regions and globally

# Group the data by Publisher and aggregate the sales for each region
publisher_sales = data.groupby('Publisher')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']].sum()

# Plot the sales data
plt.figure(figsize=(12, 8))
publisher_sales.plot(kind='line', figsize=(12, 8))
plt.title('Publisher-wise Total Units Sold Across Regions')
plt.xlabel('Publisher')
plt.ylabel('Units Sold (in millions)')
plt.xticks(rotation=90)
plt.show()

# Step 5: Find the video game publisher that sells the most units globally
top_global_publisher = data.groupby('Publisher')['Global_Sales'].sum().idxmax()
max_global_sales = data.groupby('Publisher')['Global_Sales'].sum().max()

print(f"\nPublisher with the most global sales: {top_global_publisher}")
print(f"Total global units sold: {max_global_sales} million")

