from flask import Flask
from flask import render_template
from flask import session
from flask import redirect
from flask import request
import random

app = Flask( __name__ )
app.secret_key = "secret"

@app.route( '/', methods=['GET'] )
def getRandomNumber():
    if "guess" not in session:
        session["guess"] = random.randint(1, 100)
        print(session)
    if request.form['userGuesser'] != False:
        
    return render_template('index.html', randomNum = session["guess"])

@app.route('/guess', methods=['POST'])
def ok():
    session['userGuess1'] = int(request.form['userGuesser'])
    return redirect( '/' )

# @app.route('/guess',methods=['POST'])
# def userGuess():
#     session['userGuesser'] = int(request.form['userGuesser'])
#     return redirect('/')

@app.route( '/reset', methods=['GET'] )
def closeSession():
    session.clear()
    return redirect( '/' )

if __name__ == "__main__":
    app.run( debug = True )