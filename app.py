from flask import Flask
from os import getenv
app = Flask(__name__)

@app.route('/')
def home():
    return f"{getenv('my_text')}, ok? Really."

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
