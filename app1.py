from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>财富在向我招手!</h1><img src="file:///E:/flask/templates/sy.jfif">'