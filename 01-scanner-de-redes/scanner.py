import socket
from datetime import datetime
import concurrent.futures  # A biblioteca mágica para gerenciar nossas threads

# 1. Definindo o alvo
alvo = "127.0.0.1"

# 2. Criamos uma função "trabalhadora"
# A única missão dessa função é testar UMA única porta.
def scan_port(porta):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        resultado = s.connect_ex((alvo, porta))
        
        if resultado == 0:
            print(f"[+] Porta {porta} está ABERTA")
            
        s.close()
    except Exception:
        pass # Se der algum erro inesperado na thread, apenas ignora e segue

# 3. O bloco principal de execução
if __name__ == "__main__":
    print("-" * 50)
    print(f"Iniciando varredura RÁPIDA no alvo: {alvo}")
    print(f"Horário de início: {datetime.now()}")
    print("-" * 50)

    # 4. Aqui está a mágica: criamos um "pool" com 100 trabalhadores (threads)
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        # Mapeamos a nossa função para o intervalo de portas de 1 a 1024
        # O executor distribui essas 1024 tarefas automaticamente entre as 100 threads
        executor.map(scan_port, range(1, 1025))
    
    print("-" * 50)
    print(f"Varredura finalizada: {datetime.now()}")