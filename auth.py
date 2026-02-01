from flask import Blueprint, request, jsonify, current_app
import jwt
import datetime
from functools import wraps

auth_bp = Blueprint('auth', __name__)

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('x-access-token')
        if not token:
            return jsonify({'error': 'Token manquant'}), 401
        try:
            jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        except:
            return jsonify({'error': 'Token invalide'}), 401
        return f(*args, **kwargs)
    return decorated

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    # Utilisateur admin/password pour simplifier
    if username == 'admin' and password == 'password':
        token = jwt.encode(
            {'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)},
            current_app.config['SECRET_KEY'],
            algorithm='HS256'
        )
        return jsonify({'token': token})
    return jsonify({'error': 'Identifiants invalides'}), 401
