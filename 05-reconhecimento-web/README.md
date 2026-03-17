Laboratório de Reconhecimento Web (Directory Fuzzing)

Este projeto consiste no desenvolvimento de um enumerador de diretórios (Fuzzer) automatizado em Python, projetado para mapear a superfície de ataque de aplicações web descobrindo rotas e pastas ocultas.

Conceitos Aplicados:

- Automação de Requisições HTTP: Utilização de scripts para disparo massivo de requisições GET a partir de uma wordlist personalizada.
- Bypass de Falsos Positivos (Catch-all): Implementação de uma lógica de baseline de tamanho de resposta (Response Length). O script calibra o tamanho da página raiz e ignora páginas de erro genéricas que retornam Status 200 (comum em SPAs e hospedagens cloud como Firebase/Vercel).
- Tratamento de Exceções: Controle de timeouts e quedas de conexão para evitar o travamento da ferramenta durante a varredura.

Tecnologias:

- Python 3
- Biblioteca: requests

Aplicações Práticas (Red Team / Bug Bounty):
Ferramenta fundamental na fase de Information Gathering para localizar painéis administrativos expostos, diretórios de backup não protegidos e endpoints de APIs ocultas.
