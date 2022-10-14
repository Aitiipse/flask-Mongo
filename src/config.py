from pymongo import MongoClient
import certifi

MONGO = 'mongodb+srv://Administrador:Admin123@clusterinicial.qs8uapd.mongodb.net/?retryWrites=true&w=majority'
certificado = certifi.where()

def conexion():
    try:
        client = MongoClient(MONGO, tlsCAFile=certificado)
        bd = client["bd_personas"]
    except ConnectionError:
        print('error de conexion')
    return bd