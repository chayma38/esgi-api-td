# API Système Flask – Documentation Technique

## Présentation
Cette API Flask sert de **pont entre le système d’exploitation et une interface web/API**.  
Elle permet de :

- Lister, créer, modifier et supprimer des **fichiers**  
- Lister, créer et supprimer des **dossiers**  
- Lister les **processus actifs**  
- Gérer un **système d’authentification simple** via JWT  
- Loguer les actions dans une base SQLite

---
## Structure du projet
API/

├── app.py              
├── auth.py             
├── db.py               
├── errors.py         
├── requirements.txt    
├── README.md

└── resources/         
    ├── init.py    
    ├── file.py         
    ├── folder.py      
    └── process.py     


---

## Explication du code

### `app.py`

- Crée l’application Flask :  

```
app = Flask(__name__)
```

- Initialise la base de données :
```
init_db()
```
- Enregistre les Blueprints :
```
app.register_blueprint(file_bp, url_prefix='/files')
app.register_blueprint(folder_bp, url_prefix='/folders')
app.register_blueprint(process_bp, url_prefix='/processes')
app.register_blueprint(auth_bp, url_prefix='/auth')
```
- Enregistre les gestionnaires d’erreurs personnalisés :
```
register_error_handlers(app)
```
- Fournit un endpoint / qui renvoie un JSON avec toutes les routes disponibles

### `resources/file.py, folder.py, process.py`
Chaque fichier contient un Blueprint Flask : file_bp, folder_bp, process_bp

Routes exposées pour GET/POST/PUT/DELETE selon le type de ressource

Utilise token_required pour sécuriser les routes POST/PUT/DELETE

db.log_action logue chaque action dans la base SQLite

### `auth.py`
Contient le Blueprint auth_bp pour l’authentification

Vérifie username/password et renvoie un JWT token

Le token est utilisé dans les en-têtes x-access-token pour les routes sécurisées

### `db.py`
Initialise la base SQLite locale system_api.db

Stocke les logs : création, modification, suppression de fichiers/dossiers

Facilite le suivi des actions

### `errors.py`
Centralise la gestion des erreurs Flask

Retourne des réponses JSON cohérentes pour :

400 Bad Request

401 Unauthorized

404 Not Found

500 Internal Server Error