import numpy as np

print("=" * 60)
print("       🥇 OLYMPIC MEDAL ANALYSER & PODIUM PREDICTOR")
print("=" * 60)

# ── DATASET ──────────────────────────────────────────────────
# Gold medals won by 5 countries across 4 Olympics
# Shape: (5 countries) × (4 Olympics)
countries = ["USA", "China", "Russia", "UK", "Australia"]
olympics  = [2008, 2012, 2016, 2020]

medals = np.array([
    # 2008  2012  2016  2020
    [36,    46,    46,    39],   # USA
    [51,    38,    26,    38],   # China
    [23,    24,    19,    20],   # Russia
    [19,    29,    27,    22],   # UK
    [14,    8,     8,     17],   # Australia
])

# ── STEP 1 — BASIC STATS ─────────────────────────────────────
print("\n📋 RAW MEDAL TABLE")
print(f"{'Country':<12}" + "".join(f"{y:>8}" for y in olympics) + f"{'Total':>8} {'Avg':>7}")
print("-" * 55)
for i, country in enumerate(countries):
    row   = medals[i]
    total = np.sum(row)
    avg   = np.mean(row)
    print(f"{country:<12}" + "".join(f"{m:>8}" for m in row) + f"{total:>8} {avg:>7.1f}")

# ── STEP 2 — RANKINGS PER OLYMPICS ───────────────────────────
print("\n🏆 RANKINGS PER OLYMPICS")
print(f"{'Country':<12}" + "".join(f"{y:>8}" for y in olympics))
print("-" * 44)
for i, country in enumerate(countries):
    ranks = []
    for j in range(len(olympics)):
        col  = medals[:, j]             # All countries for this Olympics
        rank = np.sum(col > medals[i, j]) + 1  # Count how many scored higher
        ranks.append(rank)
    print(f"{country:<12}" + "".join(f"  #{r}   " for r in ranks))

# ── STEP 3 — TOTAL MEDALS (axis=1 sum) ───────────────────────
totals = np.sum(medals, axis=1)
print("\n📊 TOTAL MEDALS (2008–2020)")
sorted_idx = np.argsort(totals)[::-1]
for rank, i in enumerate(sorted_idx, 1):
    bar = "█" * (totals[i] // 5)
    print(f"  {rank}. {countries[i]:<12}: {bar} {totals[i]}")

# ── STEP 4 — GROWTH RATE (first to last Olympics) ────────────
print("\n📈 GROWTH RATE (2008 → 2020)")
print("-" * 40)
growth_rates = ((medals[:, -1] - medals[:, 0]) / medals[:, 0]) * 100
for i, country in enumerate(countries):
    rate      = growth_rates[i]
    direction = "📈" if rate > 0 else "📉"
    print(f"  {direction} {country:<12}: {rate:+.1f}%")

fastest_improver = countries[np.argmax(growth_rates)]
biggest_decline  = countries[np.argmin(growth_rates)]
print(f"\n  Most improved : {fastest_improver}")
print(f"  Biggest drop  : {biggest_decline}")

# ── STEP 5 — BEST SINGLE OLYMPICS PER COUNTRY ────────────────
print("\n🌟 EACH COUNTRY'S BEST OLYMPICS")
best_game_idx = np.argmax(medals, axis=1)
for i, country in enumerate(countries):
    best_year  = olympics[best_game_idx[i]]
    best_count = medals[i, best_game_idx[i]]
    print(f"  {country:<12}: {best_year} ({best_count} golds)")

# ── STEP 6 — PERCENTILE ANALYSIS ─────────────────────────────
print("\n📐 PERCENTILE ANALYSIS (all medal scores combined)")
all_scores = medals.flatten()
p25  = np.percentile(all_scores, 25)
p50  = np.percentile(all_scores, 50)
p75  = np.percentile(all_scores, 75)
p90  = np.percentile(all_scores, 90)
print(f"  25th percentile : {p25:.1f} medals")
print(f"  Median (50th)   : {p50:.1f} medals")
print(f"  75th percentile : {p75:.1f} medals")
print(f"  90th percentile : {p90:.1f} medals")
print(f"  (Elite = above {p75:.0f} medals in a single Olympics)")

# ── STEP 7 — PREDICT NEXT OLYMPICS (2024) ────────────────────
print("\n🔮 PODIUM PREDICTION — PARIS 2024")
print("-" * 45)
# Weighted average: recent Olympics count more
weights     = np.array([0.1, 0.2, 0.3, 0.4])
predictions = np.average(medals, axis=1, weights=weights)
pred_sorted = np.argsort(predictions)[::-1]
medals_2024 = ["🥇", "🥈", "🥉"]

for rank, i in enumerate(pred_sorted, 1):
    medal_icon = medals_2024[rank-1] if rank <= 3 else f"#{rank}"
    print(f"  {medal_icon} {countries[i]:<12}: predicted {predictions[i]:.1f} golds")

# ── SUMMARY ──────────────────────────────────────────────────
print("\n" + "=" * 60)
print(f"  Dominant country  : {countries[np.argmax(totals)]}")
print(f"  Most consistent   : {countries[np.argmin(np.std(medals, axis=1))]}")
print(f"  Most volatile     : {countries[np.argmax(np.std(medals, axis=1))]}")
print(f"  Fastest improving : {fastest_improver}")
print("=" * 60)
print()