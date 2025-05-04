# 🛒 Grocery Sales Summary with SQLite and Matplotlib

This project analyzes a grocery sales dataset (`groceries.csv`) and provides a visual summary of product-wise revenue using **SQLite** for data storage and **Matplotlib** for plotting.

---

## 📌 Summary

The script reads sales data, stores it in an SQLite database, and performs an SQL aggregation query to calculate:

- Total quantity sold per product
- Total revenue generated per product (`quantity × price`)

The result is printed and visualized as a bar chart.

---

## 📂 Files

- `sales.py` – Main Python script for processing and visualization
- `groceries.csv` – Input dataset containing product sales
- `sales_chart.png` – Output chart showing revenue by product
- `sales_data.db` – SQLite database storing the sales table

---

## 🔧 Technologies Used

- Python 🐍
- Pandas 📊
- SQLite3 🛢
- Matplotlib 📈

---

## 💡 SQL Query Used

```sql
SELECT product, 
       SUM(quantity) AS total_qty, 
       SUM(quantity * price) AS revenue
FROM sales
GROUP BY product;
```

---

## 📊 Output (Sample)

A bar chart is generated that visually compares the revenue across different products.

---

## ▶️ How to Run

1. Place `sales.py` and `groceries.csv` in the same folder.
2. Install requirements if needed:

```bash
pip install pandas matplotlib
```

3. Run the script:

```bash
python sales.py
```

4. The script will:
   - Create `sales_data.db`
   - Print a product-wise revenue summary
   - Save a chart as `sales_chart.png`

---

## 👨‍💻 Author

**Abhishek Pandey**  
Sales Data Analytics Project – 2025

