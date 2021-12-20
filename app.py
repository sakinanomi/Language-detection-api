import pickle
from sklearn.feature_extraction.text import CountVectorizer
from flask_cors import CORS

# load the model
model = pickle.load(open('finalized_model.sav', 'rb'))

# load the vectorizer
vectorizer = pickle.load(open('vectorizer.pickle', 'rb'))

def preprocess(text):
    text = text.lower()
    return text

# make a prediction
def pred(text):

    predicted=(model.predict(vectorizer.transform(text)))
    return str(predicted[0])


from flask import Flask,request, jsonify
import json

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def check():
    data = (request.form)
    print('The data is' ,data)
    first_key = list(data.keys())[0]


    print(first_key)
    print("The datatype is",type(first_key))

    return 'Hello'

@app.route('/', methods=['GET'])
def index():
    return 'Machine Learning Inference'


if __name__ == '__main__':

    app.run(debug=True)




## deployed at heroku
#  https://la-identification.herokuapp.com/predict
