import pickle

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

@app.route('/predict', methods=['GET','POST'])
def check():
    if request.method == 'POST':
        data = (request.form.get('text'))
        print(data)

        if data is None:
            return jsonify({"message":"text not found"})
        else:

            text=preprocess(data)
            text=[text]
            ans=pred(text)
            response=jsonify(

                {
                    "predicted": ans
                }
            )
            return response

    else:
        return 'send the data through POST method'

@app.route('/', methods=['GET','POST'])
def index():
    return 'Machine Learning Inference'



if __name__ == '__main__':

    app.run(port='51',debug=True)




## deployed at heroku
#  https://la-identification.herokuapp.com/predict
