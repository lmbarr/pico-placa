from flask import Flask, render_template,request
import main
app = Flask(__name__)


@app.route("/")
def template_test():
    return render_template('template.html', response="")


@app.route('/predict', methods=['POST'])
def predict():
    date = request.form['circulationDate']
    time = request.form['circulationTime']
    plate_number = request.form['plateNumber']
    print(date, time, plate_number)
    response = main.can_be_on_the_road(date, time, plate_number)
    return render_template('response.html', response=response)


if __name__ == '__main__':
    app.run(debug=True)
