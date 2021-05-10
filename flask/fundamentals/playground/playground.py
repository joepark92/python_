from flask import Flask, render_template
app = Flask(__name__)
    
@app.route("/play")
def play():
    return render_template("index.html", page = "play")

@app.route("/play/<num>")
def playmore(num):
    return render_template("index.html", page = "playmore", num = int(num))

@app.route("/play/<num>/<colorchange>")
def num_and_color(num, colorchange):
    return render_template("index.html", page = "color", num = int(num), colorchange = str(colorchange))

if __name__=="__main__":
    app.run(debug=True)