import pickle
from flask import Flask

app = Flask('baby_sleep')
model_path = 'models/baseline_pipline.pkl'


@app.route('/baby_sleep', methods=['GET'])
def read_model():
    with open(model_path, 'rb') as f_in:
        model = pickle.load(f_in)
    return 'Hi'


if __name__ == '__main__':
    model = read_model()
    app.run(debug=True, host='0.0.0.0', port=9696)


