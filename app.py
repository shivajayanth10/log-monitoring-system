from flask import Flask, render_template, request, send_file, redirect, url_for
import os

from dashboard import get_statistics
from view_logs import get_all_logs
from export_csv import export_logs

app = Flask(__name__)

# Folder for uploaded files
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# Home page → directly open dashboard
@app.route("/")
def home():
    return redirect(url_for("dashboard"))


# Dashboard
@app.route("/dashboard")
def dashboard():
    stats = get_statistics()

    search = request.args.get("search", "")
    page = int(request.args.get("page", 1))

    logs = get_all_logs(search, page)

    return render_template(
        "dashboard.html",
        stats=stats,
        logs=logs
    )


# Export CSV
@app.route("/export")
def export():
    export_logs()

    return send_file(
        "logs_export.csv",
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )