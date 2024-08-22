from jira import JIRA
import logging

class JiraExtractor:
    def __init__(self, jira_url, jira_user, jira_api_token):
        options = {'server': jira_url}
        self.jira = JIRA(options, basic_auth=(jira_user, jira_api_token))
        logging.info("Connected to Jira successfully.")

    def get_stories(self, project_key):
        try:
            jql_query = f'project = {project_key} AND type = Story'
            issues = self.jira.search_issues(jql_query, maxResults=1000)
            stories = []
            for issue in issues:
                story = {
                    'ID': issue.key,
                    'Summary': issue.fields.summary,
                    'Status': issue.fields.status.name,
                    'Assignee': issue.fields.assignee.displayName if issue.fields.assignee else 'Unassigned',
                    'Reporter': issue.fields.reporter.displayName,
                    'Created': issue.fields.created,
                    'Updated': issue.fields.updated
                }
                stories.append(story)
            logging.info(f"Extracted {len(stories)} stories from Jira.")
            return stories
        except Exception as e:
            logging.error(f"Failed to retrieve stories from Jira: {str(e)}")
            return None