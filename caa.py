# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the dataset (make sure the CSV file is in the same folder)
df = pd.read_csv(r'D:\data clean\customer_shopping_data (2).csv')


"""#Objective-1
plt.figure(figsize=(18, 5))

# Age
plt.subplot(1, 3, 1)
sns.histplot(df['age'], kde=True, color='skyblue')
plt.title('Age Distribution')

# Quantity
plt.subplot(1, 3, 2)
sns.histplot(df['quantity'], kde=True, color='lightgreen')
plt.title('Quantity Distribution')

# Price
plt.subplot(1, 3, 3)
sns.histplot(df['price'], kde=True, color='salmon')
plt.title('Price Distribution')

plt.tight_layout()
plt.show() """

"""#Objective-2

correlation_data = df[['age', 'quantity', 'price']]

# Compute correlation matrix
correlation_matrix = correlation_data.corr()

# Display the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)

# Plot the heatmap
plt.figure(figsize=(6, 4))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", square=True)
plt.title("Correlation Between Age, Quantity, and Price")
plt.tight_layout()
plt.show()  """

"""#Objective-3

# Boxplot visualization for outliers
plt.figure(figsize=(12, 5))

# Quantity Outliers
plt.subplot(1, 2, 1)
sns.boxplot(x=df['quantity'], color='lightblue')
plt.title("Outlier Detection - Quantity")

# Price Outliers
plt.subplot(1, 2, 2)
sns.boxplot(x=df['price'], color='lightcoral')
plt.title("Outlier Detection - Price")

plt.tight_layout()
plt.show()  """

"""#Objective-4

# Group by category for average price and total quantity
category_summary = df.groupby('category').agg(
    avg_spending=('price', 'mean'),
    total_quantity=('quantity', 'sum')
).reset_index()

# Plot: Average Spending per Category
plt.figure(figsize=(14, 5))

plt.subplot(1, 2, 1)
sns.barplot(data=category_summary, x='category', y='avg_spending', palette='Set2')
plt.title('Average Spending per Category')
plt.ylabel('Average Price (₹)')
plt.xlabel('Category')
plt.xticks(rotation=15)

# Plot: Total Quantity per Category
plt.subplot(1, 2, 2)
sns.barplot(data=category_summary, x='category', y='total_quantity', palette='Set3')
plt.title('Total Quantity Purchased per Category')
plt.ylabel('Total Quantity')
plt.xlabel('Category')
plt.xticks(rotation=15)

plt.tight_layout()
plt.show()"""

"""#Objective-5
# Convert invoice_date to datetime format
df['invoice_date'] = pd.to_datetime(df['invoice_date'], dayfirst=True)

# Extract month for aggregation
df['month'] = df['invoice_date'].dt.to_period('M').dt.to_timestamp()

# Group by month
monthly_summary = df.groupby('month').agg(
    total_sales=('price', 'sum'),
    total_quantity=('quantity', 'sum')
).reset_index()

# Plotting time series trends
plt.figure(figsize=(14, 6))

sns.lineplot(data=monthly_summary, x='month', y='total_sales', marker='o', label='Total Sales (₹)', color='blue')
sns.lineplot(data=monthly_summary, x='month', y='total_quantity', marker='o', label='Total Quantity Sold', color='green')

plt.title("Monthly Shopping Trends: Sales & Quantity")
plt.xlabel("Month")
plt.ylabel("Amount / Quantity")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show() """

"""#Objective-6

# Set up figure size
plt.figure(figsize=(18, 5))

# Gender distribution pie chart
plt.subplot(1, 3, 1)
gender_counts = df['gender'].value_counts()
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, colors=['lightblue', 'pink'])
plt.title("Gender Distribution")

# Category distribution pie chart
plt.subplot(1, 3, 2)
category_counts = df['category'].value_counts()
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Product Category Distribution")

# Payment method distribution pie chart
plt.subplot(1, 3, 3)
payment_counts = df['payment_method'].value_counts()
plt.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', startangle=140)
plt.title("Payment Method Distribution")

plt.tight_layout()
plt.show()    """
