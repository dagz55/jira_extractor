# Pushing the Jira Extractor Project to GitHub

This guide provides step-by-step instructions on how to push the Jira Extractor project to your GitHub repository: https://github.com/dagz55/jira_extractor.git

## Prerequisites

1. Git installed on your local machine
2. GitHub account
3. Repository created on GitHub (https://github.com/dagz55/jira_extractor.git)

## Steps

1. Open a terminal or command prompt.

2. Navigate to your project directory:
   ```
   cd /Users/robertsuarez/project_jira_extractor
   ```

3. Initialize a Git repository (if not already done):
   ```
   git init
   ```

4. Add all files to the Git repository:
   ```
   git add .
   ```

5. Commit the changes:
   ```
   git commit -m "Initial commit of Jira Extractor project"
   ```

6. Add the remote GitHub repository:
   ```
   git remote add origin https://github.com/dagz55/jira_extractor.git
   ```

7. Check which branch you're on:
   ```
   git branch
   ```

   If you're on the 'dev' branch, you can either push to 'dev' or create and switch to 'main':
   ```
   git checkout -b main
   ```

8. Push the code to GitHub:
   ```
   git push -u origin main
   ```

   If you want to push the 'dev' branch instead:
   ```
   git push -u origin dev
   ```

9. Enter your GitHub credentials if prompted.

## Troubleshooting

If you encounter an error like "src refspec master does not match any", it usually means you're trying to push a branch that doesn't exist locally. Make sure you're pushing the correct branch name (e.g., 'main' or 'dev').

If you see "nothing added to commit but untracked files present", make sure to add your files before committing:
```
git add .
git commit -m "Your commit message"
```

## Updating the Repository

After making changes to your local project:

1. Stage the changes:
   ```
   git add .
   ```

2. Commit the changes:
   ```
   git commit -m "Description of changes"
   ```

3. Push the changes to GitHub:
   ```
   git push
   ```

## Best Practices

- Always pull the latest changes before starting work:
  ```
  git pull origin main
  ```
- Create meaningful commit messages that describe your changes.
- Consider using branches for major features or changes.
- Regularly push your changes to keep the remote repository up-to-date.

Remember to never commit sensitive information like API keys or passwords. Ensure your `.env` file is included in your `.gitignore` file to prevent it from being pushed to the repository.