import firebase_admin
from firebase_admin import credentials, db


JSON_CREDS = {
    "type": "service_account",
    "project_id": "safeapi-database",
    "private_key_id": "e0df0f5cedf63720da1ed68badce4b07ff293647",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC01hRkJFOp53Qx\nMjcy+p0kA0MQ9Am+Sub2oE57DiZRD9J6zsGRgeKyBgCgB08Yx53SeQhAnfd0eqMD\nxIoIp096UoxY3j1ICZiOro09lLl6HYZ//SAvGPpdhxVbZQVwvcSmKNsm5FlmX8xq\nCQGrnXsFZmzPr1y6tXhsfIS9+hquBzOhW7RUc4GPcPgxYlTnxZgPVAeI9+4hYLtj\nzm5GbHVa5lHqK+XN+UsXm9rPZx0OeRBcvg5Te1yc33nvTIIZn8qce6PFVEd7q0nb\nyG2zrYmjb2hc5lCM/I3DvNaRGEq1xcfV8f9oCaN35mvpMtrINOim75wUMg0BFke1\nXf01ZZT3AgMBAAECggEAAjNoyoWdDw0ZRbZnimAXPkz1dmT1Iv++XkBtNBb9mGPD\nTmm3XJH8GraMycwzX9XUfq9CaA1Q6akxOrNPPfO4H+di4q7LVO+Cj80ub6vTstmR\nI+JswqX6X6qfmlEmBwBupQ1yPVlVTTQO3mt/PbUMJKPhrYiXOrgV3+jtpKV0L0Uz\nh3/YrUbSiufAv9zYd54viCzrga90sI6yrSvhB9yAsgkf825UtczEdgSjQzOnXM4j\nnaOsHeOtEdg3KGqopcmhmIyV94SoaKVJctwnPLGFvohNSNNsjs+8ic9C5QDdpzoB\nWAZHo6nU6Yikvm6p1ef3Z2POJlerdrS/1mNdY6aRoQKBgQDbRnRRZuy8aTF0A62I\n0O217lmBU5OxEA80ddYaJlfc3OLjLXeg79/4eYyYY6qgrRgQw+DP6/BuV0lKO0wR\n5F3kDJBopDR0zwF9bRghFqweaQcIZ5az9i95wqLTOjbXU+/+KgTtoCx6nzq98IDF\ny8YUKNDtIv5S/6m9LJsHGpZF5QKBgQDTH4iU5PT7izE/fMsHxJh6JjnKs0kHZf4Q\n227DY+Ohb06KzbBfRd+YFBP73ErwzomwlT29QuQbfSZtIAhQOalR9nC22/sg0+sd\nyAtLDsSNXGo7IogrqbUmglJGyPauJyTyXDD292hmrMbvvplYlzNaOEaAjDiJ/00r\nSuETLdMBqwKBgHdP4sLYSkBKzMnfpnEnnfC8fJ9OJrLVljBpXdJkwrI+zoXmm41K\neIfvO30/3fwHs2yL6Ku6Kd0gSZTGpyGlLSGFZJ5Lmu9kI99nmRWIDKePZnBATVQm\nxLZwHcDpkCWiWpflrUDPQuSF96SaVLdLpcAaZXRi8hefXXC98Kzw3ouxAoGAavOe\njU8vi/6HhFIDyHufgsG6pSUN6eGRQ5jmE7WWq0Fn2Ik6wAj1rGT/eqeujy8SMZJp\nJGeuhv5vaPjBPWL4k7z0fK4UGh1BDmU401031STr6+kicnwWeNusMo+7552M6foq\nE/JhwSHl5a34oRh3u0ym6pgeTEo5HaVhQAYGzuECgYB03GnjDHGCMR/JptckFqSj\nDFqCYoU276oPZgcvVTsfkiDQNgYdkDbmfwsfEaD+/xb/XMqDMp51pZoDRIvWzqYt\nmB+g/V4mG61jSInbt0UM2Pjg1CHqthwUDFk/BfIj9rL+U6RBOjVm2SKhrbjIZN33\nMCMWS4Iq3cvz10cXWFYhiQ==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-01nnt@safeapi-database.iam.gserviceaccount.com",
    "client_id": "104051987979828961945",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-01nnt%40safeapi-database.iam.gserviceaccount.com"
}

cred = credentials.Certificate(JSON_CREDS)
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://safeapi-database-default-rtdb.asia-southeast1.firebasedatabase.app/"
})

store = db.reference("/keystores")


def create(key, val):
    if not store.child(key).get():
        store.update({key: val})
        return True
    else:
        return False

def get(key):
    value = store.child(key).get()
    if value:
        return value
    else:
        return False

def update(key, val):
    if store.child(key).get():
        store.update({key : val})
        return True
    else:
        return False

def delete(key):
    if store.child(key).get():
        store.child(key).delete()
        return True
    else:
        return False