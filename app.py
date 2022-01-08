from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "m"
debug = DebugToolbarExtension(app)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

@app.route('/')
def start():
    
    return redirect ('/begin_survey')

@app.route('/begin_survey')
def home_page():
    session["responses"] = []
    title = satisfaction_survey.title
    instruction = satisfaction_survey.instructions
    return render_template('home.html', 
                            htmltitle= title, 
                            htmlinstruction = instruction)

@app.route('/answer', methods=["POST"])
def add_ans():
    add_res = request.form['choice']
    resp = session["responses"]
    resp.append(add_res)
    session["responses"] = resp


    if len(resp) >= len(satisfaction_survey.questions):
        #session[“responses”] = []  
        return render_template('/thanks.html')
    else:
        return redirect(f"/questions/{len(resp)}")

@app.route('/questions/<int:q_num>')
def que(q_num):
    resp = session["responses"]
    if len(resp) != q_num:
        session["responses"] = []
        flash(f"invalid question number")
        return render_template("/thanks.html")
    
    question = satisfaction_survey.questions[q_num].question
    choices = satisfaction_survey.questions[q_num].choices
    return render_template('survey0.html', 
                            htmlque = question, 
                            htmlchoices = choices,
                            htmlq_num = q_num)