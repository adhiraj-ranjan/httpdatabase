import firebase_admin
from firebase_admin import credentials, db
from os import environ
from base64 import b64decode
from json import loads

b64encoded_creds = environ['token'] # base 64 encoded firebase project credentials
JSON_CREDS = loads(b64decode(b64encoded_creds).decode())

cred = credentials.Certificate(JSON_CREDS)
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://safeapi-database-default-rtdb.asia-southeast1.firebasedatabase.app/" # database URL
})

store = db.reference("/keystores")

def create(key, val):
    if store.child(key).get()==None:
        store.update({key: val})
        return True
    else:
        return False

def get(key):
    value = store.child(key).get()
    if value!=None:
        return value
    else:
        return False

def update(key, val):
    if store.child(key).get() != None:
        store.update({key : val})
        return True
    else:
        return False

def delete(key):
    if store.child(key).get() != None:
        store.child(key).delete()
        return True
    else:
        return False
