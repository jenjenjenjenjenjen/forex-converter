from crypt import methods
from flask import Flask, render_template, request, flash, redirect
from forex_python.converter import CurrencyRates, CurrencyCodes
from funcs import *

app = Flask(__name__)
app.secret_key='dhdsakf6e4i8a!'

@app.route('/')
def home():
    """render base template"""
    return render_template('base.html')

@app.route('/convert', methods=['POST'])
def redirect_to_result():
    """check if codes are valid and redirect user to home page"""
    get_form_info()
    return redirect('/')
    

