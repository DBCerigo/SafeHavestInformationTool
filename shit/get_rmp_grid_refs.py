import requests
from bs4 import BeautifulSoup
import pandas as pd
import concurrent.futures

# Read the CSV file
input_file_name = "Shellfish_classification_England_and_Wales_08032023_Classification_list_2022-2023_pacific_oysters.csv"
df = pd.read_csv(f"data/computed/{input_file_name}")

ids = df["RMP ID"]

data = []


def get_national_grid_ref(ID):
    print(ID)
    url = f"https://www.cefas.co.uk/data-and-publications/shellfish-classification-and-microbiological-monitoring/england-and-wales/shellfish-monitoring-results/details/?species=OYG&connection=SHS&PointID={ID}"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    national_grid_ref = soup.find(
        "div", string="National Grid Reference:"
    ).next_sibling.next_sibling.text
    return {"PointID": ID, "National Grid Reference": national_grid_ref}


with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(get_national_grid_ref, ids)
    for result in results:
        data.append(result)

df = pd.DataFrame(data)
print(df)
df.to_csv("data/computed/point_ids_and_grid_refs.csv", index=False)
