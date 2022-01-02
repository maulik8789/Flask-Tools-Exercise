from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "m"

responses = []

@app.route('/')
def home_page():
    responses = []
    title = satisfaction_survey.title
    instruction = satisfaction_survey.instructions
    return render_template('home.html', 
                            htmltitle= title, 
                            htmlinstruction = instruction)

@app.route('/answer', methods=["POST"])
def add_ans():
    add_res = request.form['choice']
    responses.append(add_res)

    if len(responses) >= len(satisfaction_survey.questions):
        reponses = []  
        return render_template('/thanks.html')
    else:
        return redirect(f"/questions/{len(responses)}")

@app.route('/questions/<int:q_num>')
def que(q_num):

    if len(responses) != q_num:
        reponses = []
        flash(f"invalid question number")
        return render_template("/thanks.html")
    
    question = satisfaction_survey.questions[q_num].question
    choices = satisfaction_survey.questions[q_num].choices
    return render_template('survey0.html', 
                            htmlque = question, 
                            htmlchoices = choices,
                            htmlq_num = q_num)
