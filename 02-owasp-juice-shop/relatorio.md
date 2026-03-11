Relatório de Auditoria Web: OWASP Juice Shop

Este documento detalha as vulnerabilidades exploradas durante o laboratório prático no ambiente intencionalmente vulnerável do OWASP Juice Shop. O foco desta auditoria foi identificar falhas no controle de acesso e na camada de banco de dados.

---

1. Quebra de Controle de Acesso (Broken Access Control)

- Vulnerabilidade: Acesso indevido à página de Placar (Score Board).
- Vetor de Ataque: O desenvolvedor utilizou Segurança por Obscuridade, apenas ocultando o link da interface visual.
- Execução:
  1. Utilizando as ferramentas de desenvolvedor do navegador (DevTools - Aba Sources).
  2. Mapeamento do código JavaScript minificado do front-end (Angular).
  3. Descoberta da rota oculta path:"score-board".
  4. Acesso direto via manipulação da URL no navegador para a referida rota.
- Impacto: Usuários não autenticados podem acessar páginas restritas ou painéis administrativos, uma vez que a validação de acesso não está sendo feita pelo servidor.
- Mitigação Recomendada: O servidor (back-end) deve sempre validar o token de sessão e os privilégios do usuário em todas as requisições de páginas sensíveis.

---

2. Injeção de Banco de Dados (SQL Injection)

- Vulnerabilidade: Bypass de autenticação na tela de Login.
- Vetor de Ataque: Falta de sanitização dos dados de entrada do usuário antes da concatenação na instrução SQL.
- Execução:
  1. No campo de e-mail, foi inserido o payload de escape: ' OR 1=1 --
  2. A primeira aspa fecha a string esperada pelo banco. O comando OR 1=1 força a condição a ser obrigatoriamente verdadeira. Os traços duplos anulam a verificação de senha no restante da instrução.
  3. O banco de dados retornou o primeiro usuário da tabela, concedendo acesso total à conta de Administrador.
- Impacto: Nível Crítico. Comprometimento total da conta de administrador, com potencial vazamento de todos os dados sensíveis do banco.
- Mitigação Recomendada: Substituir a concatenação de strings no código-fonte por Consultas Parametrizadas (Prepared Statements). Dessa forma, a aplicação obriga o banco de dados a tratar a entrada do usuário estritamente como dado de texto, impedindo a execução de códigos não autorizados.
