visualize_code = '''import os
import pandas as pd
import matplotlib.pyplot as plt
from clean_and_eda import clean_data

# Ensure output directory exists
os.makedirs('visualizations', exist_ok=True)

# Clean dataset end-to-end
df = clean_data()

# -----------------------------------------------------------------------------
# Chart 1: Return Rate by Payment Method
# -----------------------------------------------------------------------------
ret_rates = df.groupby('payment_method')['returned'].mean() * 100
ret_rates = ret_rates.sort_values(ascending=False)

plt.figure(figsize=(8, 5))
bars = plt.bar(ret_rates.index, ret_rates.values, color=['#d9534f', '#5bc0de', '#4cae4c'])

plt.title('COD Returns at 44.4% — 3x Card', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Payment Method', fontsize=11, labelpad=8)
plt.ylabel('Return Rate (%)', fontsize=11, labelpad=8)
plt.ylim(0, 50)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Label exact percentages on each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2.0, height + 1.0, f'{height:.1f}%',
             ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('visualizations/return_rate_by_payment.png', dpi=300)
plt.close()

# -----------------------------------------------------------------------------
# Chart 2: Outlier-Corrected Monthly Revenue Trend
# -----------------------------------------------------------------------------
monthly_rev = df[~df['is_outlier']].groupby('year_month')['order_value'].sum()
monthly_rev.index = monthly_rev.index.astype(str)

plt.figure(figsize=(9, 5))
plt.plot(monthly_rev.index, monthly_rev.values, marker='o', color='#2b5c8f', linewidth=2.5, markersize=6)

plt.title('Outlier-Corrected Monthly Revenue Trend — Peak Month: March 2026 (₹20,318.90)', fontsize=13, fontweight='bold', pad=15)
plt.xlabel('Month', fontsize=11, labelpad=8)
plt.ylabel('Total Order Value (₹)', fontsize=11, labelpad=8)
plt.grid(True, linestyle='--', alpha=0.5)

# Highlight peak value on chart
peak_month = monthly_rev.idxmax()
peak_val = monthly_rev.max()
plt.annotate(f'Peak: ₹{peak_val:,.2f}',
             xy=(peak_month, peak_val),
             xytext=(peak_month, peak_val + 1200),
             ha='center',
             arrowprops=dict(facecolor='#d9534f', shrink=0.08, width=1.5, headwidth=6),
             fontsize=9, fontweight='bold', color='#d9534f')

plt.ylim(8000, 23000)
plt.tight_layout()
plt.savefig('visualizations/monthly_revenue_trend.png', dpi=300)
plt.close()

print("Visualizations generated successfully in visualizations/")
'''

with open('analysis/visualize.py', 'w') as f:
    f.write(visualize_code)

# Test execution end-to-end
import subprocess
res1 = subprocess.run(['python3', 'analysis/clean_and_eda.py'], capture_output=True, text=True)
print("clean_and_eda.py stdout:", res1.stdout)
print("clean_and_eda.py stderr:", res1.stderr)

import sys
sys.path.append('analysis')
res2 = subprocess.run(['python3', 'analysis/visualize.py'], capture_output=True, text=True)
print("visualize.py stdout:", res2.stdout)
print("visualize.py stderr:", res2.stderr)
