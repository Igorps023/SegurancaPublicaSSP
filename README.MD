
# Indicadores e estatísticas de violência para o Estado de São Paulo
##### Arquitetura de dados utilizada: Data Lake (processamento batch - event driven)
##### Tecnologias: AWS, SPARK, SQL, PYTHON, POWER BI

**Objetivo do projeto:**
1. Coleta de dados da web.
2. Armazenamento dos dados em ambiente cloud (AWS).
3. Processamento dos dados utilizando PySpark (framework para processamento de big data).
4. Tratamento dos dados e disponibilização em camadas (Raw, Trusted e Refined), podendo ser consumidas por outros usuários e áreas.
5. Criação de um dashboard analítico para facilitar a visualização das informações.

Coleta de dados via (API)
- https://basedosdados.org/dataset/dbd717cb-7da8-4efd-9162-951a71694541?table=a2e9f998-e2c2-49b7-858a-ae1daef46dc0

Coleta de arquivos Excel (XLSX)
- https://www.ssp.sp.gov.br/estatistica/dados-mensais

##### Diagrama da Arquitetura de Dados (Data Lake):
![Event Driven Pipeline](https://github.com/Igorps023/SegurancaPublicaSSP/blob/main/Arquitetura%20Lake%20Event%20Driven.drawio.png?raw=true "Event Driven Pipeline")


Os scripts e notebooks utilizados estão disponíveis nas respectivas pastas.

##### Dashboard feito em Power BI:
![Dashboard](https://github.com/Igorps023/SegurancaPublicaSSP/blob/main/SSP_Dashboard.png?raw=true "Dashboard")

Arquivo .pbix está disponível para download.

Obrigado!
