from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)

app.secret_key = "This is a secret key."

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods = ['POST'])
def process():
    session['name'] = request.form['user_name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('results_page.html')

if __name__=="__main__":
    app.run(debug=True)