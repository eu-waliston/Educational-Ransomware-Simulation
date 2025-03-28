# Educational Ransomware Simulation

## Aviso Legal
**Este projeto é estritamente educacional.**
Ele tem como objetivo demonstrar como funciona a criptografia de arquivos e a importância da segurança de dados. O uso inadequado ou malicioso dos scripts contidos neste repositório é de total responsabilidade do usuário.

**ATENÇÃO:** Não execute este projeto em máquinas com dados sensíveis ou em sistemas de produção. Utilize exclusivamente em ambientes controlados para fins de aprendizado.

## Sobre o Projeto
Este repositório contém scripts para criptografia e descriptografia de arquivos utilizando a biblioteca `cryptography` do Python. Ele simula um ransomware, criptografando arquivos pessoais e posteriormente permitindo a sua recuperação mediante a chave gerada.

### Scripts Incluídos
- **encrypt.py:** Criptografa arquivos dos diretórios do usuário (Documentos, Imagens, Vídeos, Downloads, AppData).
- **decrypt.py:** Descriptografa os arquivos previamente criptografados.

## Requisitos
- Python 3.x
- Biblioteca `cryptography`

### Instalando a Biblioteca
```bash
pip install cryptography
```

## Uso
### Criptografando Arquivos
```bash
python encrypt.py
```
### Descriptografando Arquivos
```bash
python decrypt.py
```

## Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

