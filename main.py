from flask import Flask
app = Flask(__name__, static_url_path='/static')


if __name__ == "__main__":
    app(port=5000, host="127.0.0.1", debug=True)