import firebase_admin
from firebase_admin import credentials, db

class DatabaseConnection:
    def __init__(self) -> None:
        self.service_account_key_path  = "type in path to service_account.json"
        self.cred = credentials.Certificate(self.service_account_key_path)
        self.init_database_connection(self.cred)

    def init_database_connection(self, cred):
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://rsa-cipher-text-default-rtdb.europe-west1.firebasedatabase.app/'
        })

    def upload_to_db(self, data: dict):
        db_ref = db.reference("/")
        db_ref.set(data)

    def retrieve_from_db(self) -> list:
        db_ref = db.reference("/")
        data = db_ref.get()
        retrieved_set = list(data["Encrypted Text"])
        return retrieved_set




