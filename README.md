# AI‑Powered Business Decision Dashboard

A Flask‑based interactive dashboard for analyzing the **Superstore Sales dataset** with filters, KPIs, and AI‑driven visualizations.

---

## 📌 Features

- **Interactive filters**:
  - Region  
  - Category  
  - Date range (From / To)
- **KPI Cards**:
  - Total Sales  
  - Total Profit  
  - Total Orders  
- **Interactive Charts**:
  - Profit by Region (Bar chart)  
  - Sales by Category (Pie chart)  
  - Monthly Sales Trend + **AI‑style forecast** (scikit‑learn)
- **Export**:
  - Export current filtered data as **CSV**
- **Auto‑open browser** on startup (`run_dashboard.py`)

---

## 📂 Folder Structure
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


---

## 🧩 Requirements

- Python ≥ 3.8  
- Dependencies:
  - `Flask`
  - `pandas`
  - `numpy`
  - `scikit‑learn` (for forecasting)
  - `weasyprint` (optional, for future PDF export)

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

3. Your browser will open automatically to `http://localhost:5000` with the dashboard.

4. Use the filters and **Apply Filters** button to see updated charts and KPIs.

5. Click **Export as CSV** to download the currently filtered data.

---

## 📊 Visualizations

- **Profit by Region (Bar)** – shows profit contribution by region.  
- **Sales by Category (Pie)** – shows revenue share across `Furniture`, `Office Supplies`, `Technology`.  
- **Monthly Sales Trend + Forecast (Line)** – historical sales plus a **scikit‑learn linear regression forecast** for next 3 months.

---

## 🤖 AI‑Powered Forecasting

- The dashboard uses **LinearRegression from scikit‑learn** to forecast monthly sales based on historical data.  
- The line chart shows:
  - Past sales (solid line)  
  - Forecast (dashed line) with a simple `next 3 months` prediction.

---

## 💾 Export Features

- **Export as CSV**:
  - A `/export/csv` route returns a download of the **filtered data** (by Region, Category, Date range).  
  - Useful for audit, reporting, or feeding into other tools.

---

## 🛠️ Future Work

Planned enhancements (can be added later):

- **Export as PDF** (using `weasyprint` or similar) for printable reports.  
- **Click‑on‑bar filters** (e.g., click on a region bar → auto‑apply that filter).  
- **Real‑time KPI updates** (e.g., rolling 3‑month averages, customer‑segments).

---

## 📄 Developed By

**Archita.B**  
B.TECH CSE'26  
Tech‑Driven Business Solutions Enthusiast