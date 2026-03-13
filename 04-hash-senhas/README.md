Laboratório de Hashing de Senhas (Bcrypt)

Este projeto demonstra a implementação de armazenamento seguro de credenciais utilizando a biblioteca Bcrypt em Python. O objetivo é aplicar as melhores práticas da indústria para proteção de senhas em bancos de dados.

Conceitos Aplicados:

- Função Hash Unidirecional: Transformação de senhas em texto puro para hashes irreversíveis, garantindo que as credenciais originais não sejam expostas em caso de vazamento de dados.
- Salt Criptográfico: Geração e concatenação de uma string aleatória (Salt) a cada senha antes do processamento. Esta técnica anula a eficácia de ataques utilizando tabelas pré-calculadas (Rainbow Tables).
- Fator de Custo (Cost Factor): Utilização da lentidão intencional do algoritmo Bcrypt para inviabilizar ataques de força bruta iterativos em larga escala.

Tecnologias:

- Python 3
- Biblioteca: bcrypt

Aplicações Práticas (Blue Team):
Implementação obrigatória em sistemas de autenticação, APIs de login e arquiteturas de banco de dados que armazenam informações de usuários.
