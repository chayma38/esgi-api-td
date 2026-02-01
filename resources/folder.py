from flask import Blueprint, request, jsonify, current_app
import os
from auth import token_required
from db import log_action

folder_bp = Blueprint('folder', __name__)

@folder_bp.route('/', methods=['GET'])
def list_folders():
    path = request.args.get('path', '.')
    try:
        folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
        return jsonify({'folders': folders})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@folder_bp.route('/', methods=['POST'])
@token_required
def create_folder():
    data = request.json
    path = data.get('path')
    if not path:
        return jsonify({'error': 'Path requis'}), 400
    try:
        os.makedirs(path, exist_ok=True)
        log_action(current_app.config['DATABASE'], 'CREATE_FOLDER', path)
        return jsonify({'message': f'Dossier {path} créé'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@folder_bp.route('/', methods=['DELETE'])
@token_required
def delete_folder():
    data = request.json
    path = data.get('path')
    if not path:
        return jsonify({'error': 'Path requis'}), 400
    try:
        os.rmdir(path)
        log_action(current_app.config['DATABASE'], 'DELETE_FOLDER', path)
        return jsonify({'message': f'Dossier {path} supprimé'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
