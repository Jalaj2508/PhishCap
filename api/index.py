import pickle
import numpy as np
from feature import FeatureExtraction

def handler(request):
    # Get URL from query or body
    url = request.get("url")
    if not url:
        return {
            "statusCode": 400,
            "body": "Missing 'url' parameter"
        }

    whitelist = ['google.com', 'microsoft.com', 'github.com']
    if any(kw in url for kw in whitelist):
        return {
            "statusCode": 200,
            "body": "1.0"
        }

    file = open("pickle/model.pkl","rb")
    gbc = pickle.load(file)
    file.close()
    obj = FeatureExtraction(url)
    x = np.array(obj.getFeaturesList()).reshape(1,30)
    y_pro_non_phishing = gbc.predict_proba(x)[0,1]
    return {
        "statusCode": 200,
        "body": str(round(y_pro_non_phishing,2))
    }
