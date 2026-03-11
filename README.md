# Estudos Práticos de Cibersegurança

Este repositório documenta o inicio da minha jornada de aprendizado prático em Segurança da Informação, focado em entender vulnerabilidades (Offensive Security) e aplicar correções estruturais no código (Defensive Security).

##  Experimentos Realizados

1. Port Scanner (Python)
Objetivo: Entender a fase de Reconhecimento em testes de intrusão e o protocolo TCP (Three-Way Handshake).
Tecnologias: Python (`socket`, `concurrent.futures`).
Aprendizado: Evolução de um script sequencial lento para uma ferramenta de varredura multithread de alta performance, capaz de escanear portas comuns (ex: 135, 445) em segundos de forma assíncrona.

2. Auditoria Web (OWASP Top 10)
Objetivo: Identificar falhas críticas em aplicações web modernas utilizando o ambiente local do OWASP Juice Shop.
Vulnerabilidades Exploradas:
Quebra de Controle de Acesso (Bypass): Análise de código-fonte front-end (JavaScript minificado via DevTools) para mapear rotas ocultas e acessar painéis restritos sem botões de navegação.
SQL Injection (Login Bypass): Manipulação de queries de banco de dados diretamente pelo formulário de login (`' OR 1=1 --`) para assumir a conta de Administrador sem conhecimento da credencial.
Mitigação Proposta: Implementação rigorosa de Consultas Parametrizadas (Prepared Statements) no back-end para isolar inputs de usuários da lógica SQL.

OBS: Todas as técnicas ofensivas documentadas aqui foram executadas estritamente em ambientes locais (localhost) e aplicações intencionalmente vulneráveis (OWASP Juice Shop) para fins puramente acadêmicos e de auditoria defensiva.

3. Criptografia Simétrica em Python
Localização: /03-criptografia-python
- Implementação de algoritmos de proteção de dados (Data at Rest) utilizando o padrão AES via módulo Fernet.
- Prática de codificação e decodificação de bytes para ofuscação de mensagens confidenciais.
