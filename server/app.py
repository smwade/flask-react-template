from flask import Flask, jsonify
from config import Config
from contorllers.users import get_users


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.DB_URL


@app.route('/', methods=['GET'])
def api_page():
    res = {'mesage': 'Welcome to the API!'}
    return jsonify(res)

# USERS
# ------------------------
@app.route('/users', methods=['GET'])
def _get_users():
    res = get_users()
    return jsonify(res)

if __name__ == '__main__':
    app.run()
