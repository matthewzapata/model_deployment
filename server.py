from flask import Flask, render_template, request
import numpy as np
from model import predict

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', name='Ada')

@app.route('/roll-dice')
def roll():
    number = np.random.randint(1, 7)
    return render_template('roll-dice.html', number=number)

@app.route('/animal-shelter-project')
def asp():
    return render_template('animal-shelter-project.html')

@app.route('/my-first-form')
def my_first_form():
    return render_template('my-first-form.html')

@app.route('/make-greeting', methods=['POST'])
def handle_form_submission():
    name = request.form['name']
    title = request.form['title']

    greeting = 'Hello, '

    if title != '':
        greeting += title + ' '

    greeting += name + '!'

    return render_template('greeting.html', greeting=greeting)

@app.route('/ham-or-spam-input')
def model_input():
    return render_template('model-input.html')

@app.route('/ham-or-spam-predictions', methods=['POST'])
def model_output():
    text = request.form['mtext']
    prediction = predict(text)
    return render_template('model-output.html', prediction=prediction)