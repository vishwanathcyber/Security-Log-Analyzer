"""
JSON Report Exporter
"""

import json

def export_json(results):

    with open("reports/report.json", "w") as file:

        json.dump(results, file, indent=4)

    print("JSON report generated.")
