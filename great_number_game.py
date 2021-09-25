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
    randomNum = random.randint(1, 100)
    if "guess" not in session:
        session["guess"] = randomNum
    print(session)
    print(randomNum)
    return render_template('/index.html')

@app.route('/guess', methods=['POST'])
def ok():
    self.getRandomNumber()
    userGuess1 = int(request.form['userGuesser'])
    if userGuess1 == randomNum:
        print("Your done, you got it!")
        return render_template('/index.html')
    elif userGuess1 < randomNum:
        print("Try a little higher")
        return render_template('/index.html')
    elif userGuess1 > randomNum:
        print("Try a little lower")
        return render_template('/index.html')
    else:
        return render_template('/index.html')

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