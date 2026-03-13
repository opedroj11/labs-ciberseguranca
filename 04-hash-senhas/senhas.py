import bcrypt

def executar_laboratorio():
    print("--- 🛡️ Laboratório de Hashing de Senhas (Bcrypt) ---\n")

    # 1. O CADASTRO DO USUÁRIO
    senha_digitada = "MinhaSenhaSuperSegura123"
    print(f"👤 Usuário digitou no cadastro: {senha_digitada}")

    # Gerando o "Salt" (Um texto aleatório adicionado à senha antes do hash).
    # O Salt impede que o hacker use tabelas prontas de hashes (Rainbow Tables) para quebrar senhas comuns.
    salt = bcrypt.gensalt()
    
    # Gerando o Hash (precisamos converter a string para bytes usando encode)
    senha_hasheada = bcrypt.hashpw(senha_digitada.encode('utf-8'), salt)
    
    print(f"💾 O que é salvo no Banco de Dados: {senha_hasheada}\n")
    print("Repare que nem o administrador do banco sabe qual é a senha real!\n")

    # 2. A TENTATIVA DE LOGIN
    print("--- 🔐 Simulando o Login ---")
    senha_tentativa = "MinhaSenhaSuperSegura123"
    
    # O Bcrypt pega a senha tentada, aplica a mesma matemática e verifica se bate com o hash salvo
    if bcrypt.checkpw(senha_tentativa.encode('utf-8'), senha_hasheada):
        print(f"✅ Sucesso! A senha '{senha_tentativa}' confere com o Hash do banco.")
    else:
        print("❌ Acesso Negado! Senha incorreta.")

if __name__ == "__main__":
    executar_laboratorio()