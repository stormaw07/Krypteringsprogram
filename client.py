from cryptography.fernet import Fernet #Importerer Fernet, som krypterer med base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import random, base64, os

def kryptering():
    privKeyClient1 = random.randint(1000000,2000000)
    modulaClient1 = 3**privKeyClient1 % 17
    #Send modula til server
    #Hent modula far server
    kodeClient1 = ((modulaServer1**privKeyClient1) % 17)+1

    privKeyClient2 = random.randint(1000000,2000000)
    modulaClient2 = 3**privKeyClient2 % 17
    #Send modula til server
    #Hent modula far server
    kodeClient2 = ((modulaServer2**privKeyClient2) % 17)+1

    kodeClient = kodeClient1**kodeClient2

    passwordClient = f"{kodeClient}".encode("utf-8")
    salt = os.urandom(16)
    kdf1 = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=480000,
    )
    keyClient = base64.urlsafe_b64encode(kdf2.derive(passwordClient))

    message = "hei"
    client = Fernet(keyClient)
    encMessage = client.encrypt(message.encode())
    print(encMessage)
