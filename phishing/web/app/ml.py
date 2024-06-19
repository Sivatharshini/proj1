import pickle


def predict(url):
    loaded_model = pickle.load(open('phishing.pkl', 'rb'))
    result = loaded_model.predict(url)
    return result