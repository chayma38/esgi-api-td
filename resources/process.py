from flask import Blueprint, jsonify
import psutil

process_bp = Blueprint('process', __name__)

@process_bp.route('/', methods=['GET'])
def list_processes():
    processes = [p.info for p in psutil.process_iter(['pid', 'name', 'username'])]
    return jsonify({'processes': processes})
