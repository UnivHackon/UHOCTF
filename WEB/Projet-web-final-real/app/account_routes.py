# imports
from __main__ import app, token_required, VPS_PRICE_LINUX_WINDOWS, VPS_PRICE_MACOS, mysql
from flask import jsonify, request
import ipaddress

# POST ajouter un bot en tant qu'affilié
@app.route('/api/vps', methods=['POST'])
@token_required
def post_add_bot(session_data):
    # vérifier la présence des paramètres nécessaires
    if (request.json is None) or ('os' not in request.json) or ('ip_address' not in request.json):
        return jsonify({'message': 'Paramètres requis manquants'}), 400
    
    os = request.json['os']
    ip_address = request.json['ip_address']

    # vérifier que les paramètres sont des chaînes de caractères
    if type(os) is not str or type(ip_address) is not str:
        return jsonify({'message': 'Données de paramètre non valides'}), 400
    # valider 
    if os not in ['Windows', 'Linux', 'MacOS']:
        return jsonify({'message': 'Système d\'exploitation non valide'}), 400
    
    # valider l'adresse IP
    try:
        ipaddress.ip_address(ip_address)
    except ValueError:
        return jsonify({'message': 'Adresse IP non valide'}), 400
    
    # vérifier si l'adresse IP a déjà été ajoutée
    cur = mysql.connection.cursor()
    cur.execute("SELECT vps_id FROM Vps WHERE ip_address=%s", (ip_address,))
    response = cur.fetchone()
    if response:
        return jsonify({'message': 'Adresse IP déjà ajoutée'}), 400

    # ajouter le bot à la base de données
    #UHOCTF{Fake_flag_5}

    cur.execute("INSERT INTO Vps (os, ip_address) VALUES (%s, %s)", (os, ip_address))
    mysql.connection.commit()
    vps_id = cur.lastrowid
   

    response = {"vps_id": vps_id, "paiement": VPS_PRICE_LINUX_WINDOWS if os!='MacOS' else VPS_PRICE_MACOS}
    
    return jsonify(response), 200
