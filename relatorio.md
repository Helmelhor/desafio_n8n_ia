# RELATÓRIO FINAL DO PROJETO

## Principais Desafios

- Entender quais nodes eram mais eficientes para utilizar no n8n, considerando a lógica dos workflows e a integração entre diferentes serviços.
- Encontrar documentações oficiais e exemplos práticos de uso das ferramentas envolvidas, especialmente para integrações menos comuns.
- Ajustar as tabelas na etapa de migração de dados: as três planilhas do Google Sheets possuíam estruturas diferentes, sem colunas padronizadas, exigindo adaptação e unificação dessas informações em um único modelo de tabela no banco PostgreSQL.
- Lidar com conflitos recorrentes entre o banco de dados e a API durante a inicialização dos containers, o que demandou diversas tentativas de solução e ajustes nos volumes e permissões.


## Estrutura de Pastas e Arquivos (nível raiz)

```
/  
├── api/              # Backend (API FastAPI, modelos, banco)
├── img/              # Imagens do projeto
├── n8n_data/         # Dados persistentes do n8n
├── postgres_data/    # Dados persistentes do PostgreSQL
├── streamlit_app/    # Aplicação frontend em Streamlit
├── workflows/        # Workflows exportados do n8n
├── docker-compose.yml# Orquestração dos containers Docker
├── README.md         # Documentação principal
├── relatorio.md      # Este relatório
```

## Softwares Utilizados


O primeiro passo foi a leitura completa do arquivo PDF recebido por e-mail, contendo as instruções do desafio técnico. Após isso, identifiquei as dependências de software necessárias para o desenvolvimento do projeto:


**Já instalado:**
- Visual Studio Code (VS Code)
- Python
- Git
- Dbeaver (para melhor acompanhamento e visualização do banco de dados)

**Necessário instalar:**
- Docker

O Docker foi a única instalação manual necessária, pois tanto o PostgreSQL quanto o n8n são executados em containers, dispensando instalação direta no sistema operacional. O Docker Compose gerencia toda a orquestração dos serviços.

Também criei um ambiente virtual Python para instalar e testar as bibliotecas necessárias ao projeto, evitando conflitos com pacotes instalados globalmente. As principais bibliotecas Python utilizadas foram:

- **fastapi**: Framework para construção da API backend.
- **uvicorn**: Servidor ASGI para rodar a aplicação FastAPI.
- **sqlalchemy**: ORM para manipulação do banco de dados PostgreSQL.
- **psycopg2-binary**: Driver para conexão Python com PostgreSQL.
- **pydantic**: Validação e serialização de dados na API.
- **streamlit**: Criação da interface web interativa para o usuário.

O uso do ambiente virtual garantiu que todas as dependências do projeto fossem isoladas, e também não houve relação ou conflitos com o docker em si.

## Funcionamento da Interface Streamlit

Já utilizei bastante na faculdade o streamlit. Ele facilita a criação de páginas web dinâmicas em Python, integrando facilmente com a API backend e outros serviços do sistema. Serve como o frontend do projeto, permitindo a interação do usuário de forma simples e intuitiva via navegador.


Durante o desenvolvimento, utilizei o modelo de IA Gemini, do Google, como ferramenta de apoio. A IA foi empregada principalmente para:
- Sugerir e validar a estrutura inicial de pastas e arquivos do projeto, facilitando a organização do ambiente de desenvolvimento.
- Auxiliar na compreensão e interpretação de mensagens de erro e logs, especialmente durante a configuração de containers, integração de serviços e depuração de código.
- Fornecer explicações rápidas sobre conceitos técnicos e boas práticas de desenvolvimento.

Apesar das sugestões e explicações fornecidas pela IA, todas as decisões finais sobre arquitetura, implementação, depuração e integração foram de minha responsabilidade. A IA foi utilizada como um recurso complementar para acelerar o entendimento e a resolução de problemas.


O arquivo **docker-compose.yml** é fundamental para projetos que utilizam múltiplos serviços, pois atua como orquestrador central. Ele permite definir, configurar e executar vários containers Docker de forma integrada e automatizada, facilitando a criação de ambientes completos para desenvolvimento, testes e produção. Com ele, é possível especificar imagens, variáveis de ambiente, volumes, dependências e redes de cada serviço (como banco de dados, backend, frontend e automações), garantindo que todos os componentes do sistema sejam inicializados na ordem correta e se comuniquem entre si de maneira eficiente.

