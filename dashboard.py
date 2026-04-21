import pandas as pd
import matplotlib.pyplot as plt

# Load workout data
df = pd.read_csv("data/workouts.csv")

if df.empty:
    print("No workout data yet!")
    exit()

# Count exercises
summary = df["Exercise"].value_counts()

# Plot graph
plt.figure(figsize=(6,4))
summary.plot(kind="bar")

plt.title("Workout Progress Dashboard")
plt.xlabel("Exercise Type")
plt.ylabel("Total Reps Logged")

plt.show()