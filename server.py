from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'esta es una clave secreta'

@app.route('/')
def encuesta():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():

    acepta = "No acepta terminos"
    if 'acepta' in request.form:
        acepta = "Si acepta terminos"

    session['encuesta'] = {
        "name": request.form["name"],
        "genero": request.form["genero"],
        "location": request.form["location"],
        "language": request.form["language"],
        "comment": request.form["comment"],
        "acepta": acepta,
    }
    return redirect('/result')

@app.route('/result')
def result():
    return render_template("results.html")

if __name__=="__main__":
    app.run(debug=True)