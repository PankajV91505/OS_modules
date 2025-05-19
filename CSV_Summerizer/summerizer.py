import csv
from collections import defaultdict

filename = "sales_data.csv"

with open(filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    numeric_data = defaultdict(list)
    
    for row in reader:
        for key, value in row.items():
            try:
                num = float(value)
                numeric_data[key].append(num)
            except ValueError:
                continue

summary = []

for column, values in numeric_data.items():
    if not values:
        continue
    total = sum(values)
    avg = total / len(values)
    min_val = min(values)
    max_val = max(values)
    summary.append([column, total, avg, min_val, max_val])

print(f"{'Column':<15} {'Total':<10} {'Average':<10} {'Min':<10} {'Max':<10}")
print("-" * 55)
for col in summary:
    print(f"{col[0]:<15} {col[1]:<10.2f} {col[2]:<10.2f} {col[3]:<10.2f} {col[4]:<10.2f}")

# Optional CSV output
with open("summary.csv", "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["Column", "Total", "Average", "Min", "Max"])
    writer.writerows(summary)
