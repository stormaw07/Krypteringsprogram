from cryptography.fernet import Fernet #Importerer Fernet, som krypterer med base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import random, base64, os

privKeyServer1 = random.randint(1000000,2000000)
privKeyClient1 = random.randint(1000000,2000000)
modulaServer1 = 3**privKeyServer1 % 17
modulaClient1 = 3**privKeyClient1 % 17
kodeServer1 = ((modulaClient1**privKeyServer1) % 17)+1
kodeClient1 = ((modulaServer1**privKeyClient1) % 17)+1

privKeyServer2 = random.randint(1000000,2000000)
privKeyClient2 = random.randint(1000000,2000000)
modulaServer2 = 3**privKeyServer2 % 17
modulaClient2 = 3**privKeyClient2 % 17
kodeServer2 = ((modulaClient2**privKeyServer2) % 17)+1
kodeClient2 = ((modulaServer2**privKeyClient2) % 17)+1

kodeServer = kodeServer1**kodeServer2
kodeClient = kodeClient1**kodeClient2

print(kodeServer,kodeClient)

passwordServer = f"{kodeServer}".encode("utf-8")
passwordClient = f"{kodeClient}".encode("utf-8")
print(passwordServer,passwordClient)
salt = os.urandom(16)
kdf1 = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=480000,
)
kdf2 = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=480000,
)
keyServer = base64.urlsafe_b64encode(kdf1.derive(passwordServer))
keyClient = base64.urlsafe_b64encode(kdf2.derive(passwordClient))

server = Fernet(keyServer)
client = Fernet(keyClient)

message = "hei"

encMessage = client.encrypt(message.encode())
print(encMessage)
decMessage = server.decrypt(encMessage).decode()
print(decMessage)