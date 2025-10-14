import rsa
import base64

print("Gerando par de chaves RSA...")
(public_key, private_key) = rsa.newkeys(2048)

mensagem = input("Digite a mensagem para criptografar: ")

mensagem_criptografada = rsa.encrypt(mensagem.encode(), public_key)

print("\nCriptografada (com chave pública):", base64.b64encode(mensagem_criptografada).decode())

mensagem_descriptografada = rsa.decrypt(mensagem_criptografada, private_key)

print("Descriptografada (com chave privada):", mensagem_descriptografada.decode())