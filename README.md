# jira_extractor
Automate Jira Data Extraction and Excel Workbook Updates with Python

# Jira Extractor

This project automates the extraction of Jira data (epics, stories, and bugs) and exports it to an Excel file.

## Documentation

For detailed information on how to use this project, please refer to the following documentation:

- [Usage Guide](docs/usage.md): Instructions on how to set up and run the Jira Extractor script.
- [Requirements](docs/requirements.txt): List of required Python packages and their versions.
- [GitHub Push Instructions](docs/github_push_instructions.md): Steps to push this project to the GitHub repository.

## Quick Start

1. Clone this repository
2. Install the required packages: `pip install -r docs/requirements.txt`
3. Set up your `.env` file with the necessary credentials and configurations
4. Run the script: `python src/main.py`

For more detailed instructions, please refer to the [Usage Guide](docs/usage.md).

## Pushing to GitHub

To push this project to your GitHub repository:

1. Navigate to the project directory: `cd /Users/robertsuarez/project_jira_extractor`
2. Initialize the repository: `git init`
3. Add all files: `git add .`
4. Commit changes: `git commit -m "Initial commit of Jira Extractor project"`
5. Add remote repository: `git remote add origin https://github.com/dagz55/jira_extractor.git`
6. Check your current branch: `git branch`
7. If needed, create and switch to 'main': `git checkout -b main`
8. Push to GitHub: `git push -u origin main` (or `git push -u origin dev` if you're on the dev branch)

For troubleshooting and more detailed instructions, refer to the [GitHub Push Instructions](docs/github_push_instructions.md).

## Contributing

If you'd like to contribute to this project, please follow the [GitHub Push Instructions](docs/github_push_instructions.md) to set up your local repository and push changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.