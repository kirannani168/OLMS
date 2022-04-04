from flask import Flask, redirect, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notices')
def notices():
    return render_template('notices.html')

@app.route('/hub')
def hub():
    return render_template('hub.html')

@app.route('/newoutpass')
def new_outpass():
    return render_template('apply_outpass.html')
@app.route('/user')
def user():
    return render_template('user.html')

if __name__ == '__main__':
    app.run(debug=True)