# CIS-117 Lab3
# Description: Imports read_countries() from reading_part.py and writes one CSV
#              file per region (e.g. Europe.csv). Each output file keeps ONLY
#              the country name and region.
# Wally Moreno Negrete
# Group 15
# Collaborator: Aung Khant Kyaw
# Collaboration: Aung Khant Kyaw wrote the reading part (reading country_full.csv
# and grouping the countries by region). I wrote the writing part (creating one
# CSV file per region and handling file-writing errors). I import his
# read_countries() function here.

import csv

from reading_part import read_countries


def write_region_files(countries_by_region):
    """Write one CSV file per region containing only name and region."""
    files_written = 0

    for region, country_list in countries_by_region.items():
        output_filename = region + ".csv"

        try:
            with open(output_filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["name", "region"])

                for country in country_list:
                    # Use the group key so "Unassigned" countries are labeled too
                    writer.writerow([country["name"], region])

            files_written += 1
            print("Wrote", len(country_list), "countries to", output_filename)

        except PermissionError:
            print("Error: Permission denied when writing", output_filename)

        except FileNotFoundError:
            print("Error: Could not create", output_filename, "- path not found.")

        except OSError as error:
            print("Error writing", output_filename, ":", error)

    return files_written


def main():
    countries_by_region = read_countries("country_full.csv")

    # read_countries() returns None if the input file could not be read
    if countries_by_region is None:
        print("No data to write. Exiting.")
        return

    total = write_region_files(countries_by_region)
    print("Done.", total, "of", len(countries_by_region), "region files written.")


if __name__ == "__main__":
    main()
