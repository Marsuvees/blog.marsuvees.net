from flask import Flask
app = Flask(__name__, static_url_path='/assets', static_folder='assets', template_folder='views')

from auth import auth_bp
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app(port=5000, host="127.0.0.1", debug=True)