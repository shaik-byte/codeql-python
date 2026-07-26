
from flask import Flask, request
import sqlite3
import subprocess

app = Flask(__name__)


@app.route("/user")
def get_user():
    user_id = request.args.get("id", "")

    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    # Intentionally vulnerable: SQL injection
    query = "SELECT * FROM users WHERE id = " + user_id
    result = cursor.execute(query).fetchall()

    connection.close()
    return {"users": result}


@app.route("/ping")
def ping_host():
    host = request.args.get("host", "")

    # Intentionally vulnerable: command injection
    output = subprocess.check_output(
        "ping -c 1 " + host,
        shell=True,
        text=True,
    )

    return {"output": output}


if __name__ == "__main__":
    # Intentionally vulnerable: Flask debug mode
    app.run(host="0.0.0.0", port=5000, debug=True)

