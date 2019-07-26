from flask import Flask, Blueprint, request, render_template, redirect, url_for, request, jsonify
import requests as req

app = Flask(__name__)
app.debug = True

redirect_uri_get = "https://global.consent.azure-apim.net/redirect"
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1bmlxdWVfbmFtZSI6ImhyQHNtYXJ0YnVzaW5lc3MuY29tLnVhIiwiZW1haWwiOiJockBzbWFydGJ1c2luZXNzLmNvbS51YSIsIk5vdGVib29rSWQiOiI3MTMzNDAiLCJJc0VtcGxveWVyIjoiMSIsIk11bHRpVXNlcklkIjoiMTY2NDYyIiwiQ29tcGFueU5hbWUiOiLQodCc0JDQoNCiINCR0JjQl9Cd0JXQoSwg0J7QntCeIiwiVXNlck5hbWUiOiJIUiIsIlJvbGVJZCI6IjEiLCJJc0FsbG93ZWRUb1B1Ymxpc2giOiJ0cnVlIiwiUGhvbmUiOiIzODA0NDU4NTM1NTAiLCJBdmF0YXJVcmwiOiJTTUFSVC1CSVpORVMtT09PXzIwMTQwNTI5MDMyNDE1LmpwZyIsImlzcyI6InJhYm90YS51YSIsImF1ZCI6InJhYm90YS51YSIsImV4cCI6MTcyMTk5NTcxNH0.-wNDN6ABF4nEzyKEXJhEUlvsVkMw7CCsjk5sNYHGSF4"
token_type = "bearer"

dict_params = {}
dict_params["code"] = "fdfdsfds32ff"

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/ouath/autorize')
def autorize():
    client_id = request.args.get('client_id', type = str)
    redirect_uri = request.args.get('redirect_uri', type = str)
    state = request.args.get('state', type = str)
    dict_params["redirect_uri"] = redirect_uri
    dict_params["state"] = state
    #redirect_uri_get = redirect_uri
    print ("redirecet url = " + redirect_uri)
    print("state = " + state) 
    #return jsonify(url_s = "http://64.71.146.9:5000" + url_for('login'))
    return redirect(url_for('login'))

@app.route('/ouath/refresh', methods=['POST'])
def refresh():
    return jsonify(access_token = access_token,
                token_type = token_type,
                expires_in = 60)

@app.route('/login')
def login():
    return render_template('login.html', error = None)

@app.route('/submit', methods=['POST'])
def submit():
    #PARAMS = {'code':"fdfdsfds32ff", "state":"4152c75a-948f-4c10-ac11-fa22463ae369_europe-001"} 
    print(dict_params)
    PARAMS = {}
    PARAMS["state"] = dict_params["state"]
    #PARAMS['code'] = dict_params['code']
    url = f"{dict_params['redirect_uri']}?state={dict_params['state']}&code={dict_params['code']}"
    #response = req.get(url = url)
    #print(response.content)
    #?code={dict_params['code']}?
    #url = f"{dict_params['redirect_uri']}?state={dict_params['state']}&code={dict_params['code']}"
    #print(url)
    #return 'test"'
    return redirect(url)
    

@app.route('/ouath/token', methods=['POST'])
def token():
    return jsonify(access_token = access_token,
                token_type = token_type,
                expires_in = 60)

@app.route('/data', methods = ['POST'])
def get_data():
    return 'Hello, World!'

@app.route('/user?id/<int:user_id>')
def profile(user_id):
    return "test"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)