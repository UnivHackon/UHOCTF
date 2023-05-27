from __main__ import app, token_required, mysql
from flask import jsonify, request
from datetime import datetime

# Obtenir les informations sur le ticket
@app.route('/api/tickets/<int:ticket_id>', methods=['GET'])
@token_required
def get_ticket(session_data, ticket_id):
    # obtenir student_id à partir de ticket_id
    cur = mysql.connection.cursor()
    cur.execute("SELECT student_id, description, messages FROM Support_Tickets WHERE ticket_id=%s", (ticket_id,))
    response = cur.fetchone()
    cur.close()

    if not response and session_data['is_prof']:
        return jsonify({'message': 'Ticket introuvable'}), 404
    
    if not response or session_data['student_id'] != response[0]:
        return jsonify({'message': 'Vous n\'avez pas la permission d\'accéder à ces informations'}), 403

    response = {"ticket_id": ticket_id, "student_id": response[0], "description": response[1], "messages":response[2]}
    
    return jsonify(response), 200


# Créer un ticket
@app.route('/api/tickets', methods=['POST'])
@token_required
def post_create_ticket(session_data):
    # vérifier la présence des paramètres nécessaires
    if (request.json is None) or ('description' not in request.json):
        return jsonify({'message': 'Paramètres requis manquants'}), 400
    
    student_id = session_data["student_id"]
    description = request.json['description']
    timestamp = datetime.utcnow().isoformat()

    # vérifier que les paramètres sont des chaînes de caractères
    if type(description) is not str:
        return jsonify({'message': 'Données de paramètre non valides'}), 400

    # Insérer le ticket dans la base de données
    # UHOCTF{Fake_flag_2}

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO Support_Tickets (description, messages, time_stamp, student_id) VALUES (%s, %s, %s, %s)", (description, "", timestamp, student_id))
    mysql.connection.commit()
    ticket_id = cur.lastrowid
    cur.close()

    response = {"ticket_id": ticket_id, "description": description, "time_stamp": timestamp}

    return jsonify(response), 200


# Ajouter un message à un ticket
@app.route('/api/tickets/<int:ticket_id>', methods=['POST'])
@token_required
def post_add_message(session_data, ticket_id):
    # obtenir student_id à partir de ticket_id
    cur = mysql.connection.cursor()
    cur.execute("SELECT student_id, messages FROM Support_Tickets WHERE ticket_id=%s", (ticket_id,))
    response = cur.fetchone()
    cur.close()

    if not response and session_data['is_prof']:
        return jsonify({'message': 'Ticket introuvable'}), 404
    
    if not response or session_data['student_id'] != response[0]:
        return jsonify({'message': 'Vous n\'avez pas la permission d\'accéder à ces informations'}), 403

    # vérifier la présence des paramètres nécessaires
    if (request.json is None) or ('message' not in request.json):
        return jsonify({'message': 'Paramètres requis manquants'}), 400
    
    message = request.json['message']

    # vérifier que les paramètres sont des chaînes de caractères
    if type(message) is not str:
        return jsonify({'message': 'Données de paramètre non valides'}), 400
    
    # Insérer le message dans la base de données
    # UHOCTF{Fake_flag_3}
    cur = mysql.connection.cursor()
    new_message = response[1] + "\n" + message
    cur.execute("UPDATE Support_Tickets SET messages=%s WHERE ticket_id=%s", (new_message, ticket_id))
    mysql.connection.commit()
    cur.close()
    
    response = {"ticket_id": ticket_id, "message": message}

    return jsonify(response), 200
