# Day 2: Data Filtering and Logic
# Scenario: Filtering a list of temperatures to find "Heatwave" days (above 35°C)

temperatures = [28, 32, 35, 40, 42, 29, 31, 45, 33]
heatwave_days = []

# Using a loop and logic to filter data
for temp in temperatures:
    if temp > 35:
        heatwave_days.append(temp)

print(f"Total days recorded: {len(temperatures)}")
print(f"Number of heatwave days: {len(heatwave_days)}")
print(f"Highest temperature recorded: {max(temperatures)}°C")

# Professional touch: List Comprehension (A must-know for Data Science)
# This does the same thing as the loop above but in one line
cool_days = [t for t in temperatures if t <= 30]
print(f"Days with pleasant weather (<=30°C): {cool_days}")
