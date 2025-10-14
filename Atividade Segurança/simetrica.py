from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64

# Função para criptografar
def criptografar(mensagem, chave):
    cipher = AES.new(chave, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(mensagem.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + ct_bytes).decode()

# Função para descriptografar
def descriptografar(texto_cifrado, chave):
    data = base64.b64decode(texto_cifrado)
    iv = data[:16]
    ct = data[16:]
    cipher = AES.new(chave, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ct), AES.block_size).decode()

# Programa principal
mensagem = input("Digite a mensagem: ")
chave = get_random_bytes(16)  # Gera uma chave aleatória
texto_cifrado = criptografar(mensagem, chave)
print("Criptografado:", texto_cifrado)
texto_decifrado = descriptografar(texto_cifrado, chave)
print("Descriptografado:", texto_decifrado)
