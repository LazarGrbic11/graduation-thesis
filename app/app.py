from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# MySQL configuration (you can change the host, user, password, and db)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@db:3306/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database connection
db = SQLAlchemy(app)

# Define a model (table) for the database
class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)

    def __init__(self, content):
        self.content = content

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and insert into the database
@app.route('/submit', methods=['POST'])
def submit():
    content = request.form.get('content')
    if content:
        new_data = Data(content)
        db.session.add(new_data)
        db.session.commit()
        return redirect('/')
    return "Error: No content provided", 400

if __name__ == '__main__':
    # Make sure tables are created in the database
    db.create_all()
    app.run(host='0.0.0.0', port=8081)

