import hashlib

mensagem = input("Digite a mensagem para gerar o hash: ")

hash_obj = hashlib.sha256(mensagem.encode())

hash_final = hash_obj.hexdigest()

print("\nHash SHA-256 da mensagem:", hash_final)
print("Tamanho do Hash:", len(hash_final), "caracteres")


print("\n--- Teste de Integridade ---")
print("Veja como o hash muda completamente se adicionarmos apenas um '.' no final da mensagem.")

mensagem_alterada = mensagem + "."
hash_alterado_obj = hashlib.sha256(mensagem_alterada.encode())
hash_alterado_final = hash_alterado_obj.hexdigest()

print(f"Hash para '{mensagem}':\n{hash_final}")
print(f"\nHash para '{mensagem_alterada}':\n{hash_alterado_final}")