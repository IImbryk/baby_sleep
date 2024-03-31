import joblib
from flask import Flask
from flask import request, jsonify

app = Flask('baby_sleep')
model_path = 'models/baseline_pipline.pkl'


@app.route('/predict', methods=['POST'])
def predict_single():
    input_vector = request.get_json()
    # y = model.predict(input_vector)
    y = model.predict([list(input_vector.values())])
    result = {
        'class_output': int(y)
    }

    return jsonify(result)


@app.route('/baby_sleep', methods=['GET'])
def test_get():
    return 'Hi'


if __name__ == '__main__':

    # read model
    model = joblib.load(model_path)

    app.run(debug=True, host='0.0.0.0', port=9696)





