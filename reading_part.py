# CIS117 Lab 3
# Description: Reads CSV file and group countries by region.
# Name: Aung Khant Kyaw
# Partner: Wally Moreno Negrete
# Group 15
# Collaboration: I worked on reading the CSV file, extracting country names and regions, grouping the countries by region, and handling file errors.

import csv

def read_countries(filename):
    countries_by_region = {}

    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                name = row["name"]
                region = row["region"]

                if region == "":
                    region = "Unassigned"

                if region not in countries_by_region:
                    countries_by_region[region] = []

                countries_by_region[region].append({
                    "name": name,
                    "region": row["region"]
                })

    except FileNotFoundError:
        print("Error: The CSV file was not found.")
        return None

    except PermissionError:
        print("Error: Permission denied.")
        return None

    except OSError as error:
        print("Error reading file:", error)
        return None

    return countries_by_region


if __name__ == "__main__":
    countries = read_countries("country_full.csv")

    if countries is not None:
        for region, country_list in countries.items():
            print(region, ":", len(country_list))

        print(countries["Asia"][:3])