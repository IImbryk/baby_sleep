import pickle
from flask import Flask
from flask import request, jsonify

app = Flask('baby_sleep')
model_path = 'models/baseline_pipline.pkl'


@app.route('/predict', methods=['POST'])
def predict_single(pipeline):
    input_vector = request.get_json()
    y = pipeline.predict(input_vector)
    result = {
        'class_output': int(y)
    }

    return jsonify(result)


@app.route('/baby_sleep', methods=['GET'])
def test_get():
    return 'Hi'


if __name__ == '__main__':
    with open(model_path, 'rb') as f_in:
        model = pickle.load(f_in)

    app.run(debug=True, host='0.0.0.0', port=9696)


