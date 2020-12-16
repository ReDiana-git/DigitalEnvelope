import json
from Crypto.Cipher import AES
from base64 import b64encode
from base64 import b64decode
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes

def encoder():
    data = b"The jab was the highly anticipated start of what public health experts hope is a nationwide wave of vaccinations that will signal the beginning of the end of the pandemic. The news coincided with a dark new milestone for the country "
    key = get_random_bytes(16)
    cipher = AES.new(key,AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    key = b64encode(key).decode('utf-8')
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    result =json.dumps({'iv':iv, 'ciphertext':ct})
    with open('Name.encrypt','w') as f:
        f.write(result)
    with open('Name.envelop','w') as f:
        f.write(key)
    print(key)
    
def decoder():
    try:
        with open('Name.encrypt','r') as f:
            b64 = json.load(f)
        with open('Name.envelop','rb',) as f:
            key = b64decode(f.read())
        iv = b64decode(b64['iv'])
        ct = b64decode(b64['ciphertext'])
        cipher = AES.new(key,AES.MODE_CBC,iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        print("The message was: ", pt)
    except KeyError:
        print("Incorrect decryption")