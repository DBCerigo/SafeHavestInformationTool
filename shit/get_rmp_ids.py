import csv
import pandas as pd

# Read the CSV file
input_file_name = "Shellfish_classification_England_and_Wales_08032023_Classification_list_2022-2023.csv"

data = pd.read_csv(f"data/input/{input_file_name}")

# Filter on the 'Species(a)' column for the value 'C. gigas'
filtered_data = data[data["Species(a)"] == "C. gigas"]
filtered_data = filtered_data[filtered_data["Designated Use"] == "Production"]

# Save the filtered CSV to disk
filtered_data.to_csv(
    f"data/computed/Shellfish_classification_England_and_Wales_08032023_Classification_list_2022-2023_pacific_oysters.csv",
    index=False,
)

# Get unique values from the 'RMP ID' column
unique_rmp_ids = filtered_data["RMP ID"].unique()

# Check if the 'RMP ID' column contains unique values
if len(unique_rmp_ids) == len(filtered_data):
    print("The 'RMP ID' column contains unique values.")
else:
    print("The 'RMP ID' column contains duplicate values.")

# Print the unique RMP ID values
print(unique_rmp_ids)
