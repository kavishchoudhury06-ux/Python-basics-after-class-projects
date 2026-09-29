import pandas as pd
import numpy as np

print("=" * 62)
print("       🛒 RETAIL SALES PROCESSOR — PANDAS DEEP DIVE")
print("=" * 62)

# ── DATASET ──────────────────────────────────────────────────
# 40 sales transactions across 4 stores, 5 product categories

np.random.seed(7)

categories = ["Electronics", "Clothing", "Groceries", "Books", "Sports"]
stores     = ["Store_A", "Store_B", "Store_C", "Store_D"]
months     = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Build 60 realistic transactions
records = []
for _ in range(60):
    store    = np.random.choice(stores)
    category = np.random.choice(categories)
    month    = np.random.choice(months)
    units    = int(np.random.randint(5, 120))
    price    = round(float(np.random.uniform(10, 500)), 2)
    discount = round(float(np.random.choice([0, 0, 0.05, 0.10, 0.15, 0.20])), 2)
    records.append({
        "Store"     : store,
        "Category"  : category,
        "Month"     : month,
        "Units_Sold": units,
        "Unit_Price": price,
        "Discount"  : discount,
    })

sales = pd.DataFrame(records)

# ── STEP 1 — EXPLORE THE DATA ─────────────────────────────────
print("\n📋 STEP 1 — RAW DATA SNAPSHOT")
print(f"  Shape   : {sales.shape[0]} rows × {sales.shape[1]} columns")
print(f"  Columns : {list(sales.columns)}")
print(f"\n  First 5 rows:")
print(sales.head().to_string(index=False))
print(f"\n  Data types:")
for col, dtype in sales.dtypes.items():
    print(f"    {col:<15}: {dtype}")

# ── STEP 2 — DERIVED COLUMNS ──────────────────────────────────
print("\n🧮 STEP 2 — CALCULATING REVENUE")
print("-" * 50)

# Revenue = Units × Price × (1 - Discount)
sales["Gross_Revenue"] = sales["Units_Sold"] * sales["Unit_Price"]
sales["Net_Revenue"]   = (sales["Units_Sold"] * sales["Unit_Price"]
                          * (1 - sales["Discount"])).round(2)
sales["Discount_Amt"]  = (sales["Gross_Revenue"] - sales["Net_Revenue"]).round(2)

print(f"  Total Gross Revenue : ₹{sales['Gross_Revenue'].sum():>12,.2f}")
print(f"  Total Discounts     : ₹{sales['Discount_Amt'].sum():>12,.2f}")
print(f"  Total Net Revenue   : ₹{sales['Net_Revenue'].sum():>12,.2f}")
print(f"  Avg Transaction     : ₹{sales['Net_Revenue'].mean():>12,.2f}")

# ── STEP 3 — STORE PERFORMANCE ────────────────────────────────
print("\n🏪 STEP 3 — STORE PERFORMANCE")
print("-" * 58)

store_stats = sales.groupby("Store").agg(
    Transactions  = ("Net_Revenue", "count"),
    Total_Revenue = ("Net_Revenue", "sum"),
    Avg_Revenue   = ("Net_Revenue", "mean"),
    Total_Units   = ("Units_Sold", "sum"),
).round(2)

store_stats = store_stats.sort_values("Total_Revenue", ascending=False)
store_stats["Rank"] = range(1, len(store_stats) + 1)

print(f"  {'Store':<10} {'Txns':>6} {'Total Rev':>14} {'Avg Rev':>11} {'Units':>8} {'Rank':>5}")
print("  " + "-" * 56)
for store, row in store_stats.iterrows():
    print(f"  {store:<10} {int(row['Transactions']):>6} "
          f"₹{row['Total_Revenue']:>12,.2f} "
          f"₹{row['Avg_Revenue']:>9,.2f} "
          f"{int(row['Total_Units']):>8} "
          f"  #{int(row['Rank'])}")

top_store = store_stats.index[0]
print(f"\n  🏆 Best performing store: {top_store} "
      f"(₹{store_stats.loc[top_store, 'Total_Revenue']:,.2f})")

# ── STEP 4 — CATEGORY ANALYSIS ────────────────────────────────
print("\n📦 STEP 4 — CATEGORY ANALYSIS")
print("-" * 58)

