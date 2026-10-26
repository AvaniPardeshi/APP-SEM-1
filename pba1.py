import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

print("Total Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())

print("Month with highest sales:")
print(df.loc[df["Sales"].idxmax()])

print("\nSales by Product Category:")
print(df.groupby("Category")["Sales"].sum())

df.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Category")
plt.show()

df.groupby("Month")["Sales"].sum().plot(kind="line")
plt.title("Monthly Sales Trend")
plt.show()

df.groupby("Category")["Sales"].sum().plot(kind="pie", autopct="%1.1f%%")
plt.title("Category-wise Sales")
plt.show()