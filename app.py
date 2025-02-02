import pickle
from flask import Flask,request,app,jsonify,url_for_render_templatecle
import numpy as np
import pandas as pd

app=Flask(__name__)
#load the model
model=pickle.load(open('LRmodel.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')