from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


def makekeys(name):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    with open(name + '.key', 'wb') as f:
        f.write(private_pem)

    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    with open(name + '.pub', 'wb') as f:
        f.write(public_pem)


def encryp(key,name):
    with open(name + '.pub', 'rb') as f:
        public_key = serialization.load_pem_public_key(
            f.read(),
        )
    # with open('note.txt', 'r') as f:
    #    message = f.read().encode(encoding="gb2312")
    # message = b"encrypted data"
    message = key
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    with open(name + '.envelop', 'wb') as f:
        f.write(ciphertext)
    # print(ciphertext)


def decryp(name):
    with open(name + '.key', 'rb') as f:
        private_key = serialization.load_pem_private_key(
            f.read(),
            password=None,
        )
    with open(name + '.envelop', 'rb') as f:
        ciphertext = f.read()
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    # print(plaintext)
    return plaintext


def prtByte():
    with open('note.txt', 'r') as f:
        message = f.read().encode(encoding="gb2312")
    print(message)
    message = b"encrypted data"
    print(message)