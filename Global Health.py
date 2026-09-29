import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

print("=" * 62)
print("    🌍 GLOBAL HEALTH SNAPSHOT — FULL DATA PIPELINE")
print("=" * 62)

# ── STEP 1 — GENERATE DATASET ────────────────────────────────
# Realistic health metrics for 20 countries (2015–2023)

np.random.seed(99)

countries = [
    "India", "China", "USA", "Brazil", "Germany",
    "Japan", "Nigeria", "UK", "Australia", "Canada",
    "South Africa", "France", "Mexico", "Indonesia", "Pakistan",
    "Bangladesh", "Russia", "Egypt", "Kenya", "Argentina",
]
regions = {
    "India": "Asia", "China": "Asia", "Japan": "Asia", "Indonesia": "Asia", "Pakistan": "Asia",
    "Bangladesh": "Asia",
    "USA": "Americas", "Brazil": "Americas", "Canada": "Americas", "Mexico": "Americas",
    "Argentina": "Americas",
    "Germany": "Europe", "UK": "Europe", "France": "Europe", "Russia": "Europe",
    "Nigeria": "Africa", "South Africa": "Africa", "Egypt": "Africa", "Kenya": "Africa",
    "Australia": "Oceania",
}

# Base health metrics (realistic approximate values)
base_life_exp = {
    "India": 69, "China": 77, "USA": 79, "Brazil": 75, "Germany": 81,
    "Japan": 84, "Nigeria": 55, "UK": 81, "Australia": 83, "Canada": 82,
    "South Africa": 64, "France": 82, "Mexico": 75, "Indonesia": 71, "Pakistan": 67,
    "Bangladesh": 72, "Russia": 73, "Egypt": 72, "Kenya": 66, "Argentina": 77,
}
base_gdp_per_cap = {
    "India": 2100, "China": 10500, "USA": 63000, "Brazil": 8900, "Germany": 46000,
    "Japan": 40000, "Nigeria": 2200, "UK": 41000, "Australia": 55000, "Canada": 47000,
    "South Africa": 6500, "France": 42000, "Mexico": 10000, "Indonesia": 4100, "Pakistan": 1500,
    "Bangladesh": 1900, "Russia": 11000, "Egypt": 3500, "Kenya": 1800, "Argentina": 9600,
}
base_health_spend_pct = {
    "India": 3.5, "China": 5.4, "USA": 17.1, "Brazil": 9.5, "Germany": 11.7,
    "Japan": 10.9, "Nigeria": 3.8, "UK": 10.0, "Australia": 9.3, "Canada": 10.8,
    "South Africa": 8.1, "France": 11.1, "Mexico": 5.5, "Indonesia": 2.9, "Pakistan": 3.1,
    "Bangladesh": 2.3, "Russia": 5.6, "Egypt": 4.9, "Kenya": 4.7, "Argentina": 9.0,
}

years = list(range(2015, 2024))

records = []
for country in countries:
    for i, year in enumerate(years):
        life_exp   = round(base_life_exp[country] + i * 0.15 + np.random.normal(0, 0.3), 1)
        gdp        = round(base_gdp_per_cap[country] * (1 + 0.025 * i + np.random.normal(0, 0.01)), 0)
        health_pct = round(base_health_spend_pct[country] + np.random.normal(0, 0.2), 1)
        # Derived: doctors per 1000 (correlated with GDP)
        doctors    = round(max(0.1, gdp / 20000 * 3.5 + np.random.normal(0, 0.2)), 2)
        records.append({
            "Country"        : country,
            "Region"         : regions[country],
            "Year"           : year,
            "Life_Expectancy": life_exp,
            "GDP_Per_Capita" : gdp,
            "Health_Spend_%" : health_pct,
            "Doctors_Per_1K" : doctors,
        })

df = pd.DataFrame(records)

print(f"\n📂 STEP 1: Dataset created")
print(f"   Shape      : {df.shape[0]} rows × {df.shape[1]} columns")
print(f"   Countries  : {len(countries)}")
print(f"   Years      : {years[0]}–{years[-1]}")
print(f"\n   Sample (5 rows):")
print(df[df["Country"] == "India"].head().to_string(index=False))

# ── STEP 2 — INJECT & CLEAN MISSING VALUES ────────────────────
print("\n🧹 STEP 2 — DATA CLEANING")

# Inject 15 random NaN values
for _ in range(15):
    row_idx = np.random.randint(0, len(df))
    col     = np.random.choice(["Life_Expectancy", "GDP_Per_Capita", "Health_Spend_%"])
    df.loc[row_idx, col] = np.nan

print(f"   Missing values injected: {df.isnull().sum().sum()}")

# Clean: fill each numeric column with country-wise mean (more accurate than global mean)
for col in ["Life_Expectancy", "GDP_Per_Capita", "Health_Spend_%", "Doctors_Per_1K"]:
    null_count = df[col].isnull().sum()
    if null_count > 0:
        country_means = df.groupby("Country")[col].transform("mean")
        df[col].fillna(country_means.round(1), inplace=True)
        print(f"   Filled {null_count} NaN in '{col}' using country mean")

