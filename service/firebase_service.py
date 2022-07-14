import firebase_admin
from firebase_admin import credentials, db

QUEUE_BASE_PATH = "queue/"
MAX_QUEUE_ENTRIES = 1000

cred = credentials.Certificate("service/firebase.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://mc855g3-b7d57-default-rtdb.firebaseio.com"
})


def add_entry(data, id):
    ref = db.reference(QUEUE_BASE_PATH + id)
    ref.set(data)
    delete_older_entries(QUEUE_BASE_PATH)


def delete_entry(id):
    ref = db.reference(QUEUE_BASE_PATH + id)
    ref.delete()


def delete_older_entries(path):
    ref = db.reference(path)
    data = ref.order_by_child('arrived_timestamp').get()
    to_delete = len(data) - MAX_QUEUE_ENTRIES
    if to_delete > 0:
        for key, val in data.items():
            if to_delete == 0:
                break
            delete_ref = ref.child(key)
            delete_ref.delete()
            to_delete = to_delete - 1


def read_entries():
    ref = db.reference(QUEUE_BASE_PATH)
    return ref.order_by_child('arrived_timestamp').get()