cat_stats = sales.groupby("Category").agg(
    Total_Revenue = ("Net_Revenue", "sum"),
    Avg_Discount  = ("Discount", "mean"),
    Units_Sold    = ("Units_Sold", "sum"),
).round(2)

cat_stats["Revenue_Share_%"] = (
    cat_stats["Total_Revenue"] / cat_stats["Total_Revenue"].sum() * 100
).round(1)
cat_stats = cat_stats.sort_values("Total_Revenue", ascending=False)

print(f"  {'Category':<14} {'Total Rev':>13} {'Rev Share':>10} {'Avg Disc':>9} {'Units':>7}")
print("  " + "-" * 56)
for cat, row in cat_stats.iterrows():
    bar = "█" * int(row["Revenue_Share_%"] / 2)
    print(f"  {cat:<14} ₹{row['Total_Revenue']:>11,.2f} "
          f"  {row['Revenue_Share_%']:>5.1f}%  "
          f"  {row['Avg_Discount']*100:>5.1f}%  "
          f"{int(row['Units_Sold']):>7}  {bar}")

# ── STEP 5 — FILTER & QUERY ───────────────────────────────────
print("\n🔍 STEP 5 — SMART FILTERS")
print("-" * 50)

# High-value transactions: net revenue > 5000
high_value = sales[sales["Net_Revenue"] > 5000].sort_values(
    "Net_Revenue", ascending=False
)
print(f"  High-value transactions (>₹5,000): {len(high_value)}")
if len(high_value) > 0:
    print(f"  Top 3 high-value transactions:")
    for _, row in high_value.head(3).iterrows():
        print(f"    • {row['Store']} | {row['Category']} | "
              f"{row['Units_Sold']} units | ₹{row['Net_Revenue']:,.2f}")

# Discount analysis
heavily_discounted = sales[sales["Discount"] >= 0.15]
print(f"\n  Heavily discounted (≥15% off): {len(heavily_discounted)} transactions")
print(f"  Revenue lost to discounts: ₹{heavily_discounted['Discount_Amt'].sum():,.2f}")

# Best month per store
print(f"\n  Transactions with no discount: "
      f"{len(sales[sales['Discount'] == 0])}")

# ── STEP 6 — PIVOT TABLE ──────────────────────────────────────
print("\n📊 STEP 6 — STORE × CATEGORY PIVOT (Net Revenue)")
print("-" * 62)

pivot = sales.pivot_table(
    values  = "Net_Revenue",
    index   = "Store",
    columns = "Category",
    aggfunc = "sum",
    fill_value = 0,
).round(0)

# Print pivot nicely
header = f"  {'Store':<10}" + "".join(f"{c:>14}" for c in pivot.columns)
print(header)
print("  " + "-" * (10 + 14 * len(pivot.columns)))
for store in pivot.index:
    row_str = f"  {store:<10}"
    for cat in pivot.columns:
        row_str += f"₹{int(pivot.loc[store, cat]):>12,}"
    row_str += f"  → ₹{int(pivot.loc[store].sum()):,}"
    print(row_str)

# ── STEP 7 — EXPORT ───────────────────────────────────────────
print("\n💾 STEP 7 — EXPORTING RESULTS")

# Full processed sales
sales.to_csv("processed_sales.csv", index=False)
print("  ✅ Saved: processed_sales.csv")

# Store summary
store_stats.to_csv("store_summary.csv")
print("  ✅ Saved: store_summary.csv")

# Category summary
cat_stats.to_csv("category_summary.csv")
print("  ✅ Saved: category_summary.csv")

# ── SUMMARY ──────────────────────────────────────────────────
print("\n" + "=" * 62)
print(f"  Total transactions analysed : {len(sales)}")
print(f"  Net revenue generated       : ₹{sales['Net_Revenue'].sum():,.2f}")
print(f"  Best store                  : {store_stats.index[0]}")
print(f"  Best category               : {cat_stats.index[0]}")
print(f"  Highest single sale         : ₹{sales['Net_Revenue'].max():,.2f}")
print(f"  Most units sold in one txn  : {sales['Units_Sold'].max()}")
print("=" * 62)

