from flask import Flask, render_template, request, send_file
import os

from dashboard import get_statistics
from view_logs import get_all_logs
from export_csv import export_logs

app = Flask(__name__)

# Folder for uploaded files
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():

    stats = get_statistics()

    search = request.args.get("search", "")

    page = int(request.args.get("page", 1))

    logs = get_all_logs(search, page)
    
    return render_template(
        "dashboard.html",
        stats=stats,
        logs=logs,
        search=search,
        page=page
    )


@app.route("/export")
def export():

    export_logs()

    return send_file(
        "logs_export.csv",
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)