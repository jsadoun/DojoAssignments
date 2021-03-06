from flask import Flask,request,redirect,session,render_template
import random

app = Flask(__name__)
app.secret_key = "123123"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():
    session['rand']  = random.randint(1,100)
    session['guess'] = int(request.form['guess'])
    session['res']   = ""

    cl = session['guess']
    sv = session['rand']

    if cl == sv:
        session['res'] = "You win!"
    elif cl > sv:
        diff = cl-sv
        session['res'] = "You were "+str(diff)+" numbers above!"
    elif cl < sv:
        diff = sv-cl
        session['res'] = "You were "+str(diff)+" numbers below!"

    return render_template('index.html')

app.run(debug=True)