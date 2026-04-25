# AI‑Powered Business Decision Dashboard

A **Flask‑based interactive dashboard** for exploring the **Superstore Sales dataset**, with filters, KPIs, and visualizations for business decisions.

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
  - Monthly Sales Trend (Line chart)  
- **Auto‑open browser** on startup (`run_dashboard.py`)

---

## 📂 Folder Structure
ai_business_dashboard/
├── run_dashboard.py # Start Flask + auto‑open browser
├── app.py           # Flask backend (loads CSV, filters, KPIs, charts data)
├── requirements.txt # Python dependencies
├── data/
│ └── Superstore sales dataset.csv
├── templates/
│ └── dashboard.html # HTML + JS charts (no external JS needed)
└── static/
└── css/
└── dashboard.css    # Responsive styling for dashboard


---

## 🧩 Requirements

- Python ≥ 3.8  
- Packages: `Flask`, `pandas`, `numpy`

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

3. Your browser will **open automatically** to `http://localhost:5000` with the dashboard.

---

## 🎨 Interactivity

- Use the **filters** (Region, Category, From Date, To Date) → click **Apply** to reload data.  
- Charts update automatically with:
  - Hover tooltips  
  - Readable labels and smooth lines  
- CSS is responsive: on small screens, charts stack vertically.

---

## 🔧 Customization Ideas

- Add **Sales by Category (Pie)**.  
- Integrate **scikit‑learn models** (e.g., monthly sales forecasting).  
- Add export buttons (CSV / PDF of filtered data).  

---

## 📄 Developed By

**Archita.B**  
B.TECH CSE’26  
Tech‑Driven Business Solutions Enthusiast