
print("Rainfall Calculator\n")

years = int(input("Enter the number of years: "))
total_months = years * 12
total_rainfall = 0.0

for y in range(years):
    print(f"\nYear {y + 1}")
    for month in range(12):
        rainfall = float(input(f"  Month {month + 1} rainfall (in inches): "))
        total_rainfall += rainfall

average = total_rainfall / total_months

print("\nRainfall Summary")
print(f"  Total months:      {total_months}")
print(f"  Total rainfall:    {total_rainfall:.2f} inches")
print(f"  Average per month: {average:.2f} inches")
