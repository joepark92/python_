from flask import Flask, render_template, request, redirect, session # don't forget to import redirect!
app = Flask(__name__)
app.secret_key = "dojocounter"

@app.route("/")
def counter():
    session['counter'] = 0
    if 'counter' in session:
        print("KEY EXIST")
    else:
        print("key 'count' does NOT exist")
    return redirect("/count")

@app.route("/count")
def show_page():
    session['counter'] += 1
    return render_template("index.html")

@app.route("/destroy_session")
def destroy_session():
    session.clear()
    return redirect("/")

@app.route("/plustwo")
def plustwo():
    session['counter'] += 2
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)