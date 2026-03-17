Laboratório de Análise de Logs (SOC / Blue Team)

Este projeto simula a operação de uma ferramenta de monitoramento de Segurança Defensiva (SIEM). O script em Python foi desenvolvido para analisar registros (logs) de servidores web e detectar anomalias comportamentais que indicam ataques cibernéticos.

Conceitos Aplicados:

- Parseamento de Dados: Leitura e extração de informações específicas (IPs, Endpoints, Status) de arquivos de texto não estruturados utilizando as funções nativas de manipulação de strings do Python.
- Detecção de Anomalias (Thresholding): Implementação de uma lógica condicional baseada em limites (Cost Factor/Threshold) para diferenciar o comportamento de um usuário comum cometendo um erro de digitação de um ataque automatizado.
- Estruturas de Dados Dinâmicas: Utilização do módulo `collections.defaultdict` para otimizar a contagem e agregação de dados em tempo de execução.

Tecnologias:

- Python 3

Aplicações Práticas (Blue Team):
Lógica fundamental utilizada em Centros de Operações de Segurança (SOC) para criação de regras de alerta e em softwares como Fail2Ban para bloqueio automatizado de ataques de Força Bruta e Credential Stuffing.