print(f"   After cleaning: {df.isnull().sum().sum()} nulls remaining ✅")

# ── STEP 3 — ANALYSE — 2023 SNAPSHOT ─────────────────────────
print("\n📊 STEP 3 — 2023 COUNTRY SNAPSHOT")
print("-" * 68)

df_2023 = df[df["Year"] == 2023].set_index("Country")

print(f"  {'Country':<16} {'Region':<10} {'Life Exp':>9} {'GDP/cap':>10} "
      f"{'Health%':>8} {'Doctors':>8}")
print("  " + "-" * 65)

df_2023_sorted = df_2023.sort_values("Life_Expectancy", ascending=False)
for country, row in df_2023_sorted.iterrows():
    print(f"  {country:<16} {row['Region']:<10} {row['Life_Expectancy']:>8.1f}  "
          f"${row['GDP_Per_Capita']:>8,.0f}  "
          f"{row['Health_Spend_%']:>6.1f}%  "
          f"{row['Doctors_Per_1K']:>7.2f}")

# ── STEP 4 — REGIONAL ANALYSIS ────────────────────────────────
print("\n🌏 STEP 4 — REGIONAL AVERAGES (2023)")
print("-" * 58)

regional = df_2023.groupby("Region").agg(
    Avg_Life_Exp   = ("Life_Expectancy", "mean"),
    Avg_GDP        = ("GDP_Per_Capita",  "mean"),
    Avg_Health_Pct = ("Health_Spend_%", "mean"),
    Countries      = ("Life_Expectancy", "count"),
).round(2).sort_values("Avg_Life_Exp", ascending=False)

print(f"  {'Region':<12} {'Countries':>10} {'Avg Life Exp':>13} {'Avg GDP/cap':>12} {'Health%':>8}")
print("  " + "-" * 56)
for region, row in regional.iterrows():
    print(f"  {region:<12} {int(row['Countries']):>10}    {row['Avg_Life_Exp']:>9.1f}  "
          f"${row['Avg_GDP']:>9,.0f}  {row['Avg_Health_Pct']:>6.1f}%")

# ── STEP 5 — TREND ANALYSIS ───────────────────────────────────
print("\n📈 STEP 5 — LIFE EXPECTANCY TRENDS (2015 → 2023)")
print("-" * 58)

pivot_life = df.pivot_table(values="Life_Expectancy",
                            index="Country", columns="Year", aggfunc="mean")
gains = (pivot_life[2023] - pivot_life[2015]).sort_values(ascending=False)

print(f"  {'Country':<18} {'2015':>7} {'2023':>7} {'Gain':>7}")
print("  " + "-" * 42)
for country, gain in gains.items():
    bar       = "+" * int(gain) if gain > 0 else ""
    val_2015  = pivot_life.loc[country, 2015]
    val_2023  = pivot_life.loc[country, 2023]
    print(f"  {country:<18} {val_2015:>7.1f} {val_2023:>7.1f} {gain:>+7.1f}  {bar}")

fastest = gains.index[0]


print(f"\n  Most improved : {fastest} (+{gains[0]:.1f} years)")

# ── STEP 6 — VISUALISE ────────────────────────────────────────
print("\n🎨 STEP 6 — Building health dashboard...")

fig, axes = plt.subplots(2, 2, figsize=(16, 11))
fig.suptitle("Global Health Snapshot Dashboard (2015–2023)",
            fontsize=15, fontweight="bold")
fig.patch.set_facecolor("#f0f4f8")

region_colors = {
    "Asia"    : "#e74c3c", "Americas": "#3498db",
    "Europe"  : "#27ae60", "Africa"  : "#f39c12",
    "Oceania" : "#9b59b6",
}

# Panel 1: Scatter — GDP vs Life Expectancy (2023)
ax1 = axes[0, 0]
for region in df_2023["Region"].unique():
    subset = df_2023[df_2023["Region"] == region]
    ax1.scatter(subset["GDP_Per_Capita"], subset["Life_Expectancy"],
                label=region, color=region_colors[region],
                s=80, alpha=0.85, edgecolors="white")
for country, row in df_2023.iterrows():
    ax1.annotate(country, (row["GDP_Per_Capita"], row["Life_Expectancy"]),
                fontsize=6, alpha=0.7, xytext=(3, 3), textcoords="offset points")
ax1.set_title("GDP per Capita vs Life Expectancy (2023)", fontweight="bold")
ax1.set_xlabel("GDP per Capita (USD)")
ax1.set_ylabel("Life Expectancy (years)")
ax1.xaxis.set_major_formatter(mticker.FuncFormatter(lambda v, _: f"${int(v/1000)}K"))
ax1.legend(fontsize=8)
ax1.grid(alpha=0.3)
ax1.set_facecolor("white")

