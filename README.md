# AI‑Powered Business Decision Dashboard

An interactive Flask‑based dashboard for the **Superstore Sales dataset**, with filters, KPIs, charts, and CSV export.

---

## 📌 Features

- **Interactive filters**:
  - Region  
  - Category  
  - Date range (From / To)
- **Key KPI Cards**:
  - Total Sales  
  - Total Profit  
  - Total Orders  
- **Interactive Charts**:
  - Profit by Region (Bar chart)  
  - Sales by Category (Pie chart)  
  - Monthly Sales Trend (Line chart)  
- **Click‑on‑bar filters**:
  - Click a region bar to auto‑apply that Region filter.
- **Export**:
  - Export currently filtered data as **CSV**.
- **Auto‑open browser** on startup (`run_dashboard.py`).

---

## 📂 Folder Structure
```
ai_business_dashboard/
├── run_dashboard.py
├── app.py
├── requirements.txt
├── data/
│   └── Superstore sales dataset.csv
├── templates/
│   └── dashboard.html
└── static/
    └── css/
        └── dashboard.css
```

---

## 🧩 Requirements

- Python ≥ 3.8  
- Dependencies:
  - `Flask`
  - `pandas`
  - `numpy`

Install with:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run

1. Place the Superstore sales CSV in `data/`:

   ```bash
   ai_business_dashboard/
   └── data/
       └── Superstore sales dataset.csv
   ```

2. Start the dashboard:

   ```bash
   python run_dashboard.py
   ```

3. Your browser will open automatically to `http://localhost:5000`.

4. Use the filters and **Apply Filters** button to see updated charts and KPIs.

5. Click **Export as CSV** to download the currently filtered data.

---

## 📊 Visualizations

- **Profit by Region (Bar)** – shows profit contribution by region.  
- **Sales by Category (Pie)** – shows revenue share across `Furniture`, `Office Supplies`, `Technology`.  
- **Monthly Sales Trend (Line)** – historical sales with a clean line chart.

---
## 📄 License
This project is licensed under the MIT License.

---

## 📄 Developed By

**Archita.B**  
B.TECH CSE'26  
Tech‑Driven Business Solutions Enthusiast