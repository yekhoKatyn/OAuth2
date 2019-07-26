from flask import Flask, Blueprint, request, render_template, redirect, url_for, request, jsonify

app = Flask(__name__)
app.debug = True


access_token = "Tsffdf"
token_type = "bearer"

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/ouath/autorize')
def autorize():
    client_id = request.args.get('client_id', type = str)
    redirect_uri = request.args.get('redirect_uri', type = str)
    print (client_id)
    return jsonify(url_s = "http://127.0.0.1:5000" + url_for('login'))
    #return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html', error = None)

@app.route('/submit', methods=['POST'])
def submit():
    return "Submit"

@app.route('/ouath/token')
def token():
    return jsonify(access_token = access_token,
    token_type = token_type)

@app.route('/user?id/<int:user_id>')
def profile(user_id):
    return "test"

if __name__ == '__main__':
    app.run(debug=True, port=5000)