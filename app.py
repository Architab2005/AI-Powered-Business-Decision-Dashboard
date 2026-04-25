from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__, template_folder="templates")

DATA_PATH = os.path.join("data", "Superstore sales dataset.csv")


@app.route("/")
def index():
    # Load data
    df = pd.read_csv(DATA_PATH)

    # Convert Order Date
    df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)

    # --- Filters ---
    selected_region = request.args.get("region", None)
    selected_category = request.args.get("category", None)
    from_date = request.args.get("from_date", None)
    to_date = request.args.get("to_date", None)

    df_filtered = df.copy()

    if selected_region:
        df_filtered = df_filtered[df_filtered["Region"] == selected_region]
    if selected_category:
        df_filtered = df_filtered[df_filtered["Category"] == selected_category]
    if from_date:
        df_filtered = df_filtered[
            df_filtered["Order Date"] >= pd.to_datetime(from_date)
        ]
    if to_date:
        df_filtered = df_filtered[
            df_filtered["Order Date"] <= pd.to_datetime(to_date)
        ]

    # KPIs
    total_sales = df_filtered["Sales"].sum()
    total_profit = df_filtered["Profit"].sum()
    total_orders = df_filtered["Order ID"].nunique()

    # Profit by Region
    region_profit = (
        df_filtered.groupby("Region")["Profit"]
        .sum()
        .round(2)
        .to_dict()
    )
    region_labels = list(region_profit.keys())
    region_values = list(region_profit.values())

    # Monthly Sales
    df_filtered["Month"] = df_filtered["Order Date"].dt.to_period("M")
    monthly_sales = df_filtered.groupby("Month")["Sales"].sum()

    monthly_labels = [str(period) for period in monthly_sales.index]
    monthly_values = [float(val) for val in monthly_sales.values]

    # Dropdown options
    regions = sorted(df["Region"].unique())
    categories = sorted(df["Category"].unique())

    return render_template(
        "dashboard.html",
        total_sales=total_sales,
        total_profit=total_profit,
        total_orders=total_orders,
        region_labels=region_labels,
        region_values=region_values,
        monthly_labels=monthly_labels,
        monthly_values=monthly_values,
        regions=regions,
        categories=categories,
        selected_region=selected_region,
        selected_category=selected_category,
        from_date=from_date,
        to_date=to_date,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)