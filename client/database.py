import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
# Use a service account
cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "castmath",
    "private_key_id": "3cf983c6ae319ea2ae904879c1859e9298c73517",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCpOnq4OTH3sGGH\nFgrjQdzmXRNAc1m6ofJW6mETWU8cRqtQ6P+4RfNeywyWkBpX71RmFg2GWbvaiijY\nWcX/D7GRw7AfH0Lf5698lWMfoMKrOx1yxsbBmofQOZfho2RV1jgcoQJLnXdygdqk\nUjDxZpQ5MYUe793UpGpJGuOwteFMGFTJmYpa3zFb9lf6IFJ1+hlZir5cMu5l7dhV\nr/FQG/gl81PG0xsa3aF4qQdLlIvccB2E1Cn0nWPdlR/qU09M7r0VoPHxF4EGZ6/d\nWiR3z6vKQao8tlZCPEYY3o+qqsLHcaBT/IngVbwsAkbfCTIZH2fBJmsF98YTVgay\nBMDMZOHLAgMBAAECggEAMDNGYfN0fnqABNRr7HfFfd2zzo8sVwKqfkQKu1KcPE8K\nm6SJtYhC/dRytO29ex9hWCRe3M3xOhlQ8fJ7+R6UspJctziVuSWJ77+y+H63A8N2\nK0tfsCQeG9pTnsKFoQc/ezQG7deffn9q8ZOxegiAHlwy8PFcKyVbWpAsmxfq4Fu0\nz0W6G2F+PfRFT77iGhBXPbhKx6uqsdaVG/eVZXE2BTLyoex9ihlsnxyOcuihrVRw\nETRsBGSuXTbS/h0SxLvDrlXkomSb/u2ESaW7hqwZ9jYWwMenppF6zv15wvna3+T3\nI5BohoAYPqHh3wWcdtfRk1EVRBf0RqT87xa3RSQ/mQKBgQDh5wobxBPhP4oui/1e\nvI1QoFEyNpIbet7SBJzvEGvRTQrU29S7tblK7NhJI0Q8EMPRG3vxARE4D6SS1qPr\nd6fUt9xxJFCqxjw8hUagc0T62+LFFJboS1Hgr7RQt2YZxN18H+VSEiRuu6JoA+zF\ndNKzd+1DM2Py3zRX1yO6yQQnuQKBgQC/xm54l5vcAWzu3NRnpWVVPZNCn+LTisle\nstIwg5Rtt72GI+1lC1AlTdgrF2xexbLnRAqk1NhZ4uSHDp+j/eRJ3hQdnQbSsPa1\ndz+xvGw8iFy6j8OJf/8GODGe7KK8eWjL7GXh8piIyrPkTUUfQIQ96kT2aDnd/RlQ\n8AuNxinPowKBgQDZQQ1jrqs/0Y/fPBqsZcGybLwqAnl5nC125aDX+X73h5SHKfPp\notdUy3smu5f//E+WZ0xHd7NLqx+naG21IxpxZXHIDhjWZFfCDJrj7HfGmnn499g6\nB1XzNIfBqN+0oLQxj6tHxtLq++ExD7VCIRwSJaA1JNNW3HrGj8148aHhYQKBgHnl\nrmh2rbotKcm2kkiDSCLjbcwmhu5BxHeuII53xIvtA8nU4luc0kez8FiLnfWromj/\nxeg55n9UCkCSmgSKKGaPg6fDHQglNdvovZLDGuVrI83t/bNTqY2RgHDtJw+3+FXO\noH/7TNt+RNQ0DWCtCKG2XDlnzIh/DW1191IZiJATAoGAWmabdmEa5oWfhvXssEjy\nYldGefV3sIo1BAN+bJDniqBNaYlVIv1eum+rHkbjS6UNvX2J6jZo+5jixcn2EhQW\nNUgbB7HRoOmCUf6mDJL/DdqB6DeIoXPNi9+pRDJ73VbN8ta4pXDsbuOf6h0EkYdc\n18l/NmRG7qNqgZlgkiVw9H0=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-gtc2k@castmath.iam.gserviceaccount.com",
    "client_id": "103368982436697228221",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-gtc2k%40castmath.iam.gserviceaccount.com"
})
firebase_admin.initialize_app(cred)
db = firestore.client()


def add(doc,name,data) :
    doc_ref = db.collection(doc).document(name)
    doc_ref.set(data)

def get(doc) :
    try:
        doc_ref = db.collection(doc).order_by(u'like', direction=firestore.Query.DESCENDING)
        writes = doc_ref.stream()
        data = []
        for write in writes :
            data.append(write.to_dict())
        return data
    except:
        return "error"

def get_doc(doc,name) :
    doc_ref = db.collection(doc).document(name)
    try:
        writes = doc_ref.get()
        if(writes.to_dict()==None) :
            return "error"
        else:
            return writes.to_dict()
    except:
        return "error"

def update(doc,name,data) :
    doc_ref = db.collection(doc).document(name)
    try:
        print(data)
        doc_ref.update(data)
    except:
        return "error"
    return 0

#GET IF IT HAVE (==)
def search(doc,search,value) :
    try :
        doc_ref = db.collection(doc).where(search, u'==', value)
        writes = doc_ref.stream()
        data = []
        for write in writes :
            data.append(write.to_dict())
        return data
    except:
        return "error"

def delete(doc,name) :
    db.collection(doc).document(name).delete()
    return 0

def search_delete(doc,search,value) :
    doc_ref = db.collection(doc).where(search, u'==', value).stream()
    for ref in doc_ref :
        ref.reference.delete()
    return 0
 
def add_arr(doc,name,arr,val) :
    city_ref = db.collection(doc).document(name)
    city_ref.update({arr: firestore.ArrayUnion([val])})
    return 0

def remove_arr(doc,name,arr,val) :
    city_ref = db.collection(doc).document(name)
    city_ref.update({arr: firestore.ArrayRemove([val])})
    return 0