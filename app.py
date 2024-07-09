from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return "<h2>This is the about page </h2> <p> And also hello first deployment"


if __name__ == "__main__":
    app.run(debug=True)