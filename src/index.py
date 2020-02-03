"""
    index.py
    ---------
    This python module contains all the flask server configuration.
"""
from flask import Flask, render_template,request
from src.main import can_be_on_the_road
app = Flask(__name__)


@app.route("/")
def template_test():
    """
    This function contains the functionality when we first hit the index page.
    :return: The rendered version of templates/template.hmtl.
    """
    return render_template('template.html', response="")


@app.route('/predict', methods=['POST'])
def predict():
    """
    This route /predict servers the answer of wether or not a vehicule
    can circulate according to the pìco y placa.
    :return: The rendered version of templates/response.hmtl.
    """
    date = request.form['circulationDate']
    time = request.form['circulationTime']
    plate_number = request.form['plateNumber']
    response = can_be_on_the_road(date, time, plate_number)
    return render_template('response.html', response=response)


if __name__ == '__main__':
    app.run(debug=True)
