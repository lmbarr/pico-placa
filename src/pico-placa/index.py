from flask import Flask, render_template,request

app = Flask(__name__)


@app.route("/")
def template_test():
    return render_template('template.html', response="")


@app.route('/predict', methods=['POST'])
def predict():
    date = request.form['circulationDate']
    time = request.form['circulationTime']
    plate_number = request.form['plateNumber']

    print(type(date), date)
    print(type(time), time)
    return render_template('response.html', response="Vehiculo no puede circular")


if __name__ == '__main__':
    app.run(debug=True)
