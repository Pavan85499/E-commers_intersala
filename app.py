<<<<<<< HEAD
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/home')
def home():
   return render_template('index.html')


@app.route('/products')
def products():
   return render_template("products.html")

@app.route('/singleproduct')
def singleproduct():
   return render_template("singleproduct.html")

@app.route('/about')
def adout():
   return render_template("about.html")
                     

@app.route('/contact')
def contact():
   return render_template("contact.html")

=======
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

@app.route('/home')
def index():
   return render_templates('index.html')

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'  # Replace with your DB URI (e.g., 'mysql://user:password@localhost/dbname')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # To suppress deprecation warnings

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define a sample model (table)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

# Example route
@app.route('/')
def index():
    return "Database connection is working!"

# Run the app
>>>>>>> e14daad907c954413b2f26bbceb5a2beaae19c52
if __name__ == '__main__':
    app.run(debug=True)
