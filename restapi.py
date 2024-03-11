from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

# Verbindungsparameter für die Azure-Datenbank eintragen
"""connection = pymysql.connect(
    host='your_azure_mysql_server',
    user='your_username',
    password='your_password',
    db='your_database',
    cursorclass=pymysql.cursors.DictCursor
)"""

@app.route('/get_question', methods=['GET'])
def get_question():
    try:
        # Hier SQL-Abfrage ausführen, um eine Frage aus der Datenbank zu erhalten
        # Beispiel: with connection.cursor() as cursor:
        # Frage abrufen und zurückgeben
        question = "Wie lautet die Frage?"
        return jsonify({"question": question})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)