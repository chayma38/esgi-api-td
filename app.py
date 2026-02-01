from flask import Flask, jsonify
from resources.file import file_bp
from resources.folder import folder_bp
from resources.process import process_bp
from auth import auth_bp
from errors import register_error_handlers
from db import init_db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'votre_cle_secrete'
app.config['DATABASE'] = 'system_api.db'

# Initialiser la base SQLite
init_db(app.config['DATABASE'])

# Enregistrement des Blueprints
app.register_blueprint(file_bp, url_prefix='/files')
app.register_blueprint(folder_bp, url_prefix='/folders')
app.register_blueprint(process_bp, url_prefix='/processes')
app.register_blueprint(auth_bp, url_prefix='/auth')

# Gestion des erreurs
register_error_handlers(app)

@app.route('/')
@app.route('/')
def index():
    return jsonify({
        "message": "Bienvenue sur l'API Système Flask",
        "routes": {
            "Fichiers": {
                "GET": "/files?path=<chemin>",
                "POST": "/files  (JWT requis)",
                "PUT": "/files  (JWT requis)",
                "DELETE": "/files  (JWT requis)"
            },
            "Dossiers": {
                "GET": "/folders?path=<chemin>",
                "POST": "/folders  (JWT requis)",
                "DELETE": "/folders  (JWT requis)"
            },
            "Processus": {
                "GET": "/processes"
            },
            "Authentification": {
                "POST": "/auth/login"
            }
        },
        "note": "Voir le README pour plus de détails."
    })


if __name__ == "__main__":
    app.run(debug=True)
