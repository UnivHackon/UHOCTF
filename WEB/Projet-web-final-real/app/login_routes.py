# imports
from __main__ import app, mysql
from flask import jsonify, request, make_response
import re, jwt
from hashlib import sha256

# POST inscription
@app.route('/api/register', methods=['POST'])
def post_register():
    # vérifier la présence des paramètres nécessaires
    if (request.json is None) or ('email' not in request.json) or ('username' not in request.json) or ('password' not in request.json) or ('izly_wallet' not in request.json):
        return jsonify({'message': 'Paramètres requis manquants'}), 400
    
    email = request.json['email']
    username = request.json['username']
    password = request.json['password']
    izly_wallet = request.json['izly_wallet']

    # vérifier que les paramètres sont des chaînes de caractères
    if type(email) is not str or type(username) is not str or type(password) is not str or type(izly_wallet) is not str:
        return jsonify({'message': 'Données de paramètre non valides'}), 400
    
    # vérifier que l'email est valide
    if not re.fullmatch(r'\b[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email):
        return jsonify({'message': 'Email non valide'}), 400
    
    # vérifier que le nom d'utilisateur est valide
    if len(username) < 4 or len(username) > 255:
        return jsonify({'message': 'Longueur du nom d\'utilisateur non valide'}), 400
    
    # vérifier que le nom d'utilisateur n'est pas déjà utilisé
    cur = mysql.connection.cursor()
    cur.execute("SELECT username FROM Student WHERE username=%s", (username,))
    users_found = cur.rowcount
    cur.close()
    username_taken = (users_found > 0)

    if username_taken:
        return jsonify({'message': 'Nom d\'utilisateur déjà utilisé'}), 500
    
    # vérifier que le mot de passe est valide
    if len(password) < 12 or len(password) > 255:
        return jsonify({'message': 'Le mot de passe ne respecte pas les exigences de longueur'}), 400
    
    # vérifier que le portefeuille izly est valide
    if not re.fullmatch(r'0x[0-9a-fA-F]+', izly_wallet):
        return jsonify({'message': 'Portefeuille izly non valide'}), 400

    # insérer l'utilisateur dans la base de données
    #UHOCTF{Fake_flag_1}

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO Student (email, username, password, blocked, izly_wallet) VALUES (%s, %s, %s, %s, %s)", (email, username, sha256(password.encode()).hexdigest(), 0, izly_wallet))
    mysql.connection.commit()
    student_id = cur.lastrowid
    cur.close()
    
    response = {"student_id": student_id}
    return jsonify(response), 200


# POST connexion
@app.route('/api/login', methods=['POST'])
def post_login():
    # vérifier la présence des paramètres nécessaires
    if (request.json is None) or ('username' not in request.json) or ('password' not in request.json):
        return jsonify({'message': 'Paramètres requis manquants'}), 400
    
    username = request.json['username']
    password = request.json['password']

    # vérifier que les paramètres sont des chaînes de caractères
    if type(username) is not str or type(password) is not str:
        return jsonify({'message': 'Données de paramètre non valides'}), 400
    
    # vérifier que le mot de passe est valide
    if len(password) < 12 or len(password) > 255:
        return jsonify({'message': 'Le mot de passe ne respecte pas les exigences de longueur'}), 400
    
    # vérifier si le nom d'utilisateur existe
    cur = mysql.connection.cursor()
    cur.execute("SELECT student_id,password,blocked FROM Student WHERE username=%s", (username,))
    users_found = cur.rowcount
    response = cur.fetchone()
    cur.close()
    exists = (users_found > 0)

    if not exists:
        return jsonify({'message': 'Nom d\'utilisateur ou mot de passe non valide'}), 401
    
    student_id = response[0]
    hash = response[1]
    blocked = response[2]

    # vérifier si l'utilisateur est un professeur
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Support_Prof WHERE student_id=%s", (student_id,))
    prof_found = cur.rowcount
    cur.close()
    is_prof = (prof_found > 0)
   
    # vérifier si le mot de passe est correct
    if sha256(password.encode()).hexdigest() != hash:
        return jsonify({'message': 'Nom d\'utilisateur ou mot de passe non valide'}), 401
    
    # vérifier si l'utilisateur est bloqué
    if blocked:
        return jsonify({'message': 'L\'utilisateur est bloqué'}), 401
    
    # génére le JWT
    token = jwt.encode({'student_id': student_id, "is_prof": is_prof}, app.config['SECRET_KEY'], algorithm='HS256')

    resp = make_response(jsonify({'message': 'Connexion réussie', 'flag':('UHOCTF{Fake_flag_4}' if len(username) < 4 else 'Nope')}), 200)
    resp.set_cookie('token', token, httponly=True, samesite='Strict', max_age=None)

    return resp
