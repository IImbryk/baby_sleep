import pickle
# from flask
model_path = 'models/baseline_pipline.pkl'


def read_model():
    with open(model_path, 'rb') as f_in:
        model = pickle.load(f_in)
    return model


if __name__ == '__main__':
    model = read_model()


