from flask import Flask
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
boostrap = Bootstrap5(app)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