# Panel 2: Line — Life Expectancy Trends for 5 diverse countries
ax2 = axes[0, 1]
showcase = ["Japan", "USA", "India", "Nigeria", "Brazil"]
line_colors = ["#e74c3c", "#3498db", "#f39c12", "#27ae60", "#9b59b6"]
for country, color in zip(showcase, line_colors):
    cdf = df[df["Country"] == country]
    ax2.plot(cdf["Year"], cdf["Life_Expectancy"],
            linewidth=2.5, color=color, label=country, marker="o", markersize=4)
ax2.set_title("Life Expectancy Trends — 5 Countries", fontweight="bold")
ax2.set_xlabel("Year")
ax2.set_ylabel("Life Expectancy (years)")
ax2.legend(fontsize=9)
ax2.grid(alpha=0.3)
ax2.set_facecolor("white")

# Panel 3: Bar — Regional Avg Life Expectancy (2023)
ax3 = axes[1, 0]
reg_sorted = regional.sort_values("Avg_Life_Exp")
colors_bar = [region_colors[r] for r in reg_sorted.index]
bars = ax3.barh(reg_sorted.index, reg_sorted["Avg_Life_Exp"],
                color=colors_bar, edgecolor="white")
ax3.set_title("Avg Life Expectancy by Region (2023)", fontweight="bold")
ax3.set_xlabel("Life Expectancy (years)")
ax3.set_xlim(50, 90)
for bar, val in zip(bars, reg_sorted["Avg_Life_Exp"]):
    ax3.text(val + 0.3, bar.get_y() + bar.get_height() / 2,
            f"{val:.1f}", va="center", fontsize=9, fontweight="bold")
ax3.set_facecolor("white")

# Panel 4: Scatter — Health Spend % vs Life Expectancy (2023)
ax4 = axes[1, 1]
for region in df_2023["Region"].unique():
    subset = df_2023[df_2023["Region"] == region]
    ax4.scatter(subset["Health_Spend_%"], subset["Life_Expectancy"],
                label=region, color=region_colors[region],
                s=100, alpha=0.85, edgecolors="white")
# Trend line
z = np.polyfit(df_2023["Health_Spend_%"], df_2023["Life_Expectancy"], 1)
p = np.poly1d(z)
x_line = np.linspace(df_2023["Health_Spend_%"].min(), df_2023["Health_Spend_%"].max(), 100)
ax4.plot(x_line, p(x_line), "k--", linewidth=1.5, alpha=0.6, label="Trend")
ax4.set_title("Health Spending % vs Life Expectancy (2023)", fontweight="bold")
ax4.set_xlabel("Health Spending (% of GDP)")
ax4.set_ylabel("Life Expectancy (years)")
ax4.legend(fontsize=8)
ax4.grid(alpha=0.3)
ax4.set_facecolor("white")

plt.tight_layout()
plt.savefig("health_dashboard.png", dpi=150, bbox_inches="tight")
print("  ✅ Saved: health_dashboard.png")
plt.show()

# ── STEP 7 — EXPORT ───────────────────────────────────────────
print("\n💾 STEP 7 — EXPORTING DATA")

df.to_csv("health_full.csv", index=False)
print(f"  ✅ Saved: health_full.csv ({len(df)} rows)")

df_2023.reset_index().to_csv("health_2023_snapshot.csv", index=False)
print(f"  ✅ Saved: health_2023_snapshot.csv ({len(df_2023)} countries)")

gains.reset_index().rename(columns={0: "Life_Exp_Gain"}).to_csv(
    "life_exp_gains.csv", index=False
)
print(f"  ✅ Saved: life_exp_gains.csv")

# ── SUMMARY ──────────────────────────────────────────────────
print("\n" + "=" * 62)
print("📌 KEY GLOBAL HEALTH FINDINGS")
print("=" * 62)
highest_le = df_2023_sorted.index[0]
lowest_le  = df_2023_sorted.index[-1]
highest_gdp = df_2023.sort_values("GDP_Per_Capita", ascending=False).index[0]

print(f"  • Highest life expectancy (2023): {highest_le} "
      f"({df_2023.loc[highest_le, 'Life_Expectancy']:.1f} yrs)")
print(f"  • Lowest life expectancy (2023) : {lowest_le} "
      f"({df_2023.loc[lowest_le, 'Life_Expectancy']:.1f} yrs)")
print(f"  • Gap between highest and lowest: "
      f"{df_2023.loc[highest_le,'Life_Expectancy']-df_2023.loc[lowest_le,'Life_Expectancy']:.1f} years")
print(f"  • Highest GDP per capita        : {highest_gdp} "
      f"(${df_2023.loc[highest_gdp,'GDP_Per_Capita']:,.0f})")
print(f"  • Most improved (2015→2023)     : {fastest} (+{gains[0]:.1f} years)")
print(f"  • Countries analysed            : {len(countries)}")
print(f"  • Total data points             : {len(df):,}")
print("=" * 62)

print("\n💡 CHALLENGE:")
print("  1. Which country spends the most on health but has lower life expectancy than expected?")
print("  2. Add a 5th panel: bar chart of top 10 countries by doctors per 1,000 people.")
print("  3. Compute the correlation between GDP and life expectancy using NumPy.")
print("  4. Find which African country improved the most from 2015 to 2023.")
print()

