from flask import Flask, render_template, request, redirect, url_for
import sqlite3, requests

app = Flask(__name__, static_folder='static', template_folder='templates')

# ---------- Database Setup ----------
def init_db():
    with sqlite3.connect("portfolio.db") as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                message TEXT
            )
        """)
init_db()

# ---------- HOME ROUTE ----------
@app.route('/')
def home():
    GITHUB_USER = "manish1103"

    # --- Fetch GitHub Projects ---
    github_repos = []
    try:
        github_url = f"https://api.github.com/users/{GITHUB_USER}/repos"
        response = requests.get(github_url)
        github_repos = response.json()
        print(f"✅ GitHub Projects Loaded: {len(github_repos)}")
    except Exception as e:
        print("❌ GitHub API Error:", e)

    return render_template("index.html", github_repos=github_repos)

# ---------- CONTACT PAGE ----------
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        with sqlite3.connect("portfolio.db") as conn:
            conn.execute("INSERT INTO messages (name, email, message) VALUES (?, ?, ?)",
                         (name, email, message))
        return redirect(url_for('contact'))

    return render_template("contact.html")


if __name__ == '__main__':
    from os import environ
    port = int(environ.get('PORT', 5000))  # Render ka dynamic port
    app.run(host='0.0.0.0', port=port)      # Public access for Render
