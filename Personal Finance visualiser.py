import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

print("=" * 60)
print("       💰 PERSONAL FINANCE VISUALISER")
print("=" * 60)

# ── DATASET ──────────────────────────────────────────────────
# 12 months of income and expense breakdown for a young professional

months_short = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Monthly income (salary + freelance)
salary     = [45000] * 12
freelance  = [0, 5000, 0, 8000, 0, 12000, 0, 0, 6000, 0, 15000, 0]
income     = [s + f for s, f in zip(salary, freelance)]

# Monthly expenses by category
rent       = [12000] * 12
food       = [4500, 4200, 5100, 4800, 5500, 6200, 4900, 4700, 5300, 5000, 6800, 7200]
transport  = [2200, 2100, 2300, 2000, 2400, 2200, 2100, 2300, 2200, 2500, 2100, 2000]
utilities  = [1800, 1700, 1500, 1200, 1100, 1400, 1600, 1700, 1500, 1300, 1600, 1900]
entertainment = [3000, 2500, 4000, 3500, 5000, 8000, 3000, 2800, 4500, 3200, 6000, 9000]
savings    = [3500, 4000, 3000, 5000, 2000, 0, 4000, 3500, 2000, 5000, 0, 0]
other      = [i - (r + f + t + u + e + s)
              for i, r, f, t, u, e, s
              in zip(income, rent, food, transport, utilities, entertainment, savings)]

total_expenses = [r + f + t + u + e + s + o
                  for r, f, t, u, e, s, o
                  in zip(rent, food, transport, utilities, entertainment, savings, other)]

net_savings_monthly = [inc - exp for inc, exp in zip(income, total_expenses)]

# ── STEP 1 — PRINT SUMMARY TABLE ─────────────────────────────
print("\n📋 MONTHLY INCOME vs EXPENSES")
print(f"  {'Month':<6} {'Income':>10} {'Expenses':>10} {'Net':>10} {'Status':>8}")
print("  " + "-" * 48)
for i, m in enumerate(months_short):
    net    = net_savings_monthly[i]
    status = "✅" if net >= 0 else "🔴"
    print(f"  {m:<6} ₹{income[i]:>8,}  ₹{total_expenses[i]:>8,}  "
          f"{'₹' + f'{net:,}' if net >= 0 else '-₹' + f'{abs(net):,}':>10}  {status}")

print(f"\n  Annual Income   : ₹{sum(income):,}")
print(f"  Annual Expenses : ₹{sum(total_expenses):,}")
print(f"  Annual Net      : ₹{sum(net_savings_monthly):,}")
print(f"  Savings Rate    : {sum(savings)/sum(income)*100:.1f}%")

# ── STEP 2 — BUILD 4-PANEL DASHBOARD ─────────────────────────
print("\n🎨 Building 4-panel financial dashboard...")

fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle("Personal Finance Dashboard — Full Year Overview",
            fontsize=15, fontweight="bold")
fig.patch.set_facecolor("#f8f9fa")

# ─ Panel 1: Income vs Expenses Line Chart (top-left) ─────────
ax1 = axes[0, 0]
x   = range(len(months_short))
ax1.plot(x, income, color="#27ae60", linewidth=2.5,
        marker="o", markersize=6, label="Income")
ax1.plot(x, total_expenses, color="#e74c3c", linewidth=2.5,
        marker="s", markersize=6, label="Expenses")
ax1.fill_between(x, income, total_expenses,
                where=[inc > exp for inc, exp in zip(income, total_expenses)],
                alpha=0.15, color="#27ae60", label="Surplus")
ax1.fill_between(x, income, total_expenses,
                where=[inc <= exp for inc, exp in zip(income, total_expenses)],
                alpha=0.15, color="#e74c3c", label="Deficit")
ax1.set_title("Income vs Expenses", fontweight="bold")
ax1.set_xticks(x)
ax1.set_xticklabels(months_short, fontsize=8)
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"₹{int(v/1000)}K"))
ax1.legend(fontsize=8)
ax1.grid(alpha=0.3)
ax1.set_facecolor("white")

