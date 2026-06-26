"""
CSV Report Exporter
"""

import csv

def export_csv(results):

    with open("reports/report.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Metric", "Value"])

        for key, value in results.items():

            writer.writerow([key, value])

    print("CSV report generated.")
