import requests
import pandas as pd

# Read the CSV file
input_file_name = "Shellfish_classification_England_and_Wales_08032023_Classification_list_2022-2023_pacific_oysters.csv"
df = pd.read_csv(f"data/computed/{input_file_name}")

ids = df["RMP ID"]

base_url = "https://www.cefas.co.uk/umbraco/CefasPlugins/ShsSurface/CSV?connection=SHS&pointId={}&species=OYG"

for id_ in ids:
    # Inject the ID into the URL
    url = base_url.format(id_)

    # Download the file
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Save the file with the ID as its name
        with open(f"data/computed/{id_}.csv", "wb") as f:
            f.write(response.content)
        print(f"Downloaded file for ID {id_}.")
    else:
        print(f"Failed to download file for ID {id_}.")
