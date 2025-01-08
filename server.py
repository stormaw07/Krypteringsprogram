from cryptography.fernet import Fernet #Importerer Fernet, som krypterer med base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import random, base64, os

def dekryptering():
    privKeyServer1 = random.randint(1000000,2000000)
    modulaServer1 = 3**privKeyServer1 % 17
    #Send modula til client
    #Hent modula far client
    kodeServer1 = ((modulaClient1**privKeyServer1) % 17)+1

    privKeyServer2 = random.randint(1000000,2000000)
    modulaServer2 = 3**privKeyServer2 % 17
    #Send modula til client
    #Hent modula far client
    kodeServer2 = ((modulaClient2**privKeyServer2) % 17)+1

    kodeServer = kodeServer1**kodeServer2

    passwordServer = f"{kodeServer}".encode("utf-8")
    salt = os.urandom(16)
    kdf1 = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=480000,
    )   
    keyServer = base64.urlsafe_b64encode(kdf1.derive(passwordServer))

    #Hent melding fra client
    server = Fernet(keyServer)
    decMessage = server.decrypt(encMessage).decode()
    print(decMessage)