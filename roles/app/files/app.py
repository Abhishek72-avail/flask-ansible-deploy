from flask import Flask, render_template, jsonify, request
import os
import psycopg2
from datetime import datetime

app = Flask(__name__)

def db_check():
    try:
        conn = psycopg2.connect(
            dbname=os.environ.get("DB_NAME"),
            user=os.environ.get("DB_USER"),
            password=os.environ.get("DB_PASSWORD"),
            host=os.environ.get("DB_HOST", "127.0.0.1"),
            port=os.environ.get("DB_PORT", "5432"),
            connect_timeout=3,
        )
        cur = conn.cursor()
        cur.execute("SELECT version();")
        version = cur.fetchone()[0]
        cur.close()
        conn.close()
        return {"status": "success", "message": f"Connected to PostgreSQL: {version}"}
    except Exception as e:
        return {"status": "error", "message": f"DB connection error: {e}"}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/health")
def health():
    # Check if request wants JSON (API call) or HTML (browser)
    if request.headers.get('Accept') == 'application/json' or request.args.get('format') == 'json':
        return jsonify({"status": "OK", "timestamp": datetime.now().isoformat()})
    else:
        # Return beautiful HTML page
        health_data = {
            "status": "OK",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "uptime": "Running smoothly",
            "services": {
                "flask": "Active",
                "gunicorn": "Running",
                "nginx": "Proxying"
            }
        }
        return render_template("health.html", health=health_data)

@app.route("/db")
def db():
    db_result = db_check()
    
    # Check if request wants JSON (API call) or HTML (browser)
    if request.headers.get('Accept') == 'application/json' or request.args.get('format') == 'json':
        return jsonify(db_result)
    else:
        # Return beautiful HTML page
        return render_template("db.html", db_result=db_result)

@app.route("/api/status")
def api_status():
    db_result = db_check()
    return jsonify({
        "flask": {"status": "running", "version": "2.3.3"},
        "database": db_result,
        "nginx": {"status": "proxying"},
        "timestamp": datetime.now().isoformat()
    })

if __name__ == "__main__":
    app.run()