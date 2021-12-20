import pickle
from sklearn.feature_extraction.text import CountVectorizer

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

@app.route('/predict', methods=['POST'])
def check():
    data = json.loads(request.data) #json.loads parses the json object into python dict . request.data requests for data
    text = data.get("text",None) # get method returns the value of the item with specified key

    if text is None:
        return jsonify({"message":"text not found"})
    else:
        t=data['text']
        t=preprocess(t) #making int lower
        t=[t] #converting into list
        ans=pred(t) #predict the language
        return jsonify({"predicted ":ans})


@app.route('/', methods=['GET'])
def index():
    return 'Machine Learning Inference'


if __name__ == '__main__':

    app.run(debug=True)




## deployed at heroku
#  https://la-identification.herokuapp.com/predict
