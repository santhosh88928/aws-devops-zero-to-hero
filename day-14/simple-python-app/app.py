from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, let make good'

if __name__ == '__main__':
    app.run()

