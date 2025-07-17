# PhishCap
<img width="500" height="500" alt="PhishCap copy" src="https://github.com/user-attachments/assets/2d4f0e63-6139-4c3c-b5a0-e756b8d70f3a" />

## Table of Content
  * [Introduction and Motivation](#Introduction-and-Motivation)
  * [Installation](#installation)
  * [Directory Tree](#directory-tree)
  * [Result](#result)
  * [Conclusion](#conclusion)


## Introduction and Motivation

The life of a Modern Day Human being is next to impossible to be imagined without Internet.The expanse till which our life in automated digitally is deep and thus complex as well.And due to this, a lot of us tend to fall for cyber crimes and frauds, one of them is Phishing.According to phishing.org, Phishing is a cybercrime in which a target or targets are contacted by email, telephone or text message by someone posing as a legitimate institution to lure individuals into providing sensitive data such as personally identifiable information, banking and credit card details, and passwords.

There are ways with which phishing attacks are found out, but attackers also evolve with time, but one of the robust ways to catch the attackers is through Machine Learning.Thus, as an apiring tech and Cyber Security enthusiast, I decide to develop a project which can detect whether a website is legitimate or not, via Machine Learning, which I fancily say to be "PhishCap".

Before moving forwards, I have to give credit to Vaibhav Bichave(https://github.com/vaibhavbichave), to be the one who first worked on this project 3 years ago, as I was fortunate to who found out about his project and source code which acted as a backbone to mine as well, as I was able to recycle his original model with newer data and changes. I am always fortunate to have amazing developers who's contribution and work helps aspiring and learning techies like me!


## Installation
The Code is written in Python 3.10.12. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```

## Directory Tree 
```
├── .ipynb_checkpoints
│   ├── PhishCap-checkpoint.ipynb
├── _pycache_
│   ├── feature.cpython-38.pyc
│   ├── feature.cpython-39.pyc
├── catboost_info
│   ├── learn
│   |   ├── events.out.tfevents
│   ├── learn_error.tsv
│   ├── time_left.tsv
├── pickle
│   ├── model.pkl
├── static
│   ├── styles.css
│   ├── Logo.png
│   ├── favicon.png
├── templates
│   ├── index.html
├── Dockerfile
├── PhishCap.ipynb
├── Procfile
├── README.md
├── app.py
├── feature.py
├── phishing.csv
├── requirements.txt
├── runtime.txt

```

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/3/31/NumPy_logo_2020.svg" width=200>](https://numpy.org/doc/) [<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg" width=200>](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)
[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/8/84/Matplotlib_icon.svg" width=100>](https://matplotlib.org/)
[<img target="_blank" src="https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png" width=200>](https://scikit-learn.org/stable/) 
[<img target="_blank" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcScq-xocLctL07Jy0tpR_p9w0Q42_rK1aAkNfW6sm3ucjFKWML39aaJPgdhadyCnEiK7vw&usqp=CAU" width=200>](https://flask.palletsprojects.com/en/2.0.x/) 

## Result

Accuracy of various model used for URL detection
<br>

<br>

||ML Model|	Accuracy|  	f1_score|	Recall|	Precision|
|---|---|---|---|---|---|
0|	Gradient Boosting Classifier|	0.974|	0.977|	0.994|	0.986|
1|	CatBoost Classifier|	        0.972|	0.975|	0.994|	0.989|
2|	XGBoost Classifier| 	        0.969|	0.973|	0.993|	0.984|
3|	Multi-layer Perceptron|	        0.969|	0.973|	0.995|	0.981|
4|	Random Forest|	                0.967|	0.971|	0.993|	0.990|
5|	Support Vector Machine|	        0.964|	0.968|	0.980|	0.965|
6|	Decision Tree|      	        0.960|	0.964|	0.991|	0.993|
7|	K-Nearest Neighbors|        	0.956|	0.961|	0.991|	0.989|
8|	Logistic Regression|        	0.934|	0.941|	0.943|	0.927|
9|	Naive Bayes Classifier|     	0.605|	0.454|	0.292|	0.997|

Feature importance for Phishing URL Detection 
<br><br>
![image](https://user-images.githubusercontent.com/79131292/144603941-19044aae-7d7b-4e9a-88a8-6adfd8626f77.png)

