from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    # Retrieve user input from the form
    sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])

    # Perform any prediction logic here without using the scipy model
    # For example, you could use a simple if-else statement or another model
    # to predict the class based on the input features.

    # Example prediction logic:
    if sepal_length < 5.0:
        result = "Iris-setosa"
    elif sepal_length >= 5.0 and petal_length < 5.5:
        result = "Iris-versicolor"
    else:
        result = "Iris-virginica"

    # Render the result on the template
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
