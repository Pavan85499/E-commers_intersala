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

if __name__ == '__main__':
   app.run(debug = True)