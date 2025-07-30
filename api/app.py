#importing required libraries


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn import metrics
import warnings
import pickle
warnings.filterwarnings('ignore')
from feature import FeatureExtraction

model_path = os.path.join(os.path.dirname(__file__), '..', 'pickle', 'model.pkl')
file = open(model_path, "rb")
gbc = pickle.load(file)
file.close()


base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
template_dir = os.path.join(base_dir, 'templates')
static_dir = os.path.join(base_dir, 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        url = request.form["url"]

        #Whitelist Websites
        whitelist = ['google.com', 'microsoft.com', 'github.com']
        if any(kw in url for kw in whitelist):
            return render_template('index.html', xx=1.0, url=url)

        #ML-based prediction
        obj = FeatureExtraction(url)
        x = np.array(obj.getFeaturesList()).reshape(1,30) 

        y_pred =gbc.predict(x)[0]
        #1 is safe       
        #-1 is unsafe
        y_pro_phishing = gbc.predict_proba(x)[0,0]
        y_pro_non_phishing = gbc.predict_proba(x)[0,1]
        # if(y_pred ==1 ):
        pred = "It is {0:.2f} % safe to go ".format(y_pro_non_phishing * 100)
        return render_template('index.html', xx=round(y_pro_non_phishing,2), url=url)
    return render_template("index.html", xx=-1)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    