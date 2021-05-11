from flask import Flask, redirect, session, render_template, request
import random
app = Flask(__name__)
app.secret_key = 'mojodojo'

@app.route('/')
def initial():
    session['attempts'] = 0
    session['randNum'] = random.randint(1, 100)
    return render_template("index.html")

@app.route("/entry", methods=["POST"])
def result():
    session['entry'] = int(request.form['entry'])
    session['attempts'] += 1
    print(session['randNum'])
    return render_template("entry.html")

if __name__ == "__main__":
    app.run(debug=True)