# Jira Data Extractor Usage Guide

This document provides instructions on how to use the Jira Data Extractor script to fetch and export data from Jira to an Excel file.

## Prerequisites

1. Python 3.7 or higher
2. Required Python packages (install using `pip install -r requirements.txt`)
3. Jira account with API access
4. Excel file with the following worksheets:
   - Epics Raw
   - Stories Raw
   - Stories Raw (Active Sprint)
   - Bugs Raw
   - Summary

## Setup

1. Clone the repository or download the script files.
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the same directory as the `main.py` file with the following contents:
   ```
   JIRA_URL=https://your-company.atlassian.net
   JIRA_USER=your-email@example.com
   JIRA_API_TOKEN=your-api-token
   EXCEL_FILE_PATH=/path/to/your/excel/file.xlsx
   EPIC_FILTER_ID=your-epic-filter-id
   ALL_STORIES_FILTER_ID=your-all-stories-filter-id
   ACTIVE_STORIES_FILTER_ID=your-active-stories-filter-id
   BUGS_FILTER_ID=your-bugs-filter-id
   ```
   Replace the placeholders with your actual Jira and file information.

## Running the Script

To run the script, navigate to the directory containing `main.py` and execute:

```
python main.py
```

The script will:
1. Connect to Jira using the provided credentials
2. Fetch epics, stories, and bugs based on the specified filter IDs
3. Update the corresponding worksheets in the Excel file
4. Update the timestamp in the Summary worksheet

## Troubleshooting

- If you encounter any errors related to missing environment variables, make sure all required variables are set in the `.env` file.
- If you get authentication errors, verify that your Jira URL, username, and API token are correct.
- For issues with the Excel file, ensure that the file exists at the specified path and contains the required worksheets.

## Customization

To modify the data being extracted or the format of the Excel file:

1. Edit the `insert_epics`, `insert_stories`, and `insert_bugs` functions in `main.py` to change the data being extracted or the column layout.
2. Modify the `write_to_excel` function to add or remove data types being processed.
3. Update the filter IDs in the `.env` file to change the Jira filters being used for data extraction.

For any additional help or feature requests, please contact the development team.