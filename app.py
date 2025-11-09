from flask import Flask, render_template, request, redirect, url_for
import sqlite3, requests, os

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
    GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")  # ✅ Read token safely from environment

    github_projects = []

    try:
        headers = {"User-Agent": "portfolio-app"}

        if GITHUB_TOKEN:
            headers["Authorization"] = f"token {GITHUB_TOKEN}"

        github_url = f"https://api.github.com/users/{GITHUB_USER}/repos"
        response = requests.get(github_url, headers=headers, timeout=8)

        if response.status_code == 200:
            github_projects = response.json()[:3]  # ✅ Show only 3 latest projects
            print(f"✅ GitHub Projects Loaded: {len(github_projects)}")
        else:
            print(f"⚠️ GitHub API Error: {response.status_code}")
    except Exception as e:
        print("❌ GitHub API Exception:", e)

    # --- Fallback (local list if API fails) ---
    if not github_projects:
        github_projects = [
            {"name": "creative_portfolio_builder", "html_url": "https://github.com/manish1103/creative_portfolio_builder", "description": "Flask-based personal portfolio site."},
            {"name": "Quiz", "html_url": "https://github.com/manish1103/Quiz", "description": "Python Quiz Game with Flask backend."},
            {"name": "StudentManagementSystem", "html_url": "https://github.com/manish1103/StudentManagementSystem", "description": "Java + MariaDB Student Management App."}
        ]

    # --- Behance Projects ---
    behance_projects = [
        {"title": "School Advertising Poster", "desc": "A promotional school poster designed with bold visuals.", "url": "https://www.behance.net/gallery/229181937/school-advertising-poster"},
        {"title": "Promotional Post", "desc": "Created using Photopea, this project highlights creative product marketing.", "url": "https://www.behance.net/gallery/228352005/Promotional-Post"},
        {"title": "It's Coffee Time", "desc": "Figma-based café poster design — cozy tones and typography to attract coffee lovers.", "url": "https://www.behance.net/gallery/223576721/Its-Coffee-Time"}
    ]

    return render_template("index.html",
                           github_projects=github_projects,
                           behance_projects=behance_projects)

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

# ---------- RUN APP ----------
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
