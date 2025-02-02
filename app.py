import pickle
from flask import Flask,request,app,jsonify,render_template
import numpy as np
import pandas as pd

app=Flask(__name__)
#load the model
model=pickle.load(open('LRmodel.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_API',methods=['POST'])

def predict_api():
    data=request.json['data']
    print(data)
    raw_data=np.array(list(data.values())).reshape(1,-1)
    print(raw_data)
    scaled_data=scalar.transform(raw_data)
    output=model.predict(scaled_data)
    print(output)
    return jsonify(output[0])

if __name__=="__main__":
    app.run(debug=True)
