from flask import Flask, render_template, request, redirect, send_file
from database import create_database
from load_logs import load_logs_from_file
from dashboard import get_statistics
from view_logs import get_all_logs
from export_csv import export_logs

app = Flask(__name__)

# Create database and table if they don't exist
create_database()
# Load sample logs into database
load_logs_from_file("sample.log")
# Folder for uploaded files
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return redirect("/dashboard")


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


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]

    if file:
        filepath = f"{UPLOAD_FOLDER}/{file.filename}"
        file.save(filepath)

        load_logs_from_file(filepath)

    return redirect("/dashboard")


@app.route("/export")
def export():
    export_logs()

    return send_file(
        "logs_export.csv",
        as_attachment=True
    )


if __name__ == "__main__":
    import os

    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )