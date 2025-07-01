from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
import xmltodict
app = Flask(__name__)
# initialize Firebase
def initialize_firebase():
    try:
        cred=credentials.Certificate('/home/ahmed121176/mysite/p-9318-ahmed-bse-5b-project-firebase-adminsdk-f7jn6-13df3b6df6.json')
        firebase_admin.initialize_app(cred)
        return firestore.client()
    except Exception as e:
        print(f"Error initializing Firebase: {e}")
        return None
# initialize Firestore client
db = initialize_firebase()

def parse_xml_to_dict(xml_data):
    """Utility function to convert XML to a Python dictionary."""
    try:
        return xmltodict.parse(xml_data)
    except Exception as e:
        print(f"Error parsing XML: {e}")
        return None

def save_user_to_firestore(name, email):
    """Utility function to save user information to Firestore."""
    try:
        doc_ref = db.collection('users').add({
            'name': name,
            'email': email
        })
        return doc_ref[1].id  # document ID return
    except Exception as e:
        print(f"Error saving to Firestore: {e}")
        return None

@app.route('/receive-data', methods=['POST'])
def receive_data():
    if not db:
        return jsonify({'error': 'Firestore initialization failed'}), 500

    # parse XML data from the request
    xml_data = request.data
    data_dict = parse_xml_to_dict(xml_data)
    if not data_dict:
        return jsonify({'error': 'Invalid XML data'}), 400

    # extract user information
    user_info = data_dict.get('user', {})
    name = user_info.get('name')
    email = user_info.get('email')

    # validate required fields
    if not name or not email:
        return jsonify({'error': 'Missing name or email in XML data'}), 400

    # save user information to Firestore
    document_id = save_user_to_firestore(name, email)
    if not document_id:
        return jsonify({'error': 'Failed to save user to Firestore'}), 500

    # return stored data
    return jsonify({
        'id': document_id,
        'name': name,
        'email': email
    }), 201

@app.route('/test-firestore', methods=['GET'])
def test_firestore():
    if not db:
        return jsonify({'error': 'Firestore initialization failed'}), 500

    try:
        # get collections from Firestore
        collections = db.collections()

        # retrieve and return collection names
        collection_names = [collection.id for collection in collections]
        return jsonify({'collections': collection_names}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)