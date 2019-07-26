from flask import Flask, Blueprint, request, render_template, redirect, url_for, request, jsonify
import requests as req

app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return 'Hello, Client'

@app.route('/autorize')
def autorize():
    PARAMS = {'client_id':"12"} 
    r = req.get(url = "http://127.0.0.1:5000/ouath/autorize", params = PARAMS) 
    data = r.json()
    print(data)
    url_str = data["url_s"]
    return redirect(url_str)

if __name__ == '__main__':
    app.run(debug=True, port=5001)