**Observação:** Em alguns ambientes, ao realizar o deploy em uma máquina nova, pode ocorrer um conflito entre o banco de dados e a API, resultando no erro "could not open directory 'pg_notify': No such file or directory database system is shut down". Isso geralmente está relacionado a permissões ou corrupção de arquivos do volume do PostgreSQL. A solução temporária tem sido excluir os arquivos do banco e reiniciar os containers, eu ainda não consegui identificar o problema raiz.

## Sobre a pasta "api"

Esta pasta concentra todo o backend da aplicação, responsável pela criação da API, rotas e operações com o banco de dados. Principais arquivos:

- **main.py**: Inicializa a aplicação FastAPI, define as rotas e implementa as operações CRUD. Utiliza as bibliotecas FastAPI (API), SQLAlchemy (banco de dados) e Pydantic (validação de dados).
- **models.py**: Define o modelo de dados da tabela de eventos usando SQLAlchemy, estruturando as colunas e tipos do banco.
- **schemas.py**: Define os esquemas de dados (entrada e saída) com Pydantic, garantindo validação e organização dos dados trafegados pela API.
- **database.py**: Configura a conexão com o banco PostgreSQL via SQLAlchemy, lendo a variável de ambiente DATABASE_URL.
- **requirements.txt**: Lista as dependências do backend: FastAPI, Uvicorn (servidor ASGI), SQLAlchemy e psycopg2-binary (driver PostgreSQL).
- **Dockerfile**: Cria a imagem Docker da API, instalando dependências e configurando o ambiente.
- **wait-for-db.sh**: Script shell que garante que o banco esteja pronto antes de iniciar a API, evitando erros de conexão.

## Utilização do Postman

Durante o desenvolvimento, o software Postman poderia ter sido utilizado para testar rapidamente as rotas da API, simular requisições HTTP (GET, POST, PUT, DELETE) e validar as respostas dos endpoints sem a necessidade de criar uma interface própria ou scripts de teste. Por exemplo, seria possível enviar um POST para a rota /eventos/ com os dados de um novo evento e verificar se a resposta está correta, facilitando a identificação de erros e agilizando o processo de depuração da API. No entanto, o FastAPI já fornece uma interface interativa automática (Swagger UI).


## Sobre as pastas de dados

- **n8n_data**: Armazena configurações, workflows, credenciais e históricos do n8n. Assim, mesmo que o container seja reiniciado ou removido, as informações permanecem salvas e podem ser reutilizadas.
- **postgres_data**: Guarda os arquivos de dados do PostgreSQL, incluindo tabelas, índices e logs. Isso garante que os dados do banco não sejam perdidos ao reiniciar ou atualizar o container, mantendo a persistência das informações da aplicação.


## Outras pastas

- **img**: Armazena imagens utilizadas para documentação e compreensão do projeto.

- **workflows**: Contém os workflows criados no n8n e exportados como arquivos JSON. O usuário que for fazer o deploy deve importar esses arquivos no n8n da sua própria máquina.
    - **IA consulta eventos definitivo**: Workflow que utiliza um webhook para receber solicitações do usuário, podendo ser integrado tanto em ambiente de teste quanto de produção (por exemplo, na aplicação Streamlit). Possui lógica para registrar o histórico da conversa, integrar modelo de IA, memória e ferramentas (tools), além de realizar requisições HTTP para consultar, adicionar e (tentar) atualizar dados no banco via API. A funcionalidade de atualização via linguagem natural ainda não está funcionando corretamente.
    - **Migração de dados**: Workflow para transformar dados legados do Google Sheets em dados estruturados no banco de dados, facilitando a integração com modelos de IA. Utiliza nodes para ativação manual, leitura de planilhas (Google Sheets), mapeamento de campos (DE-PARA) e envio dos dados para a API via HTTP request. Para acessar o Google Sheets, foi necessário criar credenciais no Google AI Studio e ativar a API do Google Sheets.

## Referências

https://www.youtube.com/watch?v=3Ai1EPznlAc&list=TLGGfIFmonlLIkIyNDA4MjAyNQ&ab_channel=NateHerk%7CAIAutomation

https://www.youtube.com/watch?v=1T5srXrc6PA&ab_channel=Hiperautoma%C3%A7%C3%A3o

https://youtu.be/-GwjxOGxqxk?si=mGCSnntSrUN07kVb

https://youtu.be/DdoncfOdru8?si=qkBJpI8nzjlQXC2c