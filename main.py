from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


@app.route('/api/v1/predictions', methods=['GET'])
def predictions():
    cylinders = request.args['cylinders']
    displacement = request.args['displacement']
    horsepower = request.args['horsepower']
    weight = request.args['weight']
    acceleration = request.args['acceleration']
    model_year = request.args['model_year']

    map_origin = {'usa':1, 'europe':2, 'japan':3}
    origin = request.args['origin']
    origin = map_origin[origin]

    loaded_model = pickle.load(open('model.pkl', 'rb'))

# El orden de los datos debe ser el mismo que el del modelo
    new_data = [cylinders, 
                displacement, 
                horsepower, 
                weight, 
                acceleration, 
                model_year, 
                origin]

    prediction = loaded_model.predict([new_data])
    return jsonify({'prediction': prediction[0]})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
