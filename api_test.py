import flask
import json
import time

app = flask.Flask (__name__)


@app.route('/', methods = ['GET'])
def home():
    dict_home = {'Page':'Home', 'Message':'Api Request to home page', 'Timestamp':time.time()}
    json_dump = json_dump(dict_home)

    return json_dump

@app.route('/nothome/', methods = ['GET'])
def nothome():
    dict_nothome = {'Page':'NotHome', 'Message':'Api Request to NotHome page', 'Timestamp':time.time()}
    json_dump = json_dump(dict_nothome)

    return json_dump

@app.route('/another/', methods = ['GET'])
def another():
    dict_another = {'Page':'Another', 'Message':'Api Request to Another page', 'Timestamp':time.time()}
    json_dump = json_dump(dict_another)

    return json_dump

if __name__ == '__main__':
    app.run(port=7777)
