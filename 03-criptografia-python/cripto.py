from cryptography.fernet import Fernet

def executar_laboratorio():
    print("--- 🛡️ Laboratório de Criptografia Simétrica ---\n")

    # 1. GERAÇÃO DA CHAVE (O Segredo)
    # Aqui o Python cria uma chave aleatória super segura. Quem tiver essa chave, lê a mensagem.
    chave = Fernet.generate_key()
    fernet = Fernet(chave)
    print(f"🔑 Chave gerada: {chave}\n")

    # 2. A MENSAGEM ORIGINAL
    # O texto puro que queremos proteger.
    mensagem_original = "Relatorio Confidencial: Falha critica no servidor."
    print(f"📄 Texto Original: {mensagem_original}")

    # 3. CRIPTOGRAFANDO (O Bloqueio)
    # O método encrypt precisa que o texto seja convertido para bytes (encode) antes de embaralhar.
    mensagem_criptografada = fernet.encrypt(mensagem_original.encode())
    print(f"🔒 Texto Criptografado: {mensagem_criptografada}\n")

    # 4. DESCRIPTOGRAFANDO (A Revelação)
    # O método decrypt pega o texto embaralhado, usa a chave e converte de volta para texto legível (decode).
    mensagem_descriptografada = fernet.decrypt(mensagem_criptografada).decode()
    print(f"🔓 Texto Descriptografado: {mensagem_descriptografada}\n")

if __name__ == "__main__":
    executar_laboratorio()