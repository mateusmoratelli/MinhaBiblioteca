import uuid

def gerarUUID():
    # Gerar um UUID versão 4
    uuid_aleatorio = str(uuid.uuid4())
    print("UUID (versão 4):", uuid_aleatorio)
    return uuid_aleatorio
