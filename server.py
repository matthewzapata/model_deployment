from flask import Flask
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world!'

@app.route('/roll-dice')
def roll():
    number = np.random.randint(1, 7)
    return f'You rolled a {number}'