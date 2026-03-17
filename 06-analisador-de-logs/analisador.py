from collections import defaultdict

def analisar_logs():
    print("---  Analisador de Logs (SOC / Blue Team) ---\n")
    
    arquivo_log = "server.log"
    limite_falhas = 5
    

    tentativas_falhas = defaultdict(int)

    print(f"🔎 Varrendo o arquivo '{arquivo_log}' em busca de anomalias...\n")

    try:
        with open(arquivo_log, "r") as arquivo:
            for linha in arquivo:
                if "/login" in linha and "FAILED" in linha:
                    partes = linha.split()
                    
                    if len(partes) >= 3:
                        ip_suspeito = partes[2]
                        tentativas_falhas[ip_suspeito] += 1

        print(" Relatório de Ameaças:")
        print("-" * 30)
        
        ataque_detectado = False
        
        for ip, quantidade_falhas in tentativas_falhas.items():
            if quantidade_falhas > limite_falhas:
                print(f" ALERTA CRÍTICO: Ataque de Força Bruta detectado!")
                print(f"   IP Invasor: {ip}")
                print(f"   Tentativas bloqueadas: {quantidade_falhas} vezes")
                ataque_detectado = True
            elif quantidade_falhas > 0:
                print(f" Aviso: O IP {ip} errou a senha {quantidade_falhas} vez(es). (Normal)")

        if not ataque_detectado:
            print(" Tudo limpo. Nenhum ataque massivo detectado.")

    except FileNotFoundError:
        print(f"[!] Erro: O arquivo {arquivo_log} não foi encontrado na pasta.")

if __name__ == "__main__":
    analisar_logs()
