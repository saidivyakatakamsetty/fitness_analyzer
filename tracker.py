import csv
import os

# -----------------------------
# Setup log file
# -----------------------------
os.makedirs("data", exist_ok=True)

log_file = "data/workouts.csv"

# Create file with headers if not exists
if not os.path.exists(log_file):
    with open(log_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Exercise", "Reps"])


# -----------------------------
# Save workout data
# -----------------------------
def log_workout(exercise, reps):
    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([exercise, reps])