# ─ Panel 2: Stacked Bar — Expense Breakdown (top-right) ──────
ax2 = axes[0, 1]
bottoms = np.zeros(12)
categories_data = {
    "Rent"         : (rent,          "#e74c3c"),
    "Food"         : (food,          "#e67e22"),
    "Transport"    : (transport,     "#f1c40f"),
    "Utilities"    : (utilities,     "#1abc9c"),
    "Entertainment": (entertainment, "#9b59b6"),
    "Savings"      : (savings,       "#27ae60"),
    "Other"        : (other,         "#95a5a6"),
}
for label, (values, color) in categories_data.items():
    ax2.bar(months_short, values, bottom=bottoms,
            color=color, label=label, edgecolor="white", linewidth=0.5)
    bottoms += np.array(values)
ax2.set_title("Monthly Expense Breakdown (Stacked)", fontweight="bold")
ax2.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"₹{int(v/1000)}K"))
ax2.legend(fontsize=7, loc="upper left", ncol=2)
ax2.tick_params(axis="x", labelsize=8)
ax2.set_facecolor("white")

# ─ Panel 3: Pie — Annual Spending by Category (bottom-left) ──
ax3 = axes[1, 0]
annual_cat = {
    "Rent"         : sum(rent),
    "Food"         : sum(food),
    "Transport"    : sum(transport),
    "Utilities"    : sum(utilities),
    "Entertainment": sum(entertainment),
    "Savings"      : sum(savings),
    "Other"        : sum(other),
}
# Only show categories with non-zero spend
filtered = {k: v for k, v in annual_cat.items() if v > 0}
colors_pie = ["#e74c3c", "#e67e22", "#f1c40f", "#1abc9c", "#9b59b6", "#27ae60", "#95a5a6"]

wedges, texts, autotexts = ax3.pie(
    filtered.values(),
    labels      = filtered.keys(),
    autopct     = "%1.1f%%",
    colors      = colors_pie[:len(filtered)],
    startangle  = 140,
    pctdistance = 0.75,
)
for text in autotexts:
    text.set_fontsize(8)
ax3.set_title("Annual Spend by Category", fontweight="bold")

# ─ Panel 4: Bar — Monthly Net Savings (bottom-right) ─────────
ax4 = axes[1, 1]
bar_colors = ["#27ae60" if v >= 0 else "#e74c3c" for v in net_savings_monthly]
bars = ax4.bar(months_short, net_savings_monthly, color=bar_colors, edgecolor="white")
ax4.axhline(0, color="black", linewidth=1)
ax4.set_title("Monthly Net Savings / Deficit", fontweight="bold")
ax4.yaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"₹{int(v/1000)}K"))
ax4.tick_params(axis="x", labelsize=8)
ax4.set_facecolor("white")

# Annotate bars
for bar, val in zip(bars, net_savings_monthly):
    label = f"₹{val//1000}K" if abs(val) >= 1000 else f"₹{val}"
    ypos  = bar.get_height() + 200 if val >= 0 else bar.get_height() - 800
    ax4.text(bar.get_x() + bar.get_width() / 2, ypos,
            label, ha="center", fontsize=7, fontweight="bold")

plt.tight_layout()
plt.savefig("finance_dashboard.png", dpi=150, bbox_inches="tight")
print("  ✅ Saved: finance_dashboard.png")
plt.show()

# ── STEP 3 — KEY INSIGHTS ─────────────────────────────────────
print("\n" + "=" * 60)
print("📌 KEY FINANCIAL INSIGHTS")
print("=" * 60)
worst_month  = months_short[net_savings_monthly.index(min(net_savings_monthly))]
best_month   = months_short[net_savings_monthly.index(max(net_savings_monthly))]
highest_exp  = months_short[total_expenses.index(max(total_expenses))]

print(f"  • Best savings month   : {best_month} (₹{max(net_savings_monthly):,})")
print(f"  • Worst month (deficit): {worst_month} (₹{min(net_savings_monthly):,})")
print(f"  • Highest spending month: {highest_exp} (₹{max(total_expenses):,})")
print(f"  • Entertainment spend  : ₹{sum(entertainment):,} ({sum(entertainment)/sum(income)*100:.1f}% of income)")
print(f"  • Actual savings rate  : {sum(savings)/sum(income)*100:.1f}%")
print(f"  • Months in deficit    : {sum(1 for n in net_savings_monthly if n < 0)}")
print("=" * 60)

print("\n💡 CHALLENGE:")
print("  1. Add a 5th panel showing cumulative savings over the year.")
print("  2. Calculate what happens if entertainment is capped at ₹4,000/month.")
print("  3. Which 3 months had the highest entertainment-to-income ratio?")
print("  4. Add a horizontal 'target savings' line at ₹5,000/month in Panel 4.")
print()