from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def dojo_form():
    return render_template("index.html")

@app.route("/result", methods=['POST'])
def dojo_result():
    print(request.form)
    name = request.form['name']
    locations = request.form['locations']
    languages = request.form['languages']
    comment = request.form['comment']
    return render_template("show.html", name=name, locations=locations, languages=languages, comment=comment)

if __name__ == "__main__":
    app.run(debug = True)