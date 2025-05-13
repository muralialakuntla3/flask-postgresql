from flask import Flask, request, render_template_string
import psycopg2

app = Flask(__name__)

# PostgreSQL connection config
conn = psycopg2.connect(
    host="azure2501db.postgres.database.azure.com",
    database="demo_app",
    user="adminuser",
    password="Crmedify@12345"
)
cursor = conn.cursor()

# HTML Form Template
form_template = """
<!doctype html>
<title>PostgreSQL Form</title>
<h2>Enter User Details</h2>
<form method=post>
  Name: <input type=text name=name><br><br>
  Email: <input type=email name=email><br><br>
  Number: <input type=text name=number><br><br>
  <input type=submit value=Submit>
</form>
{% if message %}
  <p><strong>{{ message }}</strong></p>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        number = request.form["number"]
        sql = "INSERT INTO users (name, email, number) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, email, number))
        conn.commit()
        message = "Data inserted successfully!"
    return render_template_string(form_template, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



