import firebase_admin
from firebase_admin import credentials, db

class DatabaseConnection:
    def __init__(self) -> None:
        self.service_account_key_path  = "C:/Users/cante/Desktop/Sauga/RSA_Cipher/service_account.json"
        self.cred = credentials.Certificate(self.service_account_key_path)
        self.init_database_connection(self.cred)

    def init_database_connection(self, cred):
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://rsa-cipher-text-default-rtdb.europe-west1.firebasedatabase.app/'
        })

    def upload_to_db(self, data: dict):
        ref = db.reference("/")
        ref.set(data)



