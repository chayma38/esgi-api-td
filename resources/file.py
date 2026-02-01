from flask import Blueprint, request, jsonify, current_app
import os
from auth import token_required
from db import log_action

file_bp = Blueprint('file', __name__)

@file_bp.route('/', methods=['GET'])
def list_files():
    path = request.args.get('path', '.')
    try:
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        return jsonify({'files': files})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@file_bp.route('/', methods=['POST'])
@token_required
def create_file():
    data = request.json
    path = data.get('path')
    content = data.get('content', '')
    if not path:
        return jsonify({'error': 'Path requis'}), 400
    try:
        with open(path, 'w') as f:
            f.write(content)
        log_action(current_app.config['DATABASE'], 'CREATE_FILE', path)
        return jsonify({'message': f'Fichier {path} créé'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@file_bp.route('/', methods=['PUT'])
@token_required
def modify_file():
    data = request.json
    path = data.get('path')
    content = data.get('content')
    if not path or content is None:
        return jsonify({'error': 'Path et content requis'}), 400
    try:
        with open(path, 'w') as f:
            f.write(content)
        log_action(current_app.config['DATABASE'], 'MODIFY_FILE', path)
        return jsonify({'message': f'Fichier {path} modifié'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@file_bp.route('/', methods=['DELETE'])
@token_required
def delete_file():
    data = request.json
    path = data.get('path')
    if not path:
        return jsonify({'error': 'Path requis'}), 400
    try:
        os.remove(path)
        log_action(current_app.config['DATABASE'], 'DELETE_FILE', path)
        return jsonify({'message': f'Fichier {path} supprimé'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
