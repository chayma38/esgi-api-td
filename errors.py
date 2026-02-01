from flask import jsonify

def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({'error': 'Ressource non trouvée'}), 404

    @app.errorhandler(500)
    def internal_error(e):
        return jsonify({'error': 'Erreur interne du serveur'}), 500

    @app.errorhandler(401)
    def unauthorized(e):
        return jsonify({'error': 'Non autorisé'}), 401
