import firebase_admin
from firebase_admin import credentials, firestore


# initialize sdk
cred = credentials.Certificate("driver-drowsiness-system-firebase-adminsdk-cja97-3c44680dfc.json")
firebase_admin.initialize_app(cred)


# initialize firestore instance
firestore_db = firestore.client()


# add data
firestore_db.collection(u'songs').add({'song': 'Imagine', 'artist': 'John Lennon'})


# read data
snapshots = list(firestore_db.collection(u'songs').get())
for snapshot in snapshots:
    print(snapshot.to_dict())
