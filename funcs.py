
from flask import Flask, flash, request
from forex_python.converter import CurrencyRates, CurrencyCodes

app = Flask(__name__)
app.secret_key='dhdsakf6e4i8a!'

def get_form_info():
    codes = CurrencyCodes()
    convert_from = request.form["converting-from"].upper()
    convert_to = request.form["converting-to"].upper()

    flash_error_messages(codes, convert_from, convert_to)

def flash_error_messages(codes, convert_from, convert_to):
    if codes.get_currency_name(convert_from) == None:
        flash(f"Invalid code: {convert_from}")
    elif codes.get_currency_name(convert_to) == None:
        flash(f"Invalid code: {convert_to}")
    else:
        convert(convert_from, convert_to)

def convert(convert_from, convert_to):
    rates = CurrencyRates()
    amount = request.form["amount"]
    if isinstance(int(request.form["amount"]), int):
        result = rates.convert(convert_from, convert_to, int(amount))
        flash(f"The result is {result}.")
    else:
        flash("Invalid amount")
