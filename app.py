import flask
import json
import time


from simplejson import dump

app = flask.Flask (__name__)

@app.route('/', methods = ['GET'])
def home():
    dict_home = {'Page':'Home', 'Message':'API Request to home page', 'Timestamp':time.time(), 'Other_Queries':'/nothome, /another'}
    json_dump = json.dumps(dict_home)

    return json_dump

@app.route('/nothome/', methods = ['GET'])
def nothome():
    dict_nothome = {'Page':'NotHome', 'Message':'API Request to NotHome page', 'Timestamp':time.time()}
    json_dump = json.dumps(dict_nothome)

    return json_dump

@app.route('/another/', methods = ['GET'])
def another():
    dict_another = {'Page':'Another', 'Message':'API Request to Another page', 'Timestamp':time.time()}
    json_dump = json.dumps(dict_another)

    return json_dump

if __name__ == '__main__':
    app.run(port=5000)
