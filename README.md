# Log Monitoring System

A Python Flask-based web application for parsing log files, storing logs in SQLite, visualizing log statistics, searching logs, pagination, and exporting logs to CSV.

## Features

- Upload log files
- Parse logs using Regular Expressions
- Store logs in SQLite database
- Search logs by level or message
- Pagination support
- Pie chart visualization
- Export logs to CSV
- Responsive dashboard

## Tech Stack

- Python
- Flask
- SQLite
- HTML
- CSS
- Chart.js

## Project Structure

```
app.py
dashboard.py
database.py
export_csv.py
load_logs.py
log_parser.py
view_logs.py
templates/
static/
sample.log
requirements.txt
```

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

Open:

```
http://127.0.0.1:5000
```

## Author

Shiva Jayanth