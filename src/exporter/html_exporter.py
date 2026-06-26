"""
HTML Report Generator
"""

def export_html():

    html = """
    <html>

    <head>

    <title>Security Report</title>

    </head>

    <body>

    <h1>Security Log Analyzer Report</h1>

    <p>Report generation completed successfully.</p>

    </body>

    </html>

    """

    with open("reports/report.html","w") as file:

        file.write(html)

    print("HTML report generated.")
