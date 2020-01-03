from flask import Flask,render_template
from flask_restful import Api,Resource,reqparse,abort,request
import pandas as pd
import dill as pickle
from pathlib import Path
import sys

pickle._dill._reverse_typemap['ClassType'] = type



#app = Flask(__name__,template_folder='/Machine Learning Projects/Simple_NLP_Model_Deployment/templates')
root_path = Path(sys.executable).parent if getattr(sys, 'frozen', False) else Path(__file__).parent
app = Flask(__name__.split('.')[0], root_path=root_path)
api = Api(app)

filename= 'model.pkl'
#with open('./Machine Learning Projects/Simple_NLP_Model_Deployment/model/'+filename ,'rb') as f:
with open('./model/'+filename ,'rb') as f:

    classifier = pickle.load(f)

#parser = reqparse.RequestParser()
#parser.add_argument('query')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods = ['POST']) 
def PredictSentiment():
    search = request.form['Review']
    user_query = pd.DataFrame({'Phrase':search},index = [0])

    model_prediction = classifier.predict(user_query)

    if model_prediction == 0:
        pred_text = 'Negative'
    else:
        pred_text = 'Positive'

#    output = {'Prediction': pred_text}

#    return render_template('sentiment.html',
#                           prediction = output)
    return render_template('index.html',
                           prediction_text = 'The Predicted Sentiment is {}'.format(pred_text))

if __name__ == '__main__':
    app.run(port = 5000, debug=True,use_reloader=False)
