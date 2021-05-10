from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def checkerboard():
    return render_template("index.html", row=4, col=4, color1="red" ,color2="black")

@app.route("/<row>")
def totalRows(row):
    return render_template("index.html", row=int(int(row)/2), col=4, color1="red" ,color2="black")

@app.route("/<row>/<col>")
def totalColumns(row, col):
    return render_template("index.html", row=int(int(row)/2), col=int(int(col)/2), color1="red" ,color2="black")

@app.route("/<row>/<col>/<color1>/<color2>")
def checkerboardColor(row, col, color1, color2):
    return render_template("index.html", row=int(int(row)/2), col=int(int(col)/2), color1=str(color1) ,color2=str(color2))

if __name__=="__main__":
    app.run(debug=True)