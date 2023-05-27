from flask import Flask, jsonify, request
import jwt, secrets
from flask_mysqldb import MySQL
from functools import wraps
import os

# initialisation de Flask
app = Flask(__name__)
PORT = 8000
VPS_PRICE_LINUX_WINDOWS = 25.00
VPS_PRICE_MACOS = 50.00
VPS_MONTHLY_PRICE = 5.00

# configuration de l'intégration MySQL
app.config['MYSQL_HOST'] = "mysql"
app.config['MYSQL_USER'] = os.environ["MYSQL_USER"]
app.config['MYSQL_PASSWORD'] = os.environ["MYSQL_PASSWORD"]
app.config['MYSQL_DB'] = os.environ["MYSQL_DB"]
mysql = MySQL(app)

# configuration de l'intégration JWT
app.config['SECRET_KEY'] = secrets.token_hex(32)


# Fonction de vérification du JWT
def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = request.cookies.get('token')

        # vérifier que le token est présent
        if not token:
            return jsonify({'message': 'Token manquant'}), 401
        
        # vérifier que le token est valide
        try:
            session_data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except:
            return jsonify({'message': 'Token non valide'}), 401
        
        return f(session_data, *args, **kwargs)
    return decorator


### FONCTIONNALITÉ D'INSCRIPTION/CONNEXION ###
import login_routes

### FONCTIONNALITÉ DU COMPTE ###
import account_routes

### FONCTIONNALITÉ DES TICKETS ###
import ticket_routes


# Lancer l'application
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT, threaded=True, debug=True)
