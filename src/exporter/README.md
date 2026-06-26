Exporters

Purpose

This module is responsible for generating reports from the analyzed log data.

Instead of only printing results to the terminal, the project will support exporting findings in different formats.

Planned Report Formats

- JSON
- HTML
- Markdown
- CSV
- Plain Text

Report Contents

Each report should include:

- Scan Summary
- Log Statistics
- Failed Login Attempts
- Suspicious IP Addresses
- Authentication Events
- Security Findings
- Severity Levels
- Recommendations
- Scan Metadata

Design Goal

Each exporter should have only one responsibility: convert analyzed security findings into a specific output format. This modular approach makes it easier to add new report formats in the future.
