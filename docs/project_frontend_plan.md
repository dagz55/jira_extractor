To add a front end to the project, you can create a simple web interface using Flask, a lightweight web framework in Python. This front-end will allow users to input the Jira API token, Jira URL, and other details directly through a web form. The form data will then trigger the extraction of Jira stories and their export to an Excel file, which can be downloaded through the web interface.

### Directory Structure

With the front end included, the project structure will look like this:

```
/src
    ├── static/
    ├── templates/
    │   ├── index.html
    ├── app.py
    ├── jira_extractor.py
    ├── excel_exporter.py
/config
    └── .env
/output
    └── (Generated Excel files will be stored here)
```

### `app.py` (Main Flask Application)

```python
from flask import Flask, render_template, request, redirect, url_for, send_file
import os
from dotenv import load_dotenv
from src.jira_extractor import JiraExtractor
from src.excel_exporter import ExcelExporter

app = Flask(__name__)

# Load environment variables
load_dotenv()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        jira_url = request.form['jira_url']
        jira_user = request.form['jira_user']
        jira_api_token = request.form['jira_api_token']
        project_key = request.form['project_key']

        # Create JiraExtractor instance
        jira_extractor = JiraExtractor(jira_url, jira_user, jira_api_token)

        # Extract Jira stories
        stories = jira_extractor.get_stories(project_key=project_key)

        # Export to Excel
        if stories:
            excel_exporter = ExcelExporter()
            output_path = 'output/jira_stories.xlsx'
            excel_exporter.export_to_excel(stories, output_path)
            return redirect(url_for('download_file', filename='jira_stories.xlsx'))

        else:
            return render_template('index.html', error="Failed to extract stories. Please check your inputs.")

    return render_template('index.html')

@app.route('/download/<filename>')
def download_file(filename):
    file_path = os.path.join('output', filename)
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
```

### `templates/index.html`

This HTML file provides a form for user input and handles the display of any errors or download links.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jira Story Exporter</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <div class="container">
        <h1>Jira Story Exporter</h1>
        <form method="POST" action="/">
            <label for="jira_url">Jira URL:</label>
            <input type="text" id="jira_url" name="jira_url" required>

            <label for="jira_user">Jira User Email:</label>
            <input type="email" id="jira_user" name="jira_user" required>

            <label for="jira_api_token">Jira API Token:</label>
            <input type="password" id="jira_api_token" name="jira_api_token" required>

            <label for="project_key">Project Key:</label>
            <input type="text" id="project_key" name="project_key" required>

            <button type="submit">Export Stories</button>
        </form>

        {% if error %}
        <p style="color:red;">{{ error }}</p>
        {% endif %}
    </div>
</body>
</html>
```

### `static/styles.css`

Add a simple CSS file to style the web page. You can place this file in the `static` directory.

```css
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    padding: 20px;
}

.container {
    max-width: 600px;
    margin: 0 auto;
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
    margin-bottom: 20px;
}

label {
    display: block;
    margin-bottom: 8px;
}

input[type="text"],
input[type="email"],
input[type="password"] {
    width: 100%;
    padding: 8px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}
```

### How to Run the Project

1. **Install Flask and other dependencies:**

   ```
   pip install flask jira pandas openpyxl python-dotenv
   ```

2. **Set up the `.env` file:**

   This is optional but recommended for loading defaults.

3. **Run the Flask application:**

   Navigate to the `src` directory and run:

   ```
   python app.py
   ```

4. **Access the Web Interface:**

   Open your web browser and go to `http://127.0.0.1:5000/`. You will see the form where you can input your Jira URL, User Email, API Token, and Project Key.

5. **Export and Download:**

   After submitting the form, the Jira stories will be extracted and saved as an Excel file. You will then be redirected to a page where you can download the file.

### Conclusion

This setup provides a simple yet functional web interface for your Jira story extraction project. It can be further enhanced by adding more fields, error handling, and advanced UI features.