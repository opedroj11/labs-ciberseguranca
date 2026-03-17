import requests

def executar_laboratorio():
    print("--- 🛡️ Laboratório de Reconhecimento Web (Fuzzer v2.0) ---\n")

    alvo = "https://github.com/" 
    
    print(f"🎯 Alvo: {alvo}")
    
    try:
        # 1. CALIBRAGEM: Descobrindo o tamanho da página principal (Baseline)
        print("Calibrando o filtro de Falsos Positivos...")
        resposta_base = requests.get(alvo, timeout=5)
        tamanho_base = len(resposta_base.text)
        print(f"Tamanho padrão da página: {tamanho_base} bytes\n")

        with open("wordlist.txt", "r") as arquivo:
            # Lendo as linhas e removendo duplicatas com 'set()' (Isso limpa aqueles 'admin' repetidos!)
            diretorios = set(arquivo.readlines())
            
            print("Iniciando o ataque...")
            for diretorio in diretorios:
                diretorio_limpo = diretorio.strip()
                if not diretorio_limpo: # Pula linhas em branco
                    continue
                    
                url_teste = f"{alvo}{diretorio_limpo}"
                
                try:
                    resposta = requests.get(url_teste, timeout=3)
                    tamanho_atual = len(resposta.text)
                    
                    # 2. O FILTRO: Só mostra se for Status 200 E o tamanho for diferente do padrão
                    if resposta.status_code == 200:
                        if tamanho_atual != tamanho_base:
                            print(f"[+] ENCONTRADO (Tamanho: {tamanho_atual}b): {url_teste}")
                        # Se for igual, ele silenciosamente ignora o falso positivo
                            
                except requests.exceptions.Timeout:
                    pass # Ignora erros de lentidão para não poluir a tela
                except requests.exceptions.RequestException:
                    pass
                    
        print("\nVarredura concluída!")
                    
    except FileNotFoundError:
        print("[!] Erro: Arquivo wordlist.txt não encontrado.")

if __name__ == "__main__":
    executar_laboratorio()