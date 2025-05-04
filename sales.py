import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# Step 1: Load CSV data
df = pd.read_csv("C:/Users/abhishek pandey/Downloads/Task 7/groceries.csv")

# Step 2: Create SQLite DB and insert data
conn = sqlite3.connect("sales_data.db")
df.to_sql("sales", conn, if_exists="replace", index=False)

# Step 3: SQL query for summary
query = """
SELECT product, 
       SUM(quantity) AS total_qty, 
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""

summary_df = pd.read_sql_query(query, conn)

# Step 4: Display summary
print("Sales Summary:\n")
print(summary_df)

# Step 5: Plot bar chart for revenue
plt.figure(figsize=(10, 6))
summary_df.plot(kind="bar", x="product", y="revenue", legend=False)
plt.title("Revenue by Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

# Step 6: Close connection
conn.